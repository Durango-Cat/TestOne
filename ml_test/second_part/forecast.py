'''
估计器: 常见的方法：fit()
转换器：常见的方法：transform()
预测器
'''

import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split        # 跟下面实现的split_train_test方法一样。
from sklearn.model_selection import StratifiedShuffleSplit  # 分层采样
from sklearn.impute import SimpleImputer  # 指定用某属性的中位数来替换该属性所有的缺失值
from sklearn.preprocessing import LabelEncoder # 预处理的方式一转换器
from sklearn.preprocessing import OneHotEncoder # 预处理的方式一独热编码
from sklearn.preprocessing import LabelBinarizer # 预处理的方式二
from sklearn.preprocessing import CategoricalEncoder

# 读取housing下面的csv文件
def load_housing_data():
    pwd_path = os.path.dirname(__file__)
    # print(pwd_path)
    sep = os.sep  # 系统的分隔符，windows和mac方向不一样。
    csv_path = os.path.join(pwd_path + sep + "housing" + sep + "housing.csv")
    return pd.read_csv(csv_path)


# 将读取到的文件内容，分为80%为训练数据，20%为测试数据
def split_train_test(data, test_ratio):
    # numpy.random.seed()函数可使得随机数具有预见性，即当参数相同时使得每次生成的随机数相同；当参数不同或者无参数时，作用与numpy
    # .random.rand()函数相同，即多次生成随机数且每次生成的随机数都不同。

    # 产生相同的洗牌指数，就是每次执行下面的随机都是一样的随机列表
    '''
    为啥需要洗牌？
    因为不打乱顺序，很容易产生过拟合，模型泛化能力下降
    '''
    np.random.seed(44)
    #创建一个data数据的长度的列表，里面元素随机排列。如果光写一个数值的话，那这个列表里面的元素是从0到n-1。如果传的是个列表，就将列表的元素随机排列
    shuffled_indices = np.random.permutation(len(data)) 
    test_set_size = int(len(data) * test_ratio)
    # 这种写法[x:y]从x到y-1。x不写就是0，y不写就是最后一行
    test_indices = shuffled_indices[:test_set_size] # 从第0行-第test_set_size-1行
    print("test_indices: \n", test_indices)
    train_indices = shuffled_indices[test_set_size:] # 从第test_set_size行到最后一行
    print("train_indices: \n", train_indices)
    # iloc:按下标来索引数据；loc：按标签来索引
    return data.iloc[train_indices], data.iloc[test_indices] 


data = load_housing_data()
data_with_id = data.reset_index()
# print(data_with_id)
data_with_id['id'] = data['longitude'] * 1000 + data['latitude']
# print(data_with_id)
# train_set, test_set = split_train_test(data, 0.2)
# print(len(train_set), "train + ", len(test_set), "test")
train_set, test_set = train_test_split(data, test_size=0.2, random_state=44) # 跟上面的split_train_test方法一样

data["income_cat"] = np.ceil(data["median_income"] / 1.5) # ceil: 向下取整
# where: 第一个参数符合条件的留下，不符合条件的用全部替换成第二个参数的值，如果没有加第二个参数，默认改成NAN。
# 这个意思就是income_cat的值大于5的都改成5
data["income_cat"].where(data["income_cat"] < 5, 5.0, inplace=True)  

''' 
为啥需要分层采样？
在机器学习多分类任务中有时候需要针对类别进行分层采样，比如说类别不均衡的数据，这时候随机采样会造成训练集、验证集、测试集中不同类别的数据比例不一样，
这是会在一定程度上影响分类器的性能的，这时候就需要进行分层采样保证训练集、验证集、测试集中每一个类别的数据比例差不多持平。
'''

# n_splits: 表示训练和测试的组数，1表示训练和测试只有1组。test_size: 测试数据占比20%。random_state：随机44
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=44) 

'''
假设housing["income_cat"]=[1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]也就是5个1，10个2，1所占的比例为1/3，2占的比例为2/3；
则经过split.split(housing, housing["income_cat"])后，strat_train_set [“income_cat”]和strat_test_set[“income_cat”]中1和2，所占的比例相同，分别为1/2，和2/3.
也就是说，strat_train_set [“income_cat”]中有4个1，8个2；而strat_test_set[“income_cat”]中有1个1，2个2
'''
for train_index, test_index in split.split(data, data["income_cat"]): # split: 就是分割
    strat_train_set = data.loc[train_index]
    strat_test_set = data.loc[test_index]

# print(data)
# print(data["income_cat"].value_counts() / len(data))

# 删掉income_cat这一列
for set in (strat_train_set, strat_test_set):
    set.drop(["income_cat"], axis=1, inplace=True)

