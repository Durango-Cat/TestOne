# 字典的自测
'''
 可变数据类型 我才可变的数据类型有：列表、字典
 key:value的形式组成了一个item, 字典里面就是由一个个的item元素组成。
 key唯一，如果在创建的时候写了多个一样的key，只会记录最后一次的key和value
 key必须是不可变类型，如字符串、数字、元组，用列表就不行

 根据key访问value，xxx['yyy'] 后面要试试如果key是数字的，还需要用字符吗？

'''
# 数字类型的key,使用[xx]; 字符类型的key使用['xxx']
# d = {'k':1, 2: 'value', 3:4}
# print(d[3])

# items=[('name','superman_cc'),('sex','男')]
# dict1=dict(items)
# print(dict1)

# 删除key对应的值
dict1 = {'key1': 1, "key2": 2, "key3": 3, "key4": 4}
# del(dict1['key1'])
# 把字典打印成字符串
# str1 = str(dict1)
# print(str1, type(str1))

#浅复制，但是我自己试的时候看不出来是浅复制。修改了原字典 不会影响现在的字典
# dict1Copy = dict1.copy()
# dict1['key1'] = "key1Value\n"
# dict1Copy['key1'] = "key1CopyValue\n"
# print("浅复制：", dict1Copy)

# items. 以items方式, key, value变成了一个元组
# dict1Items = dict1.items()
# print(dict1Items)

# dict2以更新的方式放到dict1, 有的值就替换，没有的值就加
# dict2 = {'key1': 'dictation2', 'key5': 5}
# dict1.update(dict2)
# print(dict1)

# 返回字典的所有key 和 value
# print("所有的key集合", dict1.keys())
# print("所有的value集合", dict1.values())

# 塞一个值，如果键存在就不操作。如果键不存在就放 指定的值
# dict1.setdefault('key5', 2)
# dict1.setdefault('key4', 2)
# print(dict1)

# 获取指定键下面的值，键不存在就输出一个默认的值
# print(dict1.get('key5', None))
# print(dict1)
