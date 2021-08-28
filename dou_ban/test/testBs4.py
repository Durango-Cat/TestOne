'''
BeautifulSoup4将复杂HTML文档转换成一个复杂的树形结构，每个节点都是Python对象，
所有对象可归纳为4种：
    -Tag：标签及其内容，只能拿到它所找到的第一个内容
    -NavigableString: 标签里面的内容
    -BeautifulSoup: html所有内容
    -Comment：是一个特殊的NavigableString，输出的内容不包含注释符号
'''
import re

from bs4 import BeautifulSoup

# 二进制读取
file = open("./baidu.html", "rb")
html = file.read().decode("utf-8")
# 解析文档
bs = BeautifulSoup(html, "html.parser")
# print(bs.title)
# 找到第一个匹配的标签里面的所有内容
# print(bs.a)
# print(type(bs.head)) # <class 'bs4.element.Tag'>

# 打印标签里面的所有内容
# print(bs.title.string)
# print(type(bs.title.string))  #<class 'bs4.element.NavigableString'>

# 提取标签里面的所有键和值, 闹到一个标签里面的所有属性, 返回格式以字典的方式
# print(bs.a.attrs)

# 如果第一个是注释掉的，会显示注释掉的标签里面的内容。类型是Commit，如果第一个a标签不是注释掉的，那就
# 是NavigableString类型

# print(bs.a.string)
# print(type(bs.a.string))

# -----------------------------------------
# 文档的遍历

# tag的.content属性可以将tag的子节点以列表的方式输出
# print(bs.head.contents)
# 用列表索引来获取它的某一个元素
# print(bs.head.contents[1])



# 文档的搜索
# （1）find_all()，以列表的形式返回
# 字符串过滤：会查找与字符串完全匹配的内容
# print(bs.find_all("a"))

import re
# （2）正则表达式搜索：使用search（）方法来匹配内容
# 下面的这个就是标签和标签的内容里面含有a
# print(bs.find_all(re.compile("a")))

# （3）方法：传入一个函数（方法），根据函数的要求来搜索
# 需要搜索标签里面有name属性的 标签和标签内容
# def name_is_exist(tag):
#     return tag.has_attr("name")
#
# t_list = bs.find_all(name_is_exist)
# print(t_list)


# （4）kwargs 关键字参数
# t_list = bs.find_all(id="head")
# 包含在标签和标签里面的所有内容
# t_list = bs.find_all(class_=True)
# for item in t_list:
#     print(item)

# （5）text参数:文本
# t_list = bs.find_all(text="hao123")
# t_list = bs.find_all(text=["hao123", "地图"])
# 应用正则表达式来查找包含特定文本的内容（标签里面的字符串）
# t_list = bs.find_all(text=re.compile("\d"))
# print(t_list)

# （6） limit参数：限制多个输出的个数
# t_list = bs.find_all("a", limit=3)
# print(t_list)

# css选择器
# .类名  #id
# t_list = bs.select("#u1")
# print(t_list)
# print(bs.select(".mnav"))

# print(bs.select("a[class='bri']"))

# print(bs.select("head > title"))
# 兄弟节点
# print(bs.select(".mnav ~ .bri"))
# 想要第一个元素里面的文本，即标签里面的内容
print(bs.select(".mnav ~ .bri")[0].get_text())