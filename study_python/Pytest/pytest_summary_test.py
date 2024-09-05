# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      pytest_summary_test.py
# Author:       lao_zhao
# Datetime:     2024/9/2 9:27
# Description:
# 
# ---------------------------------------------------------------------------
import pytest

"""
    pytest的标识符规范：
        py文件：test开头或test.py结尾
        类：Test开头
        用例：test开头
"""
"""
    pytest在终端中执行用例的py文件时的方式：
        pytest 用例py文件 === python -m pytest 用例py文件
        
        参数的指定：
            -s: 显示用例中的输出结果
            -v: 显示用例执行的详细结构
            -vs: 显示用例的输出结果和详细信息
            -x: 当前用例py文件中只要发送任何错误，当前用例py文件就结束执行
            --maxfail=n: 当前用例py文件可以产生n-1次错误，只要超过n-1次错误，py文件结束执行
            
        指定运行用例函数：pytest [参数] 用例py文件::用例函数名
        指定运行用例方法：pytest [参数] 用例py文件::用例类名::用例方法名

"""
"""
    终端中执行的结果：
        . : 执行通过
        F : 表示断言不通过
        E : 表示代码产生错误
"""
"""
    pytest的断言：
        assert 实际结果 == 预期结果
"""


# 用例函数
def test_func2():
    print("用例函数2")
    try:
        i = "a" + 1
    except Exception as e:
        print(e)


def test_func3():
    print("用例函数3")
    try:
        assert 1 == 2
    except AssertionError:
        print("断言失败")
        raise AssertionError("断言失败")
    except Exception as e:
        print("产生其他类型的错误， 错误为：", e)


def test_func1():
    print("用例函数1")


class TestDemo:

    def test_02(self):
        print("用例方法2")

    def test_01(self):
        print("用例方法1")


if __name__ == '__main__':
    pytest.main()
