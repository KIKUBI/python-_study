# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      function_demo.py
# Author:       lao_zhao
# Datetime:     2024/7/31 14:15
# Description:
# 函数
# ---------------------------------------------------------------------------


"""
    函数：一组功能代码的组合, 给这一组功能代码起个别名，这个别名就是函数名。

"""
import requests

# input, print, len, min, max, sum

# 自定义函数的格式：
"""
def 函数名([形参]):
    一组功能代码
    [return 返回值..]
"""
# 执行/调用函数的方式
"""
函数名(实参)
"""

# return
"""
    return的功能：
        1: 函数返回值, 可以有1个或多个，如果返回多个值，只使用一个变量接收返回值，变量的数据类型为元组。
                注意：函数的默认返回值为None。
        2：return之后的代码不会在执行，return也表示函数的结束
"""
# 形参
"""
    函数中的功能代码动态变化的数据，就定义为函数的形参。---重要
    形参的称呼：
        位置参数：函数的形参可能有多个，在调用函数时，按照形参的位置顺序传入值。
        关键参数：在调用函数时，按照形参的名称传入值。
        默认参数：在定义函数时，可以给函数的形参设置默认值。
                在调用函数时，可以给默认参数传入值，如果传入数据，默认参数的值就为传入的值
                在调用函数时，如果没有给默认参数传入值，默认参数就使用自己的默认值。
        不定长参数：
            不定长位置参数：在定义形参时，在形参名前加一个*就为不定长位置参数，不定长位置参数在函数体中以元组的形式参与运算。
                    不定长位置参数传参时，可以不用传参，可以传入1个或多个。
            不定长关键字参数：在定义形参时，在形参名前加一个**就为不定长关键字参数, 不定长关键字参数在函数体中以字典的形式参与运算。
                    不定长关键字参数传参时，可以不用传参，可以传入1个或多个。
                    
        注意：
            定义函数时，形参的位置顺序为：位置参数-->不定长位置参数-->默认参数-->不定长关键字参数
            传参的顺序：位置参数-->不定长位置参数==>按照形参的位置顺序进行传参，默认参数-->不定长关键字参数==>按照形参名称进程传参(不定长关键字参数按照要求进程传参)
"""

'''
def my_print():
    print("我的输出函数")


my_print()
'''
'''
def add(number, number2):
    result = number + number2
    print(f"number加100的和为：{result}")


add(1, 2)
'''

'''
def get_sum(number1, number2):
    result1 = number1 + number2
    result2 = number1 - number2
    return result1, result2


# data = get_sum(100, 200)
# print(data)


data1, data2 = get_sum(200, 10)
print(data1, data2)

data = get_sum(200, 40)
print(data, type(data))
'''
'''
def func(num1, num2):
    """
    第一行描述函数的功能
    :param num1: 传入整形
    :param num2: 传入整形
    :return: 返回num1和num2的和
    """
    print(id(num1))
    print(id(num2))
    res1 = num1 + num2
    print(f"结果为{res1}")
    return res1
    print("=============")


result = func(20, 10)
print(result)
'''


'''
def score_level():
    while True:
        res = input("请输入分数：").strip()
        if res == "q":
            break

        # 使用.分割字符串，得到分割之后的结果为列表。
        res_list = res.split(".")
        # 定义分数的变量
        score = -1

        # len(res_list) in [1, 2]判断列表的长度要么为1，要么为2
        # "".join(res_list).isdigit() 将列表中的元素拼接为字符串，再判断字符串是否为数字组成的。
        if len(res_list) in [1, 2] and ("".join(res_list).isdigit()):
            # 校验是否为整形
            if res.isdigit():
                score = int(res)
            else:
                # 校验是否为浮点数
                score = float(res)

        # 对分数进行级别的判断
        if 150 >= score >= 90:
            print("A")
        elif 60 <= score < 90:
            print("B")
        elif 0 <= score < 60:
            print("C")
        else:
            print("输入的分数错误")
'''
'''
def func1(row):
    strs = ""
    for i in range(1, row):
        for _ in range(row - 2, i - 1, -1):
            # print(" ", end="")
            strs += " "

        for k in range(1, 2 * i):
            if k == 1 or k == 2 * i - 1:
                # print("*", end="")
                strs += "*"
            else:
                # print(" ", end="")
                strs += " "
        strs += "\n"

    for i in range(1, row - 1):
        for _ in range(i):
            # print(" ", end="")
            strs += " "
        for k in range(2 * (row - 2), 2 * i - 1, -1):
            if k == 2 * (row - 2) or k == 2 * i:
                # print("*", end="")
                strs += "*"
            else:
                # print(" ", end="")
                strs += " "
        strs += "\n"

    return strs
'''

'''
def fibo(month):
    m1 = 1
    m2 = 1
    for i in range(3, month+1):
        # sum1 = m1 + m2
        # m1 = m2
        # m2 = sum1
        m1, m2 = m2, m1 + m2

    return m2
'''


