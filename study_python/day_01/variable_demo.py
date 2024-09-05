# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   RONGHUA
# FileName:      variable_demo.py
# Author:       陈啸宇
# Datetime:     2024/7/22 15:38
# Description:
# --------------------------------------------------------------------------
a,b,c = 1,2,3
a,b = b,a
var = 'hello world'
c = a+b+c
list = [1,2,3,4,5,6]
#isnert()方法在指定位置插入元素之前
list.insert(3,55)
print(list)
# 空格占一位
print(a,b,c, var[2:5:2])
if a == b:
    print("a == b")
else:
    print(a,b)
###############################################
f1 = 3.11
f2 = 1.5
#浮点数运算的时候，设置浮点数精确，需要导入decimal模块
from  decimal import Decimal
print(Decimal('3.11') - Decimal('1.5'))
#reverse()方法将列表中的元素反转
list = [1,2,3,4,5,6]
list.reverse()
l1 = list
print('列表',list,l1)
print(list[::-1])
#列表和元素之间的转换
list = ['w','s','d','a','1','1','1']
listd = [1,2,3]
print('列表',list + listd)
list.remove('1')
list [1] = 'q'
print('_'.join(list))
#字符串
str = 'hello world'
str1 = str[3:2:-1] #步长为-1，从后往前取
str2 = str.replace('e','a') #替换字符串中的字符
print('字符串',str2)
#字典
dict2={"名称":"乔峰","年龄":18,"喜欢":["阿朱","阿紫"]}
print(dict2.get("名称"))
disct1 = dict2.pop("年龄") #删除键值对，并返回键值
print(dict2)
#元组
str = 'aaaaffffffssss'
print(''.join(set(str))) #将字符串中的元素去重
print('元组',(set(str)))
#集合
set1={1,5,6,5,1,2,2}
set2={1,6,2,20,50}
list = [1,2,3,10,5,6]
print(set1 & set2) #交集
set1.update(list) #将列表中的元素添加到集合中
print(set1)
#1*2*3*。。。*10
reult = 1
num = 2
while num <= 10:
    reult*=num
    num+=1
    print(reult)
else:
    print(reult)
#for循环实现1+2+3+。。。+10
num = 0
for i in range(1,11):
    num +=i
    print(num)
else:
    print(num)
# 在10中找两个数i和j，满足条件j <= (i / j)时，如果i能除尽j则打印“能除尽”并打印i和j的值，如果不满足则打印“不满足条件”并打印不满足条件的i和j的值
int = 1
for i in range(1,11):
    for j in range(1,11):
        if j <= (i / j) and i % j == 0:
            print("能除尽",i,j)
        else:
            print("不满足条件",i,j)
#求100以内的偶数
for i in range(1,101):
    if i % 2 == 0:
        print('偶数为：',i)
    else:
        print('奇数为:',i)
#求和函数
def sum(a,b):
    result1= 0
    result2 = 0
    for i in range(a,b+1):
        if i % 2 == 0:
            result1 +=i
        else:
            result2 +=i
    print('偶数和为:', result1)
    print('奇数和为:',result2 )
    return
sum(1,10)
#class类，对象      self代表类的初始化本身
from requests import get
class Person(object):
    __weight = 100      #私有属性，只能在类内部使用
    def __init__(self,name,year):
        self.name = name
        self.year = year
        print(self.name,self.year)
    def que(self,path):
        result = get(path)
        rel = result.content.decode('utf-8')
        print(rel)
        return
class Son(Person):                      #Son子类继承了父类Person里的属性和方法
    sum = 0                             #sum,sun类属性，是被类中的所有对象共享的
    sun = 0
    def __init__(self,name,year,sex):  #Son子类继承了父类Person里的属性和方法，但是子类有自己独有的属性
        super().__init__(name,year)    #super()函数是调用父类的一个方法
        self.sex = sex                  #   sex 实例属性是每个实例独有的
        print(self.name,self.year,self.sex)
    def getname(self,a,b,path):
        super().que(path)               #在getname()这个方法函数里调用父类的方法
        for i in range(a,b+1):
            if i % 2 == 0:
                self.sum +=i
            else:
                self.sun+=i
        return self.sum,self.sun
p1 = Person('cxy',22)
p2 = Son('zzz',20,'男')
# print(p1.__weight)                      #私有属性实例对象访问不了
# p2.que('https://www.baidu.com') #调用父类的方法
result = p2.getname(1,10,'https://www.baidu.com')   #被元组接收 元组是有序的，不能被更改的
print('result的数据类型为:',type(result))
print('在1-10中，偶数和为:',result[0],'奇数和为:',result[1])

#列表删除
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listx = []
for i in liste[:]:
    if i % 2 == 0:
        s1 = liste.remove(i)
        listx.append(i)
print(liste,listx)
#闭包
def outer():
    sum = 10
    def inner(a,b):
        return sum + a + b
    return inner
f = outer()         #调用函数，返回值为 inner
print(f(10,20))     #调用inner函数，返回值为40

# 装饰器
def cxys(fn):
    def cxy():
        return fn()
    return cxy
@cxys
def print_name():
    return 'cxyz'
print(print_name())     #调用装饰器函数，返回值为print_name函数的返回值


#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{j}*{i} = {i*j}  ',end='')
    print()
###########################################################################################
import time
print(time.time())
r = time.localtime()
reult1 = time.strftime('%Y-%m-%d %H:%M:%S',r)
reult2 = time.strptime('2022-01-01 00:00:00','%Y-%m-%d %H:%M:%S')
print(reult1,reult2)
###########################################################################################3
with open('./test.txt','r',encoding='utf-8') as res:
    print(res.read())
########################################################################################



