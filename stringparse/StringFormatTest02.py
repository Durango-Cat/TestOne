#
# 字符串常用的方法
#

'''
_str = "_"
list = ["I", "Love", "You"]
#语法是 字符串.join(列表）
print(_str.join(list))
'''

# 检测字符串中是否只包含空格，如果有就返回TRUE 反之返回false。通俗的讲就是判断非空验证
'''
str = "the world is true"
strOne = ' '
print(str.isspace())
print(strOne.isspace())
'''

# 检测是否只包含数字或字母。用处：可以用于判断密码，一般情况下密码不能输入汉字或空格
'''
strOne = 'a123'
strTwo = 'a1234 '
print(strOne.isalnum())
print(strTwo.isalnum()) #返回false, 因为包含空格
'''

# isdigit() 检测字符串是否只包含数字，返回true和false
'''
strThree = '123'
strFour = '1231ad'
print(strThree.isdigit())
print(strFour.isdigit())
'''

# isalpha()检测字符串是否只包含字母
# strFive = '123'
# strSix = 'dewdw'
# print(strFive.isalpha())
# print(strSix.isalpha())

print('*'*40)
# 下面开始试下字符串格式化 format方法，这个format里面东西不少
#str1 = "好风凭借力,送我上青云。万般皆在土,各自等时来。".format()

# 不带编号
# str1 = "{}, {}".format("好风凭借力", "送我上青云")


# 带数字编号，可调换顺序。 字符串大括号内可以加上数字，表示后面加数字进来的顺序
# str1 = "城市{1}, 生活{0}".format('干净', '美满')

# site = {'name1': '干净', 'name2': '美满'}
# 针对后面**字典的方式 不知道是什么操作。网上百度了下
# *args
# 不确定往一个函数中传入多少参数，以元组（tuple）或者列表（list）的形式传参数的时候。
#
# **kwargs
# 不确定往函数中传递多少个关键词参数或者传入字典的值作为关键词参数的时候。
#
# 带关键字
#str1 = "城市{name1}, 生活{name2}".format(**site)
# print(str1)

'''
进阶用法
'''
# （1）< （默认）左对齐、> 右对齐、^ 中间对齐、= （只用于数字）在小数点后进行补齐    （2）取位数“{:4s}”、"{:.2f}"等
# 第一个左对齐，第二个右对齐
# print('lalalala{:10s} and {:>10s}lalala'.format('show','me'))
# 小数点保留位数。而且保留小数和位置可以同存
# print('lalala{0:10s} and {1:^10.2f}lalalala'.format('key', 123.5456464))
# % 表示把当前的小数点 变成百分数 小数点向后移2位 并且小数点保留2位，四舍五入
# print('{:.2%}'.format(232.545674))
#
# import datetime
# d = datetime.datetime(2021, 7, 29, 17, 57, 52)
# # y小写的话，就是21，Y就是2021，写全的   h小写就是英文，H大写急救室原值
# print('{:%y-%m-%d %H:%M:%S}'.format(d))

# 多个格式化。
'''

'b' - 二进制。将数字以2为基数进行输出。
'c' - 字符。在打印之前将整数转换成对应的Unicode字符串。
'd' - 十进制整数。将数字以10为基数进行输出。
'o' - 八进制。将数字以8为基数进行输出。
'x' - 十六进制。将数字以16为基数进行输出，9以上的位数用小写字母。
'e' - 幂符号。用科学计数法打印数字。用'e'表示幂。
'g' - 一般格式。将数值以fixed-point格式输出。当数值特别大的时候，用幂形式打印。
'n' - 数字。当值为整数时和'd'相同，值为浮点数时和'g'相同。不同的是它会根据区域设置插入数字分隔符。
'%' - 百分数。将数值乘以100然后以fixed-point('f')格式打印，值后面会有一个百分号。默认是保留6位小数点

'''
# print('{0:b} {0:c} {0:d} {0:o} {0:x} {0:e} {0:g} {0:n} {0:%}'.format(45))

# 这种写法就是 针对多个值，每个都是列表，取列表 和 集合(set) 中的第几位
# g = "i am {0[0]},age{1[1]}, really{1[2]}".format([1,2,3],[11,22,33])
# g = "i am {0[0]},age{1[1]}, really{1[2]}".format((1,2,3),[11,22,33])
# print(g)


