# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      generator_demo.py
# Author:       lao_zhao
# Datetime:     2024/8/1 16:39
# Description:
# 生成器
# ---------------------------------------------------------------------------
from collections.abc import Iterator, Iterable

"""
    生成器：一个函数使用yield返回值，这个函数就是一个生成器。

"""
"""
    生成器的本质是一个迭代器。
    生成器和迭代器的区别：生成器会自己生成器元素，迭代器取的是可迭代类型的元素。
"""
# yield的功能：
"""
    1: 返回值，返回值之后不结束函数。
    2：yield返回值值之后，会让函数挂起(暂停。)，
        第一次生成器使用__next__()取值时，直接获取生成器函数中的第一个yield的返回值，会让生成器函数挂起，
        再次使用yield使用__next__()魔法方法取值时，会找生成器函数yield挂起的位置，向下找下一个yield的返回值
    3：生成器可以挂起的位置接收值
        可以使用生成器的send方法向生成器函数挂起的位置发送值,再接收下一个yield的返回值。
"""


'''
def demo():
    print("第一次返回")
    i = yield 1
    yield i.upper()
    print("第三次返回")
    yield 3
    print("第四次返回")

d = demo()
print(d, type(d))

print(next(d))
res = d.send("hello")
print("=================", res)

# print("=================", next(d))
'''


# print(isinstance(d, Iterator))
# print(isinstance(d, Iterable))

# print(d.__next__())
# print(d.__next__())
# print(d.__next__())
# print(d.__next__())

'''
str1 = "Abc"
str1_iterator = str1.__iter__().__iter__()

for i in str1_iterator:
    print(i)

for j in d:
    print(j)
'''


def demo1():
    for i in range(10):
        var = yield i
        if var == "q":
            break


d = demo1()

# for j in d:
#     print(j)

print(next(d))

print(d.send("q"))


# g1 = (i for i in range(10))
# print(g1, type(g1))
#
# print(g1.__next__())
# print(g1.__next__())
# print(g1.__next__())
# print(g1.__next__())
# print(g1.__next__())


def demo3():
    yield 1
    yield 2
    yield 3


print(demo3().__next__())
print(demo3().__next__())
print(demo3().__next__())
print(demo3().__next__())