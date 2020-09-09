#数字组合
#题目：有4个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
a=b=c=1
total=0
while a <= 4:
    while b <= 4:
        while c <=4:
            if a!=b and b!=c and a!=c:
                print(a,b,c)
                total+=1
            c+=1
        b+=1
    a+=1
print(total)
