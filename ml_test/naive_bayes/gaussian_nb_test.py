'''
如果样本特征大部分是连续的，使用高斯分布
'''
import numpy as np
from sklearn.naive_bayes import GaussianNB

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
# 拟合数据
clf = GaussianNB()

clf.fit(X, Y)

print("==Predict result by predict==")
print(clf.predict([[-0.8, -1]]))

print("==Predict result by predict_proba==")
p = clf.predict_proba([[-0.8, -1]])
print(eval(lambda x: '%f' % x， p[0][0]), str(eval(p[0][1])))

print("==Predict result by predict_log_proba==")
print(clf.predict_log_proba([[-0.8, -1]]))
