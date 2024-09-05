# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      for_demo.py
# Author:       lao_zhao
# Datetime:     2024/7/30 15:23
# Description:
# 
# ---------------------------------------------------------------------------

"""
    for循环：python中的for循环，循环的是可迭代类型的元素，每次循环取出可迭代类型的一个元素。
        注意：元素只能向前取，不能向后取。

"""
# 格式：
"""
for 变量 in 可迭代类型：
    循环体代码
"""
# 可迭代类型：字符串，列表，元组，字典，集合，range序列. __iter__()
str1 = "hello"
list1 = [1, 2, 3, "hello", "python"]
tuple1 = (100, 200, 300, "hello", "python")
dict1 = {"a": 100, "b": 200}
set1 = (1, 2, 3, 4, 100, "hello")
for i in set1:
    print(i)

for i in range(len(str1)):   # range(10) == range(0, length, 1)
    if i == 2:
        break
    print(i)
else:
    print("else代码块")

print("-"*100)
for i in range(1, 11):
    if i % 2 == 1:
        print("="*i)


# for i in range(1, 9):
#     for j in range()


print("-"*100)
row = 4
for i in range(1, row+1):  # 空行数
    # 控制每行的输出内容
    # 空格的规律
    for _ in range(row-1, i - 1, -1):  # range(开始值, 结束值, 步长)
        print("=", end="")

    # 星号的规律
    for _ in range(1, 2 * i):
        print("*", end="")

    print()

print("-"*100)
row = 13
for i in range(1, row+1):  # 空行数
    # 控制每行的输出内容
    # 空格的规律
    for _ in range(row-1, i - 1, -1):  # range(开始值, 结束值, 步长)
        print("=", end="")

    # 星号的规律
    for k in range(1, 2 * i):
        # 控制什么时候输出*号
        if k == 1 or k == 2*i-1:
            print("*", end="")
        else:
            print(" ", end="")

    print()

print("-"*100)
row = 21
for i in range(1, row+1):  # 空行数
    # 控制每行的输出内容
    # 空格的规律
    for _ in range(row-1, i - 1, -1):  # range(开始值, 结束值, 步长)
        print(" ", end="")

    # 星号的规律
    for k in range(1, 2 * i):
        # 控制什么时候输出*号
        if i == 1:
            continue
        elif i % 2 == 1:
            print("*", end="")
        else:
            if i == 2:
                continue
            elif k == 1 or k == 2*i-1:
                print("*", end="")
            else:
                print(" ", end="")

    print()

print("-"*100)
row = 21
for i in range(3, row+1):  # 空行数
    # 控制每行的输出内容
    # 空格的规律
    for _ in range(row-1, i - 1, -1):  # range(开始值, 结束值, 步长)
        print(" ", end="")

    # 星号的规律
    for k in range(1, 2 * i):
        # 控制什么时候输出*号
        if i % 2 == 1:
            print("*", end="")
        else:
            if k == 1 or k == 2*i-1:
                print("*", end="")
            else:
                print(" ", end="")

    print()
