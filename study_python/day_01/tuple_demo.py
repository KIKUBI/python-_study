# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      tuple_demo.py
# Author:       lao_zhao
# Datetime:     2024/7/26 14:01
# Description:
# 元组
# ---------------------------------------------------------------------------


"""
    元组：由一组有序的元素组成，元组是不可变的，元组中的元素可以为任意类型。
         元组一般是用来保护数据使用的。

    元组的声明：
        变量 = ()
        变量 = tuple()
        变量 = (元素,....)
"""
"""
    元组的特点：
        1: 有序，下标或切片操作
        2: 元组是不可变的。元组的长度和元组中的元素的值是不可改变，如果元组中嵌套了列表等，列表中的元素是可以发生改变。
            获取：
                len(元组)：获取元组的长度
                index(元素)：获取元素在元组中的下标位置
                count(元组)：获取元素在元组中的个数
                min(元组)：获取元组中最小的值
                max(元组)：获取元组中最大的值
                sum(元组)：获取元组中的元素求和
            增加：
                +: 元组可以和元组相加，得到一个新的元组
                *n: 元组可以和整形n相乘，元组中的元素就会出现n次。
                
            更改：
                先将元组转成列表===>list(元组)
                再使用列表的更改操作对列表中的元素进行更改
                再将更改之后的列表转成元组===>tuple(列表)

            删除：
                del 元组
"""

'''
t1 = ()
print(t1, type(t1))

t2 = tuple()
print(t2, type(t2))

t3 = (1, "111", 4.31, (1, 2, 3), [3, 4, 5])
print(t3, type(t3))

# 下标操作
print(t3[0])
print(t3[-1])
print(t3[0:-2:2])

t3[-1].append("hello")
print(t3)
'''

# 获取
'''
t1 = (1, 2, 100, 3, 4, 1)
print(t1, len(t1))

print(min(t1))
print(max(t1))
print(sum(t1))

# print(t1.index(1, 1))
#
# list1 = [1, 2, 3, 4, 1]
# print(list1.index(1, 2))
#
# str1 = "12341"
# print(str1.index("1", 1))

# print(t1.count(1))

s1 = "dabc"
print(sorted(s1, reverse=True))
'''

# 增加
'''
t1 = (1, 2, 3)
t2 = ("hello", [1, 2, 3])

t3 = t1 + t2
print(t3)

t4 = t2 * 2
print(t4)
'''

# 更改
'''
tuple1 = (1, 2, 3, 4, ["hello", 1.3], (3, 4, 5))
# 先将元组转成列表
list1 = list(tuple1)
print(list1)
# 修改列表中的元素
list1[3] = 400
print(list1)
# 将更改之后的列表转成元组
tuple2 = tuple(list1)
print(tuple2)
'''


tuple1 = (1, 2, 3, 4, ["hello", 1.3], (3, 4, 5))
t1 = tuple1[:3]
t2 = tuple1[4:]
print(t1)
print(t2)

t3 = t1 + t2
print(t3)