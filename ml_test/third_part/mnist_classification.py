'''
第三章  分类

使用sklearn里面提供的MNIST数据
MNIST 这个数据集，它有着 70000 张规格较小的手写数字图片，从0-9的
'''
import sklearn
from sklearn.datasets import fetch_openml  # 书上写的是mldata，引入找不到，查了下发版是python3.8以下的sklearn版本在0.19版本的时候是支持的，故我又把sklearn从1.0.2降到0.23.2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.base import clone
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import precision_score, recall_score

'''
报错:urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed
原因:Python 2.7.9 之后版本引入了一个新特性:当你urllib.urlopen一个 https 的时候会验证一次 SSL 证书 ，当目标使用的是自签名的证书时就会爆出该错误消息
解决:全局加下面2行代码
'''
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

'''
mac电脑上安装的sklearn时0.23.2不存在这个问题，windows电脑上sklearn是0.24版本，
出现了X[0]报pandas\core\indexes\base.py", line 2900, in get_loc raise KeyError(key) from err
原因：从 Scikit-Learn 0.24 开始，fetch_openml() 默认返回 Pandas DataFrame。
为了避免这种情况并保持与书中相同的代码，我们使用 as_frame=False。
'''
version = sklearn.__version__ < '0.24.0'
if version:
    mnist = fetch_openml('mnist_784')
else :
    # 从原来的fetch_mldata('MNIST original') 改成现在这个样子，sklearn里面的openml是在0.20.0版本开始才支持的。本质都是一样的内容
    mnist = fetch_openml('mnist_784', version=1, as_frame=False) 
# print(mnist)
X, y = mnist["data"], mnist["target"]
# print(X)
# print(X.shape)
# print(y.shape)

# 
if version:
    some_digit = np.array(X.iloc[0])
else :
    some_digit = X[0]
# some_digit_image = some_digit.reshape(28, 28) # 784=28*28
# plt.imshow(some_digit_image, cmap = matplotlib.cm.binary, interpolation="nearest")
# plt.axis("off")
# plt.show() # 3600看到是个9字 0索引时5字
# print(y[0])

X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]
# print(X_train) # X输出的都是二维数值数组，不是字符串
# print("查看下DataFrame y_train的类型：", y_train.dtype) # object
# print(y_train) # 输出：['5' '0' '4' ... '5' '6' '8']
y_train = y_train.astype(np.int8) # 不加这个y_train_5的输出的是[False], 一个值。加上之后输出的是[False True]
# print("查看下DataFrame y_train的类型：", y_train.dtype) # int8
# print(y_train) # 输出：[5 0 4 ... 5 6 8]
y_test = y_test.astype(np.int8)
# print(X_train)
shuffle_index = np.random.permutation(60000) # 将60000个元素打乱顺序
X_train, y_train = X_train[shuffle_index], y_train[shuffle_index] #将训练数据打乱顺序，可以保证交叉验证的每一折里面数据都是类似的

y_train_5 = (y_train == 5) 
# print(y_train_5)
# print(np.unique(y_train_5))
'''
结果数组中应该有多个值。
如果不是，那么可能发生的事情是您使用 fetch_openml() 下载 MNIST，并将标签作为字符串返回，
因此当您定义 y_train_5 = (y_train == 5) 时，它会产生一个充满 False 的数组。
一个解决方案是将 y_train 转换为 int8: y_train = y_train.astype(np.int8) （这是我在笔记本中所做的，就在加载数据之后）。
'''
y_test_5 = (y_test == 5)


'''
二分类
选择 随机梯度下降SGD分类器。这个分类器的好处:能够高效的处理非常大的数据集。原因在于:SGD每次只处理一条数据,适合在线学习。
'''
sgd_clf = SGDClassifier(random_state=42)
sgd_clf.fit(X_train, y_train_5) # 在整个训练集上进行训练 ，fit(X，y) 里面的X训练样本，y是训练样本目标值（类标签）
# x = sgd_clf.predict([some_digit]) # 预测
# print(x) # 输出True

# 交叉验证
'''
交叉验证的基本思想是把在某种意义下将原始数据(dataset)进行分组,一部分做为训练集(train set),
另一部分做为验证集(validation set or test set),首先用训练集对分类器进行训练,再利用验证集来测试训练
得到的模型(model),以此来做为评价分类器的性能指标。

K折交叉验证，初始采样分割成K个大小相等子样本，一个单独的子样本被保留作为验证模型的数据，其他K-1个样本用来训练。
交叉验证重复K次，每个子样本验证一次，平均K次的结果或者使用其它结合方式，最终得到一个单一估测。
这个方法的优势在于，同时重复运用随机产生的子样本进行训练和验证，每次的结果验证一次，10折交叉验证是最常用的。
（我在下面试了下，60000个数据量切成K折，每3份，就会把每折的训练集为40000，测试集20000。这样每一折都有重叠的数据

n_splits:折叠次数，默认为3，至少为2。
shuffle:是否在每次分割之前打乱顺序。
random_state:随机种子，在shuffle==True时使用，默认使用np.random。
'''

# K折交叉验证的方式一

skfolds = StratifiedKFold(n_splits=3, shuffle=True, random_state=42) 
for train_index, test_index in skfolds.split(X_train, y_train_5):
    clone_clf = clone(sgd_clf)
    X_train_folds = X_train[train_index]
    y_train_folds = (y_train_5[train_index])

    X_test_fold = X_train[test_index]
    y_test_fold = (y_train_5[test_index])

    clone_clf.fit(X_train_folds, y_train_folds) # 训练
    x_pred = clone_clf.predict(X_test_fold) # 预测
    # print("train_index.length: ", len(train_index), " test_index.length:", len(test_index), "x_pred: ", x_pred)
    # print("x_pred: ", x_pred)
    value = x_pred == y_test_fold
    # print(value)
    n_correct = sum(value)
    # print(n_correct)
    # print(n_correct / len(x_pred))  # 0.9718  0.9669  0.952  # 计算出被正确预测的数目和输出正确预测的比例

# k = precision_score(y_train_5, y_pred)
# print(k)
# K折交叉验证的方式二, 得到评估分数
# value = cross_val_score(sgd_clf, X_train, y_train_5, cv=3, scoring="accuracy")
# print(value) # [0.95265 0.9641  0.96935]

# K折交叉验证的方式三，得到预测值
y_train_pred = cross_val_predict(sgd_clf, X_train, y_train_5, cv=3)
print(len(y_train_pred)) # 长度都是60000
print(len(y_train_5))    # 长度都是60000
print(recall_score(y_train_5, y_train_pred))  # 召回率 0.7885998893193138

