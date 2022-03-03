import numpy as np
import pandas as pd
import os

# 读取housing下面的csv文件
def load_housing_data():
    pwd_path = os.path.dirname(__file__)
    # print(pwd_path)
    csv_path = os.path.join(pwd_path + "\housing\housing.csv")
    return pd.read_csv(csv_path)


# 将读取到的文件内容，分为80%为训练数据，20%为测试数据
def split_train_test(data, test_ratio):
    # numpy.random.seed()函数可使得随机数具有预见性，即当参数相同时使得每次生成的随机数相同；当参数不同或者无参数时，作用与numpy
    # .random.rand()函数相同，即多次生成随机数且每次生成的随机数都不同。

    # 产生相同的洗牌指数，就是每次执行下面的随机都是一样的随机列表
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
print(data_with_id)
data_with_id['id'] = data['longitude'] * 1000 + data['latitude']
print(data_with_id)
# train_set, test_set = split_train_test(data, 0.2)
# print(len(train_set), "train + ", len(test_set), "test")

