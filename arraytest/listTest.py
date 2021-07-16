# 列表的测试
# 列表截取的时候可以像字符串一样，list[前:后]
# 列表里面可以存储不同类型的字段。python里面数值有2种类型：int,float
lists = ['Show', 'me', 12, 32, 45]
# 从后往前是不包含的
# print('看下截取下标1到从后往前2个的元素列表', list[1:-2])
# list1 = ['sss', 888]
# print('看列表的拼接', list + list1)

# 更新列表
# list[2] = 'rrr'
# print('查看下list的第三个元素', list[2])

# 删除最后一个元素
# del(list[4])
# print('看下删除后的list信息', list)

# 嵌套列表
# sub1 = [0, 1, 2, 3]; sub2 = [7, 8, 9, 0]
# list2 = [sub1, sub2]
# print('查看下list2的嵌套列表信息', list2)
# 继续看下嵌套列表中的下标数组中的第一个元素
# print('看嵌套列表中第一个数组中的第一个元素', list2[1][2])

# 列表的其他常用方法
# list.append(33)
# print('往最后一个元素后面追加元素', list)

# 查看列表中某个元素出现的次数，我想看看是不是一个字符在某一个数值下出现了好几次也算进去
#试了下不是，而且去根据传进去的字符去匹配每一条值，看值是否有符合的。相当于遍历的过程中用equals算数量
# list3 = ['elephant', 'panada', 'giraffe']
# print(list3.count('panad'))

# 追加另一个集合。这种是啥，等于追加之后把集合，放在最后一个元素后面了。
# appendList = ['a1', 'a2', 'a3']; '''['Show', 'me', 12, 32, 45, ['a1', 'a2', 'a3']]'''
# list.append(appendList)
# print(list)

# 根据元素找出在列表中的索引位置。这个下标位置是从0开始算的。
# print(list.index(32))
# 删除指定索引下的元素，不填就是最后一位
# print(list.pop(-2))

# 数组复制，深度克隆，改原数组
# listCopy = list.copy()
# list[3] = 4444
# print(listCopy, list)

# 反转列表
# listReverse = list(reversed(lists))
# print(listReverse)

# 排序的話，要求列表中數據的類型要一致。
lists = [12,55,78,1,4,66]
# listSort = sorted(lists)
# print(listSort)