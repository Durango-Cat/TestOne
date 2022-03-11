"""
sklearn对模型的预测

在这个里面我学着pandas涉及的语法，以及numpy的部分函数用法

在NumPy中，where() 函数可以看作判断表达式的数组版本:
X = where(condition,y,z)
其中condition、y和z都是数组，它的返回值是一个形状与 condition相同的数组。当condition中的某
个元素为True时，x中对应下标的值从数组y获取，否则从数组z获取。
如果y和z是单个数值或者它们的形状与condition的不同，将先通过广播运算使其形状一致。

pandas里面的iloc 和 loc的区别：
loc就根据这个index来索引对应的行。
iloc是根据行号来索引，行号从0开始，逐次加1。
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
import os
# 加载数据
pwd_path = os.path.dirname(__file__) + "/"
oecd_bli = pd.read_csv(pwd_path + "oecd_bli_2015.csv", thousands=',')

gdp_per_capita = pd.read_csv(pwd_path + "gdp_per_capita.csv",thousands=',',delimiter='\t', encoding='latin1', na_values="n/a")

# 清洗数据
def prepare_country_stats(oecd_bli, gdp_per_capita):
    # 提取出 INEQUALITY 字段为 'TOT' 的数据
    p = oecd_bli['INEQUALITY'] == 'TOT'
    oecd_bli = oecd_bli[p]
    # 转换为以国家为索引，每行是由Indicator列的数据在这个国家上分组， values就是用那个列表里面的这一列数值能匹配到的第一个返回
    oecd_bli = oecd_bli.pivot(index='Country', columns='Indicator', values='Value')
    # print(oecd_bli.head(3))
    gdp_per_capita.rename(columns={'2015': 'GDP per capita'}, inplace=True)
    gdp_per_capita.set_index('Country', inplace=True)
    # print(gdp_per_capita.head(3))
    full_country_stats = pd.merge(left=oecd_bli, left_index=True, right=gdp_per_capita, right_index=True)
    full_country_stats.sort_values(by='GDP per capita', inplace=True)
    # print(full_country_stats.head(3))
    # print(full_country_stats[['GDP per capita', 'Life satisfaction']])
    # print(full_country_stats[['GDP per capita', 'Life satisfaction']].loc['United States'])  # 这是是取美国里面 按照GDP 和 Life两个维度分组的数据
    remove_indices = [0, 1, 6, 8, 33, 34, 35]
    keep_indices = list(set(range(36)) - set(remove_indices))

    return full_country_stats[['GDP per capita', 'Life satisfaction']].iloc[keep_indices]


# 准备数据
country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)
# np.r_是按列连接两个矩阵, 要求列数相等， 如果只是一组数据的话，就会拼成列向量
# np.c_是按行连接两个矩阵, 要求行数相等， 如果只是一组数据的话，就会拼成行向量
X = np.c_[country_stats["GDP per capita"]]
y = np.c_[country_stats["Life satisfaction"]]
# print("X: ", X)
# print("y: ", y)

# 可视化数据
# 设置打印格式 (kind: 图表类型, x: x轴文字, y: y轴文字, figsize: 图表尺寸)
# country_stats.plot(kind='scatter', x="GDP per capita", y='Life satisfaction', figsize=(5, 3))
# plt.show() # 手动关闭，还可以继续执行接下来的代码逻辑

# 选择线性模型
#lin_reg_model = LinearRegression()   # LinearRegression()是一个预测器
lin_reg_model = KNeighborsRegressor(n_neighbors=3)

# 训练模型
lin_reg_model.fit(X, y)

# 对塞浦路斯进行预测
X_new = [[22587]]  # 塞浦路斯的人均 GDP
print(lin_reg_model.predict(X_new)) # outputs [[ 5.96242338]]  # predict():用新实例的数据集做出相应的预测

