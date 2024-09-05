# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      decorator_demo.py
# Author:       lao_zhao
# Datetime:     2024/9/4 9:32
# Description:
# 
# ---------------------------------------------------------------------------
import requests

# 装饰器：在不改变源代码的情况下，丰富被装饰对象的功能。
"""
    @功能：
    1：将被装饰者的名称传入给装饰器的形参
    2：被装饰者的名称接收装饰器的返回值
"""
# 装饰器的格式--不传参的格式
"""
def 装饰器名称(形参):
    def 内部函数(*args, **kwargs):
        # 前置动作
        结果 = 形参()
        # 后置动作
        return 结果
    return 内部函数
"""
# 装饰器的格式--传参的格式
"""
def 装饰器名称(形参....):
    def 外部函数(形参):
        def 内部函数(*args, **kwargs):
            # 前置动作
            结果 = 形参()
            # 后置动作
            return 结果
        return 内部函数
    return 外部函数
"""


# def func1(param):
#     print(f"====前置动作======{param, param.__name__}")
#     return param


# @func1
# def demo1():
#     print(f"demo=={demo1.__name__}")
#     print("demo1函数")

'''
def decorator_demo(param):

    def inner(*args, **kwargs):
        print("======前置动作=======")
        value = param(*args, **kwargs)
        print("======后置动作=======")
        return value
    return inner


@decorator_demo
def demo(a=1, b=2):
    print(f"demo==={demo}")
    print(f"功能代码--------{a}-{b}-")


demo(a=100, b=200)
'''


def decorator(name):
    def outer(func_name):
        def inner(*args, **kwargs):
            print(f"-----------前置动作------{name}------")
            value = func_name(*args, **kwargs)
            print("-----------后置动作------------")
            return value
        return inner
    return outer


@decorator(name="张三")
def func2():
    print("func2函数")


func2()


def decorator_func(func_name):
    def inner(*args, **kwargs):
        try:
            print(f"执行的是：{func_name.__name__}，功能描述为：{func_name.__doc__}")
            result = func_name(*args, **kwargs)
            print("---------------")
        except Exception as e:
            print(f"产生错误，错误为{e},形参的值为：{args, kwargs}")
            raise e
        else:
            return result
    return inner


@decorator_func
def login_req():
    """科瑞登录"""
    res = requests.request(method="post", url="http://47.109.99.224:8090/korei/login.ht", data={"username": "admin", "password": "1"})

    assert "退出1" in res.text


login_req()