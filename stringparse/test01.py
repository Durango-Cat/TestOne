# 常用字符串内置函数
str = 'Tell me the world is true'
# 返回该字符串中某个子串出现的次数
print('返回该字符串中o出现的次数', str.count("o"))
# 返回某个子串出现在该字符串的起始位置 检测字符串是否包含。如果不包含返回-1
print(str.find("ell"))
# 跟上一个功能一样，都是检测字符串是否包含，返回开始的索引值。如果不包含就直接报错了
# str.index("0")
# 转小写
print(str.lower())
# 转大写
print('转正大写', str.upper())
# 分割字符串，默认以空格分割
print(str.split())
# 字符串的长度，从0开始，比如11位长度的就是10
print(len(str))
# 转成整型
num = "323432.323"
# int强转整型的话，如果是字符串就必须不带小数点，不是字符串的数值类型可以支持包含小数点
print(int(323432.323))
# 转成浮点型
print(float(num))
