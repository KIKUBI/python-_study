# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      iterable_iterator_generator.py
# Author:       lao_zhao
# Datetime:     2024/8/1 15:20
# Description:
# 
# ---------------------------------------------------------------------------
from collections.abc import Iterable, Iterator

# 迭代：iteration
"""
    可迭代类型-iterable：可迭代类型必须有__iter__()魔法方法。
    迭代器-iterator：迭代器是可迭代类型使用__iter__()魔法方法/iter()函数创建的迭代器，迭代器的功能：每次迭代，迭代器是用来取可迭代类型的元素的。
                迭代器使用__next__()魔法方法/next()函数取可迭代类型的元素。__next__()魔法方法/next()每次取元素只向前取，不会向后取。
                
                注意：迭代器即是一个迭代器也是一个可迭代类型。
                     迭代器本身是没有任何元素的。

"""
"""
    for循环的底层原理：for 变量 in 可迭代类型，for循环的开始可迭代类型使用__iter__()魔法方法创建迭代器，for每次循环会使用迭代器的
                    __next__()魔法方法取可迭代类型的元素，如果可迭代类型的元素去完，还使用__next__()魔法方法取元素，就会报StopIteration的错误。
                    for循环底层再捕获StopIteration的错误，for循环只要捕获到StopIteration的错误，for循环就结束。
"""
"""
    __iter__()/iter()的功能：可迭代类型使用__iter__()魔法方法创建迭代器。
"""


'''
s1 = "Abc"
print(isinstance(s1, Iterable))  # 判断数据是否为某一个对象/类型
# print(type(s1) == Iterable)  # 明确判断数据是否为哪一种数据类型

s_iterator = s1.__iter__()
print(s_iterator, type(s_iterator))

list1 = [1, 2, 3]
print(isinstance(list1, Iterable))
l_iterator = list1.__iter__()
print(l_iterator, type(l_iterator))

t1 = (1, 2, 3)
print(isinstance(t1, Iterable))
t_iterator = t1.__iter__()
print(t_iterator, type(t_iterator))

set1 = {1, 2, 3}
print(isinstance(set1, Iterable))
s1_iterator = set1.__iter__()
print(s1_iterator, type(s1_iterator))

dict1 = {"name": "张三", "age": 18}
print(isinstance(dict1, Iterable))
d_iterator = dict1.items().__iter__()
print(d_iterator, type(d_iterator))

r = range(10)
print(isinstance(r, Iterable))
# r_iterator = r.__iter__()
r_iterator = iter(r)
print(r_iterator, type(r_iterator))
'''

str1 = range(3)
str1_iterator = str1.__iter__()

print(str1_iterator.__next__())
print(str1_iterator.__next__())
print(str1_iterator.__next__())
print(str1_iterator.__next__())  # StopIteration

'''
print(next(str1_iterator))

print(isinstance(str1_iterator, Iterable))
print(isinstance(str1_iterator, Iterator))

print(isinstance(str1, Iterable))
print(isinstance(str1, Iterator))
'''