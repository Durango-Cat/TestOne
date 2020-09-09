#正则的测试  re模块就是正则表达式
import re
#将正则表达式字符串编译成正则re对象
p = re.compile("abc")
print(p.search("zabct"))
#也可以在一行表示，在目标字符串中匹配正则表达式
print(re.search('bcd', 'you bcd'))

#compile还可以添加些标志位，比如re.I(re.IGNORECASE) 忽略大小写
p = re.compile('abc')
print(p.search('xAbCy'))
p = re.compile('abc', re.I)
print(p.search('xAbCw'))

#match() 从目标字符串第一个字符开始匹配正则表达
print()
p = re.compile('abc')
print(p.search('xxxabcyyyy'))

print(p.match('xxxabcyyyy'))

print(p.match('abcyyyy'))

print()
#返回目标字符串中匹配正则表达式中所有子串列表
p = re.compile('^([a-z]{2}):([1-9]{3}):(.+)$')
#上面字符串是由3个括弧括起来的，分别是'[a-z]{2}'、'[1-9]{3}'、'.+'  分别要被下面的字符串里面用2个：拼接起来的字符串
print(p.findall('as:123:a12'))