# range
'''
函数原型：range（start， end， scan):

参数含义：

start:计数从start开始。默认是从0开始。例如range（5）等价于range（0， 5）;

end:技术到end结束，但不包括end.例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5

scan：每次跳跃的间距，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)

因为在for循环中，实际上是根据range的值对i进行了赋值操作，所以不论在for中如何更改i的值，在下一次循环前，i的值都会重新赋值，所以这个循环一共执行5次。
'''
# for循环如果不满足，可以加到else判断逻辑中
# for n in range(2, 10):
#     print("外面的n:", n)
#     for x in range(2, n):
#         print("x:", x, "\t n:", n)
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # 循环中没有找到元素
#         print(n, 'is a prime number')

# 其中的一个现象是：for内部对i进行赋值，其实只在赋值后的内部循环管用，下一次循环不管用
# for i in range(5):
#     print(i)
#     i += 2
#     print(i)
#     print('一轮结束')

# 如果想要内部加完，下次循环还管用的操作，换成while和for都行，就是要把变量定义到外面去
j = 0
while j < 5:
    print(j)
    j += 2
    print(j)
    print('这一轮结束')


