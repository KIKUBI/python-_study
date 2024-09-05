# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      data_convert.py
# Author:       lao_zhao
# Datetime:     2024/7/29 14:46
# Description:
# 
# ---------------------------------------------------------------------------

# 浮点数和整形之间的转换
"""
    整形转浮点数：float(整形)
    浮点数转整形：int(浮点数)
"""

# 字符串和数值类型之间的转换
"""
    字符串转整形：int(字符串[, base=进制])
    字符串转浮点数：float(字符串)
    
    整形和浮点数转字符串：str(整形/浮点数)
"""

# 字符串和列表、元组、集合之间的转换
"""
    列表、元组、集合转字符串：str(列表、元组、集合)
        如果：列表、元组、集合的元素类型为字符串，可以使用join将列表、元组、集合中的元素拼接为一个字符串。

    字符串转列表、元组、集合：list(字符串)/tuple(字符串)/set(字符串): 会将字符串中的每个字符串作为列表、元组、集合的每个元素。
"""

# 列表、元组、集合的相互转换
"""
可迭代类型有：字符串、列表、元组、字典(keys、values, items)、集合
    转列表：list(可迭代类型)
    转元组：tuple(可迭代类型)
    转集合：set(可迭代类型)----注意：可迭代类型的元素不能为可变类型(列表、字典、集合)
"""

list1 = [1, 2, 3]
tuple1 = (1, 2, 3, 10000)
set1 = {1, 2, 3, 4, 100}
dict1 = {"name": "tom", "age": 10}

res = set(list1)
print(res, type(res))



"""
str1 = "hello"
list1 = list(str1)
print(list1)

t1 = tuple(str1)
print(t1)

s1 = set(str1)
print(s1)
"""

'''
l1 = ['1', '2', '3', [1, 2]]
t1 = ("a", "B", "c")
s1 = {"1", "2", "3"}
dict1 = {"a": 100, "b": 200}
s_1 = "hello"

str1 = str(l1).strip("[]").replace(", ", "").replace("[", "").replace("]", "").replace("'", "")
print(str1, type(str1))

# str2 = "".join(l1)   # join(可迭代类型)：可迭代类型的每个元素必须为字符串，才能使用join
# print(str2, type(str2))

# str2 = str(t1)
str2 = "".join(t1)
print(str2, type(str2))

# str3 = str(s1)
str3 = "".join(s1)
print(str3, type(str3))

# str4 = str(dict1)
str4 = "".join(dict1)
print(str4, type(str4))

str5 = str(s_1)
print(str5, type(str5))

n = None
str6 = str(n)
print(str6, type(str6))

b1 = True
str7 = str(b1)
print(str7, type(str7))

r = range(10)
str8 = str(r)
print(str8, type(str8))
'''

"""

s1 = "1101"
i1 = int(s1)
print(i1, type(i1))

s2 = "3.14"
f1 = float(s2)
print(f1, type(f1))


i_1 = 1101
f_1 = 3.1231

s_1 = str(i_1)
s_2 = str(f_1)
print(s_1, type(s_1))
print(s_2, type(s_2))
"""

'''
i1 = 10
f1 = 0.1111111111111199

i2 = float(i1)
print(i2, type(i2))

i3 = i1 / 1
print(i3, type(i3))

i_1 = int(f1)
print(i_1)
'''