'''
函数中的作用域：
局部作用域(Local，L) -> 闭包函数外的函数（Enclosing, E) -> 全局作用域（Global, G) -> 内建作用域（Built-in, B)
L: 最内层，包含局部变量，比如一个函数/方法内部。
E: 包含了非局部(no-local)也非全局(non-global)的变量。比如两个嵌套函数，一个函数（或类）A里面又包含了一个函数B，那么对于B中的名称来说A
    中的作用域就是non-local。
G: 当前脚本的最外层，比如当前模块的全局变量
B: 包含了内建的变量/关键字等，最后被搜索。
'''
a_count = 0
def outer():
    a_count = 1
    def inner():
       a_count = 2
       return print('最里面的', a_count)
    inner()
    return print('次里面的', a_count)
# print(outer()
# print(outer()outer())
print('最外面的', a_count)

# if True:
#     msg = 'I am from Runoob'
#
# print(msg)