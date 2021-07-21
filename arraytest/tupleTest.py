import operator
# 元组的测试

# 元组不可修改，但是可以把从列表转换成元组的字段，针对这个字段来修改
# 元组中只有一个值的时候，要这种写法(x,)
# oneValue = (1,)
# for one in oneValue: print(one)

# manyValue = (1, 2, 3, 4)
# for many in manyValue: print(many)

# 使用 +、*运算符 可以对元组数据增加
# 使用+会追加
# value1 = (2,)
# value2 = (3,4,5)
# value1 += value2
# print(value1)
# 使用*会数量直接翻倍
# value3 = (3,)
# print(value3 * 4)
# # 多个的话，就是当前的数据重复N次
# value4 = (4,5,6)
# print(value4 * 2)

# 将列表数据转换成元组
# value5 = tuple([7, 8, 're'])
# 这种格式也是不能修改的
# value5[3] = 9
# print(value5)
# 这种格式不能修改
# value6 = (7, 8, 9,)
# print(len(value6))
# value6[3] = 2
# print(value6)
# 这种创建写法也是可以的
# value7 = 4, 5, 7, 8, 9
# print(type(value7)), '''<class 'tuple'>'''

# python3已经没有cmp方法了，可以使用operator模块
value8 = 5, 6,7,77
value9 = 6,7, 77, 5
# print(operator.eq(value8, value9))
# print(operator.eq((6,7, 77, 5), value9))

# 最大最小
# print(min(value9), max(value9))
