# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      test_demo.py
# Author:       lao_zhao
# Datetime:     2024/9/2 16:44
# Description:
# 
# ---------------------------------------------------------------------------
import pytest


def test_demo():
    print("用例函数")


@pytest.mark.usefixtures("fix1")
def test_1():
    print("用例函数1")
    # print(fix1)


@pytest.mark.usefixtures("fix1")
class TestDemo:

    def test1(self):
        print("用例方法1")

    def test2(self):
        print("用例方法2")