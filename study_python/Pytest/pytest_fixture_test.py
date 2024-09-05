# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      pytest_fixture_test.py
# Author:       lao_zhao
# Datetime:     2024/9/2 11:21
# Description:
# 
# ---------------------------------------------------------------------------
import pytest


"""
    固件：用例执行之前和执行之后的动作
        setup: 用例执行之前的前置动作
        teardown：用例执行之后的后置动作。

    pytest自带的固件：
        setup_module/teardown_module: 用例模块(用例py文件)执行之前和执行之后的动作
        setup_function/teardown_function: 用例函数执行之前和执行之后的动作---只作用函数用例
        setup_class/teardown_class: 用例类执行之前和执行之后的动作---只作用用例类--必须写在用例类中
        setup_method/teardown_method: 用例方法执行之前和执行之后的动作--只作用用例方法--必须写在用例类中
        
        函数用例执行时固件的执行顺序：
            setup_module-->setup_function-->用例函数-->teardown_function-->teardown_module
            setup_module
                -->setup_function-->用例函数1-->teardown_function
                -->setup_function-->用例函数2-->teardown_function
            -->teardown_module
            
        用例方法执行时固件的执行顺序：
            setup_module-->setup_class-->setup_method-->用例方法-->teardown_method-->teardown_class-->teardown_module
            setup_module-->setup_class
                -->setup_method-->用例方法1-->teardown_method
                -->setup_method-->用例方法2-->teardown_method
            -->teardown_class-->teardown_module
"""


def test_01():
    print("用例函数1")


def test_02():
    print("用例函数2")


def setup_module():
    print("module级别自带的固件----前置动作-setup_module")


def teardown_module():
    print("module级别自带的固件----后置动作-teardown_module")


def setup_function():
    print("function级别自带的固件----前置动作-setup_function")


def teardown_function():
    print("function级别自带的固件----后置动作-teardown_function")


class TestDemo:
    # def __init__(self):
    #     print("构造方法")  # 如果用例类中有自定义的构造方法时，用例类不会被执行，用例类中的用例方法也不会被执行

    @staticmethod
    def setup_class():
        print("class级别自带的固件----前置动作-setup_class")

    @staticmethod
    def teardown_class():
        print("class级别自带的固件----后置动作-teardown_class")

    @classmethod
    def setup_method(cls):
        print("method级别自带的固件----前置动作-setup_method")

    @staticmethod
    def teardown_method():
        print("method级别自带的固件----后置动作-teardown_method")


    def test_01(self):
        print("用例方法1")

    def test_02(self):
        print("用例方法2")

if __name__ == '__main__':
    pytest.main()