"""
def func2(number=9):
    for i in range(1, number+1):
        for j in range(1, i+1):
            print(f"{j}X{i}={j*i}\t", end="")
        print()


func2(6)
"""


"""
def func_1(name, age, score=60):
    print(f"姓名为：{name}, 年龄为：{age}岁，考试的分数为:{score}分！")


# func_1("张三", 18, 90)
# func_1(20, "李四", 91)
#
# func_1(score=99, age=18, name="王五")
func_1("tom", 10)
func_1("tom", 10, score=79)
"""


# 不定长位置参数
'''
def demo(a, b):
    print("demo函数--------------", a, b)


def func_2(*param):
    print("param的值为：", param, type(param))
    # t1 = (1, 2)   # *t1 ==> 1, 2 ===> demo(1, 2)
    # l1 = [1, 2, 3, "python"]
    # set1 = {1, 2, 3, "成都"}
    # str1 = "abc"
    # dict1 = {"a": 100, "b": 200}
    # print(*t1)  # print(*t1) ---> print(1, 2)
    # print(*l1)
    # print(*set1)
    # print(*str1)
    # print(*dict1)

    demo(*param)


func_2(11, 12)
'''

# 不定长关键字参数
'''
def demo1(name, age):
    print(f"姓名为：{name}, 年龄为：{age}岁！")


def func_3(**params):
    print(params, type(params))  # **params ==> name=张三， age=18 ==> demo1(name=张三, age=18)
    # print(**params)              # **params ==> a=1, b=2 ==> print(a=1, b=2)
    demo1(**params)



# func_3(a=1, b=2)
func_3(name="张三", age=18)


requests.request()
'''


# 位置参数  默认参数 不定长的参数
'''
def func_demo(param1, *args, value="默认参数", **kwargs):
    print(f"位置参数param1的值为：{param1}")
    print(f"不定长位置参数args的值为：{args}")
    print(f"默认参数value的值为：{value}")
    print(f"不定长关键字参数kwargs的值为：{kwargs}")


func_demo(1, 2, 3, 4, name="张三", age=18, score=99)
func_demo(1, args=(1, 2, 3), name="张三", age=18, score=99)
'''


dict1 = {"a": 1, "b": 2, "c": 3, "d": 4}
dict2 = {"c": 5, "d": 6, "e": 7, "f": 8}

# dict3 = {"a": 1, "b": 2, "c": 8, "d": 10, "e": 7, "f": 8}

'''
# 取出两个字典中的key，存放在一个列表中，并对key去重，再进行升序排序
dict_keys = sorted(set(list(dict1.keys()) + list(dict2.keys())))

# 创建一个新的字典，存放操作之后的键值对
new_dict = {}
# 循环取出key
for key in dict_keys:
    # 判断key是否同时在字典1和字典2中，取出key对应的value，并相加，存放到一个新的字典中
    if key in dict1.keys() and key in dict2.keys():
        new_dict[key] = dict1[key] + dict2[key]
    # 判断key是否只在字典1中，如果是，取出key对应的value，存放到新的字典中
    elif key in dict1.keys():
        new_dict[key] = dict1[key]
    else:
        new_dict[key] = dict2[key]

print(new_dict)
'''


def dict_value_sum(dict_1, dict_2):
    """
    对两个字典中相同key的value相加，得到一个新的字典，key有序
    :param dict_1: 字典
    :param dict_2: 字典
    :return: 字典
    """
    # 取出两个字典中的key，存放在一个列表中，并对key去重，再进行升序排序
    dict_keys = sorted(set(list(dict_1.keys()) + list(dict_2.keys())))

    # 创建一个新的字典，存放操作之后的键值对
    new_dict = {}
    # 循环取出key
    for key in dict_keys:
        # 判断key是否同时在字典1和字典2中，取出key对应的value，并相加，存放到一个新的字典中
        if key in dict1.keys() and key in dict2.keys():
            new_dict[key] = dict1[key] + dict2[key]
        # 判断key是否只在字典1中，如果是，取出key对应的value，存放到新的字典中
        elif key in dict1.keys():
            new_dict[key] = dict1[key]
        else:
            new_dict[key] = dict2[key]

    return new_dict


dict1 = {"a": 1, "b": 2, "c": 3, "d": 4}
dict2 = {"c": 5, "d": 6, "e": 7, "f": 8}

# dict1.update(dict2)
# print(dict1)

dict3 = dict_value_sum(dict1, dict2)
print(dict3)


def dict_value_sum2(dict_1, dict_2):
    # 循环取出第二个字典中所有的key
    for key in dict_2.keys():
        # 判断key是否在第一个字典中，如果在，更新第一个字典中key的值，值为两个字典中key对应的value
        if key in dict_1.keys():
            dict_1[key] = dict_1[key] + dict_2[key]
        else:
            dict_1[key] = dict_2[key]

    return dict_1


print(dict_value_sum2(dict1, dict2))
