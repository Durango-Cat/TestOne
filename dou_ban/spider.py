# coding=utf-8
# 网页解析，获取数据
from bs4 import BeautifulSoup
# 正则，文字匹配
import re
# 获取网页数据
import urllib.request,urllib.error
# 进行excel操作
import xlwt
# 进行sqlite数据库操作
import sqlite3



def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)
    # askURL(datalist)

    # savepath = '.\\豆瓣电影评分.xls'
    # saveData(datalist, savepath)
    # 换成数据库保存
    dbpath = "movie.db"
    saveData2DB(datalist, dbpath)

# 全局变量，创建正则表达式对象  用单引号的话，里面可以用双引号不会报错。
# 为啥这样就能匹配上，返回的还是一部分内容？因为正则表达式findall存在小括号子式，只返回子式内容
# 影片的详情链接规则
findLink = re.compile(r'<a href="(.*?)">')
# re.S 让换行符包含在字符串内
# 影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)

# 影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')

# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')

# 找到评分人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')

# 找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')

# 找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)

# 1.爬取网页
def getData(baseurl):
    datalist = []
    # 调用获取信息的页面，10次，每次25条
    for i in range(0, 10):
        url = baseurl + str(i*25)
        # 获取到网页源码
        html = askURL(url)
        # 2.解析数据, 使用html解析器
        soup = BeautifulSoup(html, "html.parser")
        # 查找符合要求的字符串，形成列表。找所有div且class还是item的元素
        for item in soup.find_all('div', class_='item'):
            # print(item) # 测试：查看电影item全部信息

            # 保存一部电影的所有信息
            data = []
            item = str(item)
            # print(item)

            # 获取影片的详情链接
            link = re.findall(findLink, item)[0]
            data.append(link)
            # 图片
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)
            # 有的只有一个中文名，没有外文名称
            titles = re.findall(findTitle, item)
            ctitle = titles[0]
            data.append(ctitle)
            if len(titles) == 2:
                otitle = titles[1].replace("/", "")
                data.append(otitle)
            else:
                # 这一列不存在，也要为空，留着，不能列乱了
                data.append(' ')

            # 打分
            rating = re.findall(findRating, item)[0]
            data.append(rating)

            # 评价人数
            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)

            # 概述
            inq = re.findall(findInq, item)
            # 可能没有
            if len(inq) != 0:
                # 去掉句号
                inq = inq[0].replace("。", "")
            else:
                inq = " "
            data.append(inq)

            #
            bd = re.findall(findBd, item)[0]
            # 去掉br
            bd = re.sub('<br(\s+)?/>(\s+)?', ' ', bd)
            # 去掉/
            bd = re.sub('/', ' ', bd)
            # 去掉前后的空格
            data.append(bd.strip())
            # 把处理好的一部电影信息放进去
            datalist.append(data)
            # print(datalist)
            # break
    return datalist

# 得到指定一个URL的网页内容
def askURL(url):
    # 为了伪装用的，告诉浏览器，我们可以接收什么水平的内容
    head = {
        # 模拟浏览器头部信息，向豆瓣服务器发送消息, key一定要对
        "User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 92.0.4515.159 Safari / 537.36"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html
# 3.保存数据
def saveData(datalist, savepath):
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = workbook.add_sheet("豆瓣电影Top250", cell_overwrite_ok=True)
    col = ('电影详情链接', "图片链接", "影片中文名", "影片外国名", "评分", "评价数", "概况", "相关信息")
    for firstRow in range(0, len(col)):
        sheet.write(0, firstRow, col[firstRow])
    for otherRow in range(0, len(datalist)):
        data = datalist[otherRow]
        for cell in range(0, len(data)):
            sheet.write(otherRow+1, cell, data[cell])
    workbook.save(savepath)

def saveData2DB(datalist, dbpath):
    # init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    for data in datalist:
        sql = "insert into movie250 (info_link, pic_link, cname, ename, score, rated, instroduction, info) values ("
        for index in range(len(data)):
            # data[index] = data[index] if isinstance(data[index], str) else ('"' + str(data[index]) + '"')
            data[index] = '"' + data[index] + '"'
        sql +=  ",".join(data) + ")"
        # print(sql)
        cursor.execute(sql)
        conn.commit()
    cursor.close()
    conn.close()
def init_db(dbpath):
    sql = '''
        create table movie250 
        (id integer primary key autoincrement,
         info_link text,
         pic_link text,
         cname varchar,
         ename varchar,
         score numeric,
         rated numeric,
         instroduction text,
         info text
         );
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
# 这就是在下面的内容中调用流程，下面的就是程序入口
if __name__ == "__main__":
# 调用函数
    main()
    print("爬取完毕")