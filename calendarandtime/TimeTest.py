#Time模块
import time
t = time.localtime()
#输出本地时间
#print(time.asctime(t))
#跟上面的这个方法一样都是返回星期 月日 时分秒 年
#print(time.ctime())
#系统运行时间
#print(time.perf_counter())
#推迟调用线程的运行，里面填写的是秒数
#time.sleep(20)
#进程运行时间
#print(time.process_time())
#格式化日期
#格式化 年-月-日 时-分-秒
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#格式化 周 月 日 时：分：秒 年 的形式
print(time.strftime("%a %b %c %H:%M:%S %Y", time.localtime()))
#周 月 日
print(time.strftime("%a %b %c", time.localtime()))