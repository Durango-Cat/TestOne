# 正则表达式：字符串模式（判断字符串是否符合一定的标准）
import re

# 创建模式对象

# 此处的AA是正则表达式，用来验证其他的字符串
pat = re.compile("AA")
# m = pat.search("CDB")
# print(m) # None

# 只会找到第一个AA，第一个匹配到的
# search方法，进行查找比对
# m = pat.search("AVCAAewweAA")
# print(m)

# 没有模式对象的话，前面的字符串是规则（模板），后面的字符串就是需要匹配的字符串
# m = re.search("asd", 'ewdeasd')
# print(m)

# 前面的字符串是规则（模板），后面的字符串就是需要校验的字符串
# print(re.findall("a", "ADSDacdedcasdsdeda")) # ['a', 'a', 'a']
# 查询所有单个的大写字母
# print(re.findall("[A-Z]", "ADSDacdedcasdsdeda")) # ['A', 'D', 'S', 'D']
# 把所有大写连着的字母打印出来
# print(re.findall("[A-Z]+", "asdASASDEdededAEDEFS")) # ['ASASDE', 'AEDEFS']

# sub

# 找到小a用A替换，在第三个字符串中
# print(re.sub("a", "A", "asfreASDSa"))

# 建议在正则表达式中，在被比较的字符串前面加上r 不用担心转义字符的问题，就人为是正常的\
a = r"\adasda-\'"
print(a)
