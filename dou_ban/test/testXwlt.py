import xlwt

'''
写内容到xlsx文件
'''
# 创建workbook对象
workbook = xlwt.Workbook(encoding="utf-8")
#
worksheet = workbook.add_sheet('sheet1')
# 写入数据，第一个参数就是'第一行', 第二个参数就是'第二行'

# 写个99乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        # value = str(i) + "*" + str(j)
        # worksheet.write(i-1, j-1, value)
        # 用format输出
        worksheet.write(i-1, j-1, "{0:d} * {1:d} = {2:d}".format(i, j, i * j))
# worksheet.write(0, 0, 'hello')
# 保存数据到xlsx中
workbook.save('student.xls')
