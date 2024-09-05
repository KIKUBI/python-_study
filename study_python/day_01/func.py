# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      func.py
# Author:       lao_zhao
# Datetime:     2024/7/31 14:02
# Description:
# 
# ---------------------------------------------------------------------------
"""
    列表推导式：[变量 for 变量 in 可迭代类型]
    集合推导式：{变量 for 变量 in 可迭代类型}
    字典推导式：{key: value for key in 可迭代类型}
    生成器推导式：(变量 for 变量 in 可迭代类型)

"""

list1 = [i for i in range(1, 10)]
print(list1)

set1 = {i for i in range(1, 11)}
print(set1)

str1 = "hello"
data = [[1, 2, 10], [3, 4, 20], [5, 6, 30]]   # 二维列表
data1 = [[1, 2], [3, 4], [5, 6], 100]   # 一维列表
dict1 = {key: str1.count(key) for key in str1}
print(dict1)

for i, j, k in data:
    print(i, j, k)


generator = (i for i in range(10))
print(generator, type(generator))
for i in generator:
    print(i)

lists = {}
for i in range(10):
    lists[i] = i+1

print(lists)