# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      list_demo.py
# Author:       lao_zhao
# Datetime:     2024/7/26 9:28
# Description:
# 列表
# ---------------------------------------------------------------------------


"""
    列表：一致有序元素的组合，元素的类型可以是任何的类型，每个元素之间由英文的逗号隔开。

    声明：
        变量 = [元素1, 元素2.....]
"""
"""
    列表的特点：
        1：列表是有序的。列表可以进行下标操作，也可以进行切片的操作。
                列表[下标]：获取指定下标位置的元素
                列表[开始下标:结束下标]：结束下标需要在开始下标的右边
                列表[开始下标:结束下标:步长]：参考字符串的切片操作
                
        2：可变:列表的长度是可变的，列表中的元素也是可变的。
            增：
                append(值)：将一个值追加到列表的末尾.
                insert(下标, 值)：将值插入到列表的指定下标位置
                extend(列表1)：将列表1中元素依次追加到列表的末尾
                +：列表和列表可以相加，相加之后会得到一个新的列表
                *: 列表可以和整形相乘，会得到一个新的列表，乘n，列表中的元素会出现n次
            查：
                len(列表)：获取列表的长度/元素个数
                index(元素)：获取元素在列表中的下标位置
                count(元素)：获取元素在列表中的个数
                min(列表)：获取列表中元素最小值，元素类型必须一致
                max(列表)：获取列表中元素最大值，元素类型必须一致
                sum(列表): 获取列表中元素的和，元素的类型必须为整形
            
            改:
                列表[下标] = 值：更改指定下标位置元素的值。
                sort([reverse=False]): 对列表中的元素进行排序，可以控制是否为升序(默认)或降序--方法
                                注意：会更改原来列表中元素的顺序。
                sorted(列表[, reverse=False]):对列表中的元素进行排序，可以控制是否为升序(默认)或降序--函数
                                注意：不会更改原来列表中元素的顺序。
                reverse(): 列表反转,注意：会更改原来列表中元素的顺序。
                列表[::-1]:  列表反转,注意：不会更改原来列表中元素的顺序。
                
            删:
                pop([index]): 默认删除列表末尾的元素，删除元素之后，会返回删除元素的值。注意：会改变列表的长度。
                remove(元素)：根据元素的值，将元素从列表中删除。如果元素不在列表中会报错。
                clear(): 清空列表
                del 列表[下标]：将列表下标对应的值从内存地址中删除。
                del 列表：将列表从内存地址中删除。
            
            
"""
# [] {}

# 声明
# 声明一个空列表
'''
list1 = list()
print(list1, type(list1))

list2 = []
print(list2, type(list2))

# 声明一个非空列表
l1 = [1]
print(l1, type(l1))

name = "tom"
l2 = [1, 3.14, "hello", [3, 4, 5], 1, name]
print(l2, type(l2))
'''

# 下标操作
'''
list1 = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9
]
print(list1, type(list1))

print(list1[0])
print(list1[-1])

# 切片
# 列表[开始下标:结束下标]：结束下标需要在开始下标的右边
print(list1[1:-1])
print(list1[:])
print(list1[100:200])

# 列表[开始下标:结束下标:步长]
print(list1[1:-1:2])
print(list1[::2])
print(list1[1::2])
print(list1[::-1])
'''

# 操作
'''
list1 = ["a", "b", "c"]
list2 = [100, 200, 4.12]

list3 = list1 + list2
print(list3)
print(list1)
print(list2)


list4 = list1 * 2
print(list4)
'''
# append
'''
print("-"*100)
list1 = ["a", "b", "c"]
list1.append("hello")
list1.append([1, 2, 3, 4])
list1.append(3.13)
print(list1)
'''
# insert
'''
list1 = [100, 1, 3]
print(id(list1))
list1.insert(2, "hello")
print(list1)
print(id(list1))
'''
# extend
'''
list1 = [1, 2, 3, 4]
list2 = ["h", "l", "z"]

list1.extend(list2)
print(list1)
'''

# 查
# len
'''
list1 = ["he1", "xx", "tom", 1, 2, [4, 5, 6], 1, 200, 300, 1, [4, 5, 6]]
print(len(list1))
'''
# index
'''
print(list1.index(1, list1.index(1)+1, -1))
'''
# count
'''
print(list1.count([4, 5, 6]))
'''
# min, max, sum
'''
list1 = [3, 10, 40, 100, 200]
# list1 = ["a", "b", "c", "成都"]
print(min(list1))
print(max(list1))
print(sum(list1))
'''

# 更改
'''
list1 = [1, 2, 3]
list1[1] = "python"
print(list1)
'''
# sort/sorted
'''
list1 = ["AZ", "AC", "c", "D"]
list1.sort(reverse=True)

print(list1)
print(ord("A"))
print(ord("D"))
print(ord("b"))
print(ord("c"))

list2 = [100, 2, 4, 200]
print("排序之前的第一个元素的值：", list2[0])
list2.sort(reverse=True)
print(list2)
print("排序之后的第一个元素的值：", list2[0])

list3 = [10, 4, 5, 20, 40]
print("排序之前的列表：", list3)
new_list = sorted(list3, reverse=True)
print(new_list)
print("排序之后的列表：", list3)
'''

# reverse
'''
list1 = [1, 2, 10, 20, 3, 4, 5]
print("反转之前的列表：", list1)
list1.reverse()
print(list1)
print("反转之后的列表：", list1)


print("-"*100)
list2 = [1, 2, 10, 20, 3, 4, 5]
print("反转之前的列表：", list2)
list3 = list2[::-1]
print(list3)
print("反转之后的列表：", list2)
'''

'''
list4 = [1, 2, 10, 20, 3, 4, 5]
new_list = reversed(list4)
print(list(new_list))
'''

# 删除
# pop
'''
list1 = ["a", "B", "C", "d"]
print(list1.pop(2))
print(list1, len(list1))

name = "tom"
age = 18
sex = "男"

list_demo = []
list_demo.append(name)
list_demo.append(age)
list_demo.append(sex)

print(list_demo)
# print(list_demo.pop())
# print(list_demo.pop())
# print(list_demo.pop())
'''

# remove
'''
list1 = [1, 2, 3, 1, 4, 5]
list1.remove(1)
list1.remove(1)
print(list1)
'''
# clear
'''
list1 = [1, 2, 3, 1, 4, 5]
list1.clear()
print(list1)
'''

# del
'''
list1 = [1, 2, 3, 1, 4, 5]
del list1[0]
print(list1)

# del list1
# print(list1)

# s1 = "hello"
# del s1
# print(s1)
'''


list1 = [1, 2, 3, [4, 5, 6]]

print(list1[-1][0])
list1[-1][0] = "hello"
print(list1)
