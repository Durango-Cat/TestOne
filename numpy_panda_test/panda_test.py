import pandas as pd

ser = pd.Series([5, 0, 3, 8, 4], index=['blue', 'red', 'yellow', 'white', 'green'])

print(ser, '\n')
#rank() 把对象的value替换为数值等级
# （相应的名次，如果没有重复的就是相应的升序名次。
# 如果有重复的 那对重复的这n个元素就是把应该的下标变成（3+4+... +n)/n=average就是本来应该重复的n个值，现在都是average）
# 左边index的顺序不变，右边的值按照升序，从0开始的顺序，每个index在升序中的位置是多少后面就是啥值
print(ser.rank(), '\n')
# 左边不变，右边是按照降序, 这个参数的意思就是不要升序了，默认是升序True
print(ser.rank(ascending=False))