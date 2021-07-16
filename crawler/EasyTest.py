import requests
from bs4 import BeautifulSoup
# import lxml
'''
r = requests.get('http://www.jianshu.com/')
print(r.encoding)
'''

# 要抓取的目标页码地址
url = 'http://www.ranzhi.org/book/ranzhi/about-ranzhi-4.html'

# 抓取页码内容，返回响应对象
response = requests.get(url)

# 查看响应状态码
status_code = response.status_code

# 使用BeautifulSoup解析代码，并锁定页码指定标签内容
decodeValue = response.content.decode("utf-8")
# print(decodeValue)
content = BeautifulSoup(decodeValue, 'lxml')
# 虽然这块的id会爆红 但是 不影响使用，all里面的内容就是整个抓下来的标签里面的某一个精确的内容
element = content.find_all(id="book")
print(element)
print(status_code)
#print(element)