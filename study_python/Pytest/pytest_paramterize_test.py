# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      pytest_paramterize_test.py
# Author:       lao_zhao
# Datetime:     2024/9/3 9:58
# Description:
# 
# ---------------------------------------------------------------------------
import pytest

"""
    pytest有两种方式给用例实现参数化。
        1：使用装饰器@pytest.mark.parametrize实现用例的参数化。
            装饰器@pytest.mark.parametrize的注意点
             i): @pytest.mark.parametrize("字符串", 可迭代类型)需要有两个形参
             ii): 设置用例的形参来取可迭代类型的元素，装饰器传入的字符串需要和用例的形参的格式一摸一样，自定义固件除外。
             iii): 如果用例的形参超过1个以上，装饰器可迭代类型数据必须是二维的。二维数据中子容器的元素个数需要和用例形参的个数一致。

"""


@pytest.mark.parametrize("a1,a2,a3", [[1, 2, 3], [4, 5, 6]])
def test1(fix1, a1, a2, a3):
    print("用例函数")
    print(f"a1={a1}, a2={a2}, a3={a3}")