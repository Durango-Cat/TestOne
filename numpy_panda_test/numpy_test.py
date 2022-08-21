
import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import tree

X_test = np.arange(0, 5.0, 0.01)[:, np.newaxis]
print(X_test)
# arr = np.arange(12).reshape((3,4))

# print(arr)

# t1 = arr[:, [0, 2]]
# print(t1)

'''
# 这段就是看下meshgrid是干嘛的。 把第一个数组的长度当列，第二个数组的长度当行。xx表示将数组按照第一行往下一直复制第二个数组的长度行数，。
# yy就是将第二个数组转置下，用列一直复制第一个数组的长度的这么多列
points = np.arange(-5, 5, 1)
points1 = np.arange(5, 10, 1)
print(points)
xx, yy = np.meshgrid(points, points1)
print(xx)
print(xx.shape, "-----", yy.shape)
print(yy)
'''

# 仍然使用自带的iris数据
iris = datasets.load_iris()
print(iris.feature_names)
print(iris.discrete_feature_names)
X = iris.data  #后面的方法，就是切片，将原来的多维数组，取出第1列和第三列拼成新的一个数组。总共有150行的数据，
# X = iris.data[:, [0, 2]]  #后面的方法，就是切片，将原来的多维数组，取出第1列和第三列拼成新的一个数组。总共有150行的数据，
# print("X的列名称：", X.target_names)
# print("X: \n", X)
# print(X.shape)
y = iris.target # 这个是目标值，也有150个
print("y: \n", y, y.shape)

clf = tree.DecisionTreeClassifier(max_depth=4)

clf = clf.fit(X, y)
plt.figure(figsize=(15,10))
tree.plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.show()

# x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
# y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
# xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
#                      np.arange(y_min, y_max, 0.1))
# print("xx.shape: ",xx.shape)
# ravel：将数组变为一维的
# np.c_: 将每个数组，转置下当做新数组的每一列加进去。
# 现在这样做的目的 就是变成成左边1个
# xxR = xx.ravel()  # 总长度4424
# print(xxR.shape)
# yyR = yy.ravel()   # 总长度4424
# print(yyR.shape)
# Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
# print(Z)
# print(Z)
# print("Z.reshape before:",Z)  #这是一个一维的
# Z = Z.reshape(xx.shape)
# print("Z.shape:",Z.shape)

# plt.contourf(xx, yy, Z, alpha = 0.5) #说是用来画出不同分类的边界线，可能有些是圆滑的凸函数线条，有些是有棱有角的线段
# plt.scatter(X[:, 0], X[:, 1], c=y, alpha= 0.9)
# plt.show()