# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      pytest_custom_fixture_test.py
# Author:       lao_zhao
# Datetime:     2024/9/2 14:03
# Description:
# 
# ---------------------------------------------------------------------------
import time
import pytest
from selenium import webdriver

# 装饰器功能在不改变源代码的情况下，丰富被装饰对象的功能。
"""
    pytest中使用装饰器@pytest.fixture装饰器函数，这个函数就是自定义固件。

    注意：
        1：自定义固件如果有返回值，如果在用例中使用自定义固件的名称，自定固件的名称的值为自定义固件的返回值。
        2：用例函数/用例方法，可以调用多个自定义固件，如果自定义固件的级别相同，谁在前谁先执行，如果级别不同，级别高的先执行。
            如果自定义的固件和自带的固件级别相同，自带的固件比自定义的固件先运行。
            
        3：自定义固件可以使用return和yield返回值，返回值之前的代码为自定义固件setup的功能，返回值之后的代码为teardown的功能(return没有teardown的功能)
           自定义固件如果使用yield返回值，自定义固件中有且只能有一个yield。
        4：自定义固件还可以调用自定固件----慎用。
        5：装饰器@pytest.fixture中使用形参scope指定自定义固件的级别。
        6：自定义固件通常是放在conftest.py文件中，pytest框架会自动调用，不需要导入。conftest.py一般和用例py文件在同一目录中。只有自定义固件执行之后，才会生效。
"""
# 自定义固件的调用方式
"""
    1: 将自定义固件的名称放在用例的形参中，就实现了自定义固件的调用。--可以获取自定义固件的返回值。
    2: 将装饰器@pytest.fixture(autouse=True), 所有的用例都会默认调用将autouse设置为True的自定义固件
        如果自定义固件有返回值，这种方式所说可以默认调用自定义固件，但是没法获取自定义 固件的返回值。
    3：使用装饰器@pytest.mark.usefixtures("自定义固件的名称")装饰用例函数/方法可以使用自定义固件的调用
"""
"""
    自定义固件的级别：
        session: 会话级别--最高级别---只会执行一次
        package：包级别---测试阶段---只会执行一次
        module: 模块级别---只会执行一次
        class: 类级别--会单独作用于每个函数用例-方法：会作用于类。
        function：函数/方法级别--会单独作用于每个函数和方法用例---默认级别
        
        session --> package --> module --> class --> function
        注意：实际工作中，自定义固件默认指定为session级别。
"""


'''
@pytest.fixture()
def fix1():
    print("自定义固件fix1")
    yield "hello1"
    print("自定义固件的后置动作")


def test_01(fix1):
    print("测试用例1")
    print("-----------------------------", fix1)
    time.sleep(2)

'''


'''
@pytest.fixture()
def fix1():
    print("自定义固件1")
    yield "hello"
    print("自定义fix1固件的后置")


@pytest.fixture()
def fix2(fix1):
    print("自定义固件2")
    print("---------fix1 =", fix1)
    yield
    print("自定义fix2固件的后置")


def test_01(fix2):
    print("用例函数1")
'''


# 自定义固件的例子
'''
@pytest.fixture()
def my_driver():
    driver = webdriver.Edge()
    yield driver
    driver.quit()


@pytest.fixture()
def max_driver_window(my_driver):
    my_driver.maximize_window()
    yield my_driver
    my_driver.close()


def test_baidu(max_driver_window):
    max_driver_window.get("https://www.baidu.com")
    time.sleep(5)
'''


def setup_module():
    print("module级别自带的固件----前置动作-setup_module")


def teardown_module():
    print("module级别自带的固件----后置动作-teardown_module")


def setup_function():
    print("function级别自带的固件----前置动作-setup_function")


def teardown_function():
    print("function级别自带的固件----后置动作-teardown_function")


# def test_01(fix_function, fix_class, fix_module, fix_package, fix_session):
#     print("用例函数1")
#
#
# def test_02(fix_function, fix_class):
#     print("用例函数2")


class TestDemo:
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

    def test_1(self, fix_function, fix_class, fix_module, fix_package, fix_session):
        print("用例方法1")

    def test_2(self, fix_function):
        print("用例方法2")


if __name__ == '__main__':
    pytest.main()