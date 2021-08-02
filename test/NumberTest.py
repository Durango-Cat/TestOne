#import sys; x='runoob'; sys.stdout.write(x+'\n')
'''
import sys
print("命令行参数为：")
for i in sys.argv :
    print(i)
print('\n python 路径为', sys.path)
'''
'''
from sys import argv, path #导入特定的成员
print('path:', path) #因为已经导入path成员，所以此处引用时不需要sys.path
'''
'''

a = b = c = 1
print(a)
a,b,c=1,2,'runoob'
print(a, b, c)
#互相交换值
a,c=c,a
print(a,c)
'''
print(5+4)

# 试下round方法
num = 98.43454523
# 而且round方法都是向下取整
# print(round(num, 2))
# 后面不写的话，就是取整了。
print(round(num))