# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      set_demo.py
# Author:       lao_zhao
# Datetime:     2024/7/29 10:08
# Description:
# 
# ---------------------------------------------------------------------------


"""
    集合：一组唯一元素的组合。集合中的元素只能为不可变类型(整形，浮点数，字符串，元组)。
        注意：集合的元素不能为：列表、字典、集合

    声明：
        变量 = set(): 声明空集合
        变量 = {元素,...}: 声明一个非空集合
"""
"""
    集合的特点：
        1：集合中的元素是无序
        2：集合中的元素唯一: 可以对字符串中的字符、列表和元组中的元素去重(列表和元组中的元素不能为可变类型)
"""
"""
    操作:
        运算：
            &(交集)：获取两个集合的相同元素，返回一个新的集合
            |(并集)：获取两个集合中所有的元素，相同的元素去重，返回一个新的集合
            -(差集)：集合1 - 集合2：获取集合1中的元素没有在集合2中，返回一个新的集合。
            ^(对称差集)：获取两个集合中不相同的元素，返回一个新的集合
            
        获取：
            len(集合)：获取集合的长度
            min(集合)：获取集合中元素的最小值
            max(集合)：获取集合中元素的最大值
            sum(集合)：获取集合的中元素的和
        增加：
            add(元素)：将元素添加到集合中,元素必须为不可变类型。
            update(可迭代类型)：将可迭代类型的元素添加到集合中。
        
        删除：
            pop(): 随机删除集合中的一个元素，返回删除元素的值
            remove(值)：根据元素的值将元素从集合中删除，如果指定的值不在集合中，会报错
            discard(值)：根据元素的值将元素从集合中删除，如果指定的值不在集合中，不会报错
            clear(): 清空集合
            del 集合：从内存中删除集合
"""

# 声明
'''
s1 = set()   # {}
print(s1, type(s1))

s2 = {1, 2, 4}
print(s2, type(s2))

s3 = {}
print(s3, type(s3))
'''

# 集合中元素的数据类型
"""
s1 = {1, 1.11, "hello", (1, 2.131, "python")}
print(s1)

l2 = [1, 1, 1, 2, 3, 3]
print(l2)
# str1 = "hello"
# 将列表转集合： set(列表/元组/字符串)
s2 = set(l2)
print(s2)

# 在将集合转列表：list(集合)/tuple(集合)/"".join(集合)
# print(list(s2))
# print(tuple(s2))
# print("".join(s2))

list1 = [1, 2, 3, 1, "hello", "....", "hello", 1]
print(list(set(list1)))
"""

# 运算
'''
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

# &
set3 = set1 & set2
print(set3)
# |
set4 = set1 | set2
print(set4)
# -
set5 = set1 - set2
print(set5)

set6 = set2 - set1
print(set6)
# ^
set7 = set1 ^ set2
print(set7)

str1 = "hello"
str2 = "HElLo"
str1_set1 = set(str1)
str1_set2 = set(str2)
print(str1_set1, str1_set2)
print("两个字符串相同的字符：", str1_set1 & str1_set2)
print("两个字符串不相同的字符：", str1_set1 ^ str1_set2)

dict1 = {"a": 100, "b": 200}
dict2 = {"A": 100, "b": 400}

dict1_keys = set(dict1.keys())
dict2_keys = set(dict2.keys())
print(dict1_keys & dict2_keys)

new_dict = {}

a = list(dict1_keys & dict2_keys)[0]
new_dict[a] = dict1[a] + dict2[a]
print(new_dict)
'''

# 获取
'''
set1 = {1, 2, 3, 100, -1}
print(min(set1))
print(max(set1))
print(sum(set1))
print(len(set1))
'''
# 增加
# add
'''
set1 = {1, 2, 3, 100, -1}
set1.add((1, 2, 3))
print(set1)
'''
# update
'''
set2 = set()
set2.update("hello")
set2.update([1, 2, 3])
set2.update((11, 21, 31))
set2.update({111, 211, 311})
set2.update({"a": 200, "b": 300}.keys())
set2.update({"a": 200, "b": 300}.values())
set2.update({"a": 200, "b": 300}.items())
print(set2)
'''

# 删除
# pop
set1 = set(range(10))
print(set1)
# print(set1.pop())
# remove
set1.remove(5)
print(set1)

# discard
set1.discard(99)
print(set1)

# clear
set1.clear()
print(set1)

# del 集合
del set1
