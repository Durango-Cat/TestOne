import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split        # 跟下面实现的split_train_test方法一样。
from sklearn.model_selection import StratifiedShuffleSplit  # 分层采样

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


