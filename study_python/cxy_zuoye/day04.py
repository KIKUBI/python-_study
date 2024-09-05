# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   RONGHUA
# FileName:      day04.py
# Author:       陈啸宇
# Datetime:     2024/7/31 11:00
# Description:
# ---------------------------------------------------------------------------
#水仙花树
def shuixian(a,b):
    for i in range(a,b):
        if (i//100)**3+(i//10%10)**3+(i%10)**3==i:
            print(i)
shuixian(1,1000)
# 1.写个函数实现：1+2+3+…+n，n在每次调用函数时传入
# 比如 f(5)就计算1+2+3+4+5
def f(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
print(f(5))
#
# 2.实现一个计算器功能，传入两个int及算法（加减乘除），返回计算结果
# 比如 f(1,3,”+”)返回4，f(10,2,”/”)返回5
def jisuan(a,b,c):
    if c=="+":
        return a+b
    elif c=="-":
        return a-b
    elif c=="*":
        return a*b
    elif c=="/":
        return a/b
    else:
        return "输入错误"
print(jisuan(1,3,"+"))
#
# 3.输出100以内所有的素数。（这道题不用写成函数的形式）
# 说明：素数指的是只能被1和自身整除的正整数（不包括1）。比如5只能被1和5整除，5就是一个素数；6可以被1，2，3和6整除，所以6就不是素数。
def sushu(b):
    for i in range(2,b):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
sushu(100)
# 4.写个函数实现：传入两个列表，返回列表中相同的元素和不同的元素
# 比如，传入[1, 2, 3]和[1, 2, 5]，返回：[1, 2]和[3, 5] （可以忽略返回列表中的元素顺序）
def listc(list1,list2):
    list1 = set(list1)
    list2 = set(list2)
    return list1 & list2,list1 ^ list2
print(listc([1, 2, 3],[1, 2, 5]))
# 5.	写个函数输入一个年份，判断是否为闰年？
# 闰年是历法中的名词，分为普通闰年和世纪闰年。1582年以来设置闰年的规则：
# 普通闰年：公历年份是4的倍数，且不是100的倍数的，为闰年（如2004年、2020年
# 等就是闰年）。
# 世纪闰年：公历年份是整百数的，必须是400的倍数才是闰年（如1900年不是闰年，
# 2000年是闰年）。
def runnian(year):
    if year%4==0 and year%100!=0 or year%400==0:
        print('是闰年')
    else:
        print('不是闰年')
runnian(2000)