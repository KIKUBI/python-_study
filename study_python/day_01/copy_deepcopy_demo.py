# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      copy_deepcopy_demo.py
# Author:       lao_zhao
# Datetime:     2024/8/6 11:01
# Description:
# 
# ---------------------------------------------------------------------------


# 对象,引用
# 变量是没有对象，值数据/值才拥有对象(类型)
# 一个变量等于某个值时，表示这个变量在引用这值(对象/类型)内存地址
i = 10
print(id(i))

i = "abc"

# 值相等，内存地址不相同
i1 = "成都"
i2 = "成都"
print(id(i1))
print(id(i2))

# 共享引用：多个变量同时共享一个类型/值/对象的内存地址。
a = b = c = "成都"
print(id(a))
print(id(b))
print(id(c))
a = "hello 成都"
print(a, b, c)

# 共享引用中的注意
a1 = b1 = c1 = [1, 2, 3]
a1.append(100)
print(a1)
print(b1)
print(c1)
print("-"*100)

# 浅拷贝：如果多个变量共享引用的数据类型为列表、字典、集合(列表、字典没有嵌套可变类型数据)时，如果其中一个变量的值发送改变其他的也会随之发送改变。
#        可以使用列表(切片也是复制的动作)、字典、集合的copy方法(copy模块中的copy函数)对列表、字典、集合进行复制，对复制之后的列表、字典、集合进行操作，不会改变原来的数据，
#        copy方法的行为称为浅拷贝。

# list
a1 = b1 = c1 = [1, 2, 3]
a1 = a1[:]   # 切片的操作就是复制的操作
a1.append(100)
print(a1)
print(b1)
print(c1)

# dict
a2 = b2 = c2 = {"name": "tom", "age": 18}
a2 = a2.copy()   # copy复制
a2["name"] = "王老五"
print(a2)
print(b2)
print(c2)

# set
a3 = b3 = c3 = {1, 2, 3}
a3 = a3.copy()
a3.discard(1)

print(a3)
print(b3)
print(c3)
print("-"*100)

import copy
# 深拷贝：如果多个变量共享引用的数据类型为列表、字典、元组时，并且列表、字典、元组中嵌套了可变类型数据，如果其中一个变量的值发送改变可以使用浅拷贝进行复制。
#        如果是嵌套的可变类型的数据发生改变，即使使用浅拷贝嵌套的可变类型数据所有变量的值都会发生改变，这时可以使用copy模块中的deepcopy进行深拷贝。
x = y = z = [1, 2, [3, 4, [100]]]
x = copy.deepcopy(x)  # 深拷贝
x[-1][-1].append("成都")

print(x)
print(y)
print(z)


x1 = y1 = z1 = {"data": [1, 2, 3]}
# x1 = x1.copy()
x1 = copy.deepcopy(x1)
x1["data"].append(100)
print(x1)
print(y1)
print(z1)


x2 = y2 = z2 = (1, 2, [3, 4, [100]])
# x2 = copy.copy(x2)
x2 = copy.deepcopy(x2)
x2[-1].append("hello")
print(x2)
print(y2)
print(z2)