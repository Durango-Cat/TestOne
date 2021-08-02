'''
    yield 关键字的用法


'''

def foo(num):
    print("starting...")
    while num<10:
        yield num
        num=num+1
for n in foo(0):
    print(n)