# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      recursion_limit_demo.py
# Author:       lao_zhao
# Datetime:     2024/8/1 10:49
# Description:
# 
# ---------------------------------------------------------------------------
"""
    递归：函数内调用函数本身，就称为函数的递归。

"""

import sys

# print(sys.getrecursionlimit())   # 查看函数递归的深度
# # 设置函数递归的深度
# sys.setrecursionlimit(10000)
#
# print(sys.getrecursionlimit())



'''
def demo():
    print("函数的递归")
    demo()  # 函数内调用自己本身


demo()
'''
'''
def demo(n):
    print("函数的递归", n)
    n -= 1
    if n == 1:   # 需要定义递归的出口
        return
    demo(n)  # 函数内调用自己本身

demo(5)
'''


def get_sum(n):
    if n == 1:
        return 1
    else:
        return get_sum(n-1) * n


res = get_sum(5)
print(res)


def fibo(month):
    print(f"month的值为：{month}")
    if month == 1 or month == 2:
        return 1
    else:
        return fibo(month-1) + fibo(month-2)


def fibo1(month):
    m1 = m2 = 1
    for i in range(3, month+1):
        m1, m2 = m2, m1 + m2
    return m2



str1 = "上海自来水1来自海上"
print(str1 == str1[::-1])


def func(strs):
    # 判断字符串的长度是否为1或0， 如果是，返回True，就表示是回文字符串
    if len(strs) == 1 or len(strs) == 0:
        return True
    # 判断字符串的第一个字符和最后一个字符是否相等，如果相等，继续调用函数本地对象字符串第二位字符到倒数第二位字符之间的字符做判断
    elif strs[0] == strs[-1]:
        print(f"====={strs[1:-1]}======")
        return func(strs[1:-1])
    # 如果上面的分支都不满足，表示该字符串不为回文字符串
    else:
        return False


print(func(str1))


l1 = [[[[[[[[[[1.1, [[[[[[(1, 2), [[[[[[{1, 2}, [[[[[[[[[100]]]]]]]]], 200]]]]]]]]]]]]]]]]]]]]]]


sum1 = 0
def get_sum(lists):
    # 使用for循环获取列表所有的元素
    for i in lists:
        # 判断列表中的元素是否位整形，如果是，对整形进行累加
        if type(i) == int or type(i) == float:   # 判断数据类型是否整形
            global sum1
            sum1 = sum1 + i
        # 判断i的值是否为列表，如果为列表，调用函数本身进行操作
        # elif type(i) in [list, tuple, set]:   # isinstance(变量, 类型) <==> type(变量) == 类型
        elif isinstance(i, (list, tuple, set)):
            get_sum(i)

get_sum(l1)
print(sum1)


# 全局变量和局部变量
# 函数外定义的变量为全局变量，函数里面定义的变量为局部变量

'''
var = 10
l2 = [1]
def demo():
    res1 = 100
    global var, l2   # 在函数里使用global声明所修改的全局变量
    var = var + 10

    l2.append(100)
    print(var, l2)


demo()
'''
