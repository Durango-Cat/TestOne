import sqlite3

'''
python3已经默认内置进sqlite3
这是一个数据库
'''
# 执行的时候，会去检查当前类所在的路径里面是否有这个test.db，没有就创建一个,
# 有就是打开这个数据库了
#
#
# conn = sqlite3.connect("test.db")
#
# print("成功打开数据库")
# # 获取游标
# c = conn.cursor()
# # 执行sql语句
#
# # 创建数据表
# sql = '''
#     create table company
#         (id int primary key not null,
#          name text not null,
#          age int not null,
#          address char(50),
#          salary real);
# '''
# c.execute(sql)
#
# # 提交数据库操作
# conn.commit()
# # 关闭数据库连接
# conn.close()
# print("成功关闭数据库连接")


# conn = sqlite3.connect("test.db")
#
# print("成功打开数据库")
# # 获取游标
# c = conn.cursor()
# 执行sql语句

# 插入数据
# sql = '''
#    insert into company (id,name,age,address,salary)
#     values (1,'张三',32,"成都",8000);
# '''
# sql2 = '''
#     insert into company (id,name,age,address,salary)
#     values (2,'李四',28,"重庆",10000);
# '''
# c.execute(sql)
# # c.execute(sql2)
#
# # 提交数据库操作
# conn.commit()
# # 关闭数据库连接
# conn.close()
# print("插入数据库")

datalist = [['1', '2', '3',43, 454, 4343], ['4', '5', '6', 3232, 2131, 7686]]
# data = ['1', '2', '3',43, 454, 4343]
for data in datalist:
    # print(data)
# key = "".join(data)
# print(key)
    sql = "insert into movie250 (info_link, pic_link, cname, ename, score, rated, instroduction, info) values("
    for index in range(len(data)):
        data[index] = data[index] if isinstance(data[index], str) else str(data[index])
        # ifstr(data[index])
    print(data)
    sql += ",".join(data) + ");"
    print(sql)