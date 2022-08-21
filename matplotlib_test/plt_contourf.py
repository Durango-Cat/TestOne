from xml.sax.xmlreader import Locator
import numpy as np #这个写法是使用numpy时，可以以np开头
import matplotlib.pyplot as plt
from numpy import ma  #这个写法是导入Numpy的ma库函数，ma模块是支持数组中包含掩码元素（包含缺失值或者异常值）
from matplotlib import ticker, cm

N = 7
x = np.linspace(-6.0, 6.0, N)
y = np.linspace(-7.0, 7.0, N)

X, Y = np.meshgrid(x, y)
print("X: ", X)
print("Y:", Y)
Z1 = np.exp(X*Y)
z = 50 * Z1
z[:5, :5] = -1
z = ma.masked_where(z <= 0, z)
print("z:",z)

# 按照我对这个方法这几个参数尤其是X,Y，z的理解
# X,Y负责表格的x轴和y轴。z表示的在这个坐标轴里面的值，就是X,Y上面的每个点的值，通过Z来反映，Z大或者小在这个图里右边有个Z取值范围
# cs = plt.contourf(X, Y, z, locator= ticker.LogLocator(), cmap="bone") #其中X,Y的值是可以不填的，不填就认为坐标轴从0开始
cs = plt.contourf(z, locator= ticker.LogLocator(), cmap="bone")
cbar = plt.colorbar(cs)

plt.show()