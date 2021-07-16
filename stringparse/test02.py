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


