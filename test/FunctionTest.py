'''
方法的测试
'''
# *args :可变参数
def avgs(*args):
    if len(args) == 0:
        return 0
    else:
        sum = 0
        for x in args:
            sum += x
        # 求平均后，转换成整数
        # 转换成整数int(xxx), 转换成浮点型float(xxx), 转换成字符str(xxx)
        return int(sum/len(args))

# print(avgs(1,2,3,4,5))
# 不加参数表示 没有参数，取的也是0
print(avgs())