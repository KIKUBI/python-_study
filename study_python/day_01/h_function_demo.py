# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      h_function_demo.py
# Author:       lao_zhao
# Datetime:     2024/8/1 14:23
# Description:
# 
# ---------------------------------------------------------------------------

"""
    高阶函数：
        map(函数名, 可迭代类型)：使用函数名对应的函数对可迭代类型的每个元素进行操作，操作之后返回一个map类型。map类型为可迭代类型。
                    注意：函数名对应的函数，必须有一个形参，必须有一个返回值。

        reduce(函数名, 可迭代类型)：使用函数名对应的函数对可迭代类型的前两个元素进行操作，操作之后得到的结果再和可迭代类型的第三个元素进行操作
                                依次类推，返回值就为操作的结果。
                    注意：函数名对应的函数，必须有两个形参，必须有一个返回值。

        filter(函数名, 可迭代类型)：使用函数名对应的函数对可迭代类型的每个元素进行过滤，返回一个过滤器类型。过滤器类型是可迭代类型。
                    注意：函数名对应的函数，必须有一个形参，必须有一个bool类型返回值。
        sorted(可迭代类型[, reverse=False])：对可迭代类型进行排序，排序之后返回一个列表，可以使用reverse控制升序或降序(默认升序)
        reversed(有序的可迭代类型)： 对可迭代类型的元素进行反转，返回一个reversed类型。reversed类型是可迭代类型。


"""
from functools import reduce

# map
'''
list1 = [1, 2, 3, 4]

def demo1(param):
    # return param*param
    if param % 2 == 0:
        return param * param
    else:
        return param


result1 = map(demo1, list1)
print(result1, type(result1))
print(list(result1))



str1 = set("Abcd成都")
print(str1)

def demo2(param):
    return ord(param)


res1 = map(demo2, str1)
print(tuple(res1))
'''

# reduce
'''
def demo3(param1, param2):
    print(f"param1={param1}, param2={param2}")
    return str(param1) + str(param2)

list1 = ['1', '2', '3', '4', '100', 100, 200]

res = reduce(demo3, list1)                     # alt+enter  == > 快速导入
print(res, type(res))
'''


# filter
'''
def demo4(param):
    if param.isdigit():
        return True
    else:
        return False

list1 = "afa3131f晨读撒131法发"


res = filter(demo4, list1)
print(res, type(res))
print(list(res))


l2 = ['3', '1', '3', '1', '1', '3', '1']
def demo5(param1, param2):
    return int(param1) + int(param2)


print(reduce(demo5, l2))
'''

# sorted
'''
list1 = [1010, 200, 300]
str1 = "Acsafa"
dict1 = {"a1": 100, "b": 200, "a2": 100}
print(sorted(dict1.items(), reverse=True))
'''

list1 = [1010, 200, 300]
res = reversed(list1)
print(res, type(res))
print(list(res))


set1 = (1990, 100, 300)
res1 = reversed(set1)
print(list(res1), type(res1))

str1 = "bacs"
res2 = reversed(str1)
print(res2, type(res2))