import urllib.request
import urllib.parse
'''
# 获取get请求
response = urllib.request.urlopen("http://www.baidu.com")
# 读取response里面的内容, 用utf-8解码， 这样就会把换行符和中文正确的解释
print(response.read().decode('utf-8'))
# 建议把返回过来的内容，用utf-8进行解码
'''
'''
# 获取post请求 可以用httpbin.org
# 解析器

# 将里面的内容转换成二进制，里面可以用字典的方式，再用parse解析下
data = bytes(urllib.parse.urlencode({"hello":"world"}), encoding="utf-8")
response = urllib.request.urlopen("http://httpbin.org/post", data=data)
print(response.read().decode("utf-8"))
'''

'''
# 超时处理，进行处理
try:
# 设置超时
    response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)
    print(response.read().decode("utf-8"))
except urllib.error.URLError as e:
    print("time out")
'''
'''
# 把拿到的内容做简单的解析
response = urllib.request.urlopen("http://www.baidu.com")
# print(response.status)
# 能把请求过程中的所有信息都获取到，请求头，返回结果，返回状态码什么的
print(response.getheaders())
'''
'''
# 将防爬虫的网页 中 headers里面的信息包装下再发请求
# 要模拟浏览器里面的所有headers信息，把所有的header信息都放进来
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}
url = "http://httpbin.org/post"
data = bytes(urllib.parse.urlencode({"name":"eric"}), encoding="utf-8")
req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
'''

#豆瓣不允许非浏览器的这种形式访问，就可以直接在headers里面模拟一个浏览器，就可以访问
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}
url = "http://www.douban.com"
req = urllib.request.Request(url=url, headers=headers)
# 塞一个request对象去访问
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))