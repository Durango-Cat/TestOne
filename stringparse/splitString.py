# 字符串截取，从前往后
str='Showme'
# 按照下标返回字符串里面的第一个字符
print('可以按照下标来查找指定索引下的字符', str[0])
# 可以分为从前面索引，也可以分为从后面索引。从前面索引下标是从左到右0~size-1；从后面索引是从右到左-1~-size
# 用的时候，从前面索引可以写在字符串[]中括号里面。如果有后面索引时，就将[]中间加:，将后面索引写在:后面。形式：[:xx]
print('从前面索引和后面索引来截取字符串', str[2:-2]); '''ow'''
# 截取字符串并拼接字符串
print('截取字符串并拼接字符串', str[:-2] + ' time')