'''
属性组合实验
'''
# data["rooms_per_household"] = data["total_rooms"]/data["households"]
# data["bedrooms_per_room"] = data["total_bedrooms"]/data["total_rooms"]
# data["population_per_household"]=data["population"]/data["households"]

# 保持干净的训练数据，复制
train_set_copy = strat_train_set.copy()
# print(train_set_copy.head(5))
# 删掉median_house_value这一列
housing = train_set_copy.drop("median_house_value", axis=1)  # drop()创建了一份数据的备份，而不影响train_set_copy。其中这个方法参数的axis表示删除的是这1列，不加这个参数表示删除的行
# print(housing.head(5))
# print(train_set_copy.head(5))  # 的确原来的数据不影响
housing_labels = train_set_copy["median_house_value"].copy()
# print(housing_labels.head(5))

imputer = SimpleImputer(strategy="median")    # 取中位数
housing_num = housing.drop("ocean_proximity", axis=1)  # 删掉这一列，因为这一列为文本不是数值，算不出中位数
# print(housing_num)

imputer.fit(housing_num) # 将imputer实例拟合到训练数据
# print(imputer.statistics_)
X = imputer.transform(housing_num)  # 对训练集进行转换，将缺失值替换为中位数，结果就是普通的numpy数组
# print(X)

housing_tr = pd.DataFrame(X, columns=housing_num.columns) # 又放回到DataFrame里面了

'''
处理文本和类别属性
将本文标签转换为数字
有3种方式实现
'''
housing_cat = housing["ocean_proximity"]
"""
# 方式一 开始
# labelEncoder： 适用的场景，有一列为文本特征值的时候可以；如果有多列文本特征值的时候就要换成factorize()
encoder = LabelEncoder()        
housing_cat_encoded = encoder.fit_transform(housing_cat)
print(encoder.classes_) # 看有哪几种分类

# print(housing_cat_encoded)
# housing_cat_encoded, housing_categories = housing_cat.factorize()
# print(housing_cat_encoded[:10]) # 从0展示到10
# print(housing_cat_encoded)

'''
上面的这种用LableEncoder.fit_transform的做法有问题, ML 算法会认为两个临近的值比两个疏远的值要更相似。显然这样不对（比如，分类 0 和分类 4 就比分类 0 和分类 1 更相似)。
要解决这个问题, 一个常见的方法是给每个分类创建一个二元属性：当分类是<1H OCEAN, 该属性为 1(否则为 0), 当分类是INLAND, 另一个属性等于 1(否则为 0), 
以此类推。这称作独热编码(One-Hot Encoding), 因为只有一个属性会等于 1(热), 其余会是 0(冷)。

这种常见方式，在nlp-beginner-finish项目的task1.data_process.py里面 预处理方法有应用
'''
encoder_one_hot = OneHotEncoder() # 将整数分类值转变为独热向量
# fit_transform()用于 2D 数组，而housing_cat_encoded是一个 1D 数组，所以需要将其变形
# reshap(-1,1), 表示转换成2维数组，只不过是2维1列数组 
# reshap(行, 列) 表示把一维数组转换成x行y列的2维数组。另外在行和列中会出现-1的情况，这个-1表示未指定的，未给定的。
# 只需要特定的行数，列数我无所谓多少，我只需要指定行数，列数用-1代替就行了，计算机帮我算应该有多少列，反之亦然。所以-1在这里应该可以理解为一个正整数通配符，它代替任何正整数。
housing_cat_1hot = encoder_one_hot.fit_transform(housing_cat_encoded.reshape(-1,1)) #这时的输出是一个SciPy稀疏矩阵
'''
SciPy稀疏矩阵的好处：
当类别属性有数千个分类时，这样非常有用。经过独热编码，我们得到了一个有数千列的矩阵，这个矩阵每行只有一个 1，其余都是 0。使用大量内存来存储这些 0 非常浪费，
所以稀疏矩阵只存储非零元素的位置。
'''
print(housing_cat_1hot.toarray()) # 这样就转换成Numpy数组了

#方式一结束

"""

# 方式二 开始
encoder = LabelBinarizer(sparse_output=True)  # 默认是Numpy数组，如果需要变成稀疏矩阵，就要在定义LabelBinarizer时，加一个sparse_output=True 参数就变成稀疏矩阵了
housing_cat_1hot = encoder.fit_transform(housing_cat)
print(housing_cat_1hot)
# 方式二 结束


"""
# 方式三 开始 现在还没有这个方法 网上查了下，只有开发版本里面才有这个
cat_encoder = CategoricalEncoder()
housing_cat_reshaped = housing_cat.values.reshape(-1, 1)
housing_cat_1hot = cat_encoder.fit_transform(housing_cat_reshaped)
print(housing_cat_1hot)
# 方式三 结束
"""
# TODO 后面还有一点，等以后功力深了，看下第二章的结束部分内容就知道什么意思了
