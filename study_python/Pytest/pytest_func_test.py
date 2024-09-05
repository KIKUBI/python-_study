# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      pytest_func_test.py
# Author:       lao_zhao
# Datetime:     2024/9/3 10:56
# Description:
# 
# ---------------------------------------------------------------------------
import pytest

"""
    1: @pytest.fixture(scope="级别", autouse=True/False, params=可迭代类型)
    2：@pytest.mark.parametrize("字符串", 可迭代类型)
    3：@pytest.mark.usefixtures("自定义固件名称")
    
    4: @pytest.mark.skip(reason="无条件跳过不执行")
    5: @pytest.mark.skipif(bool表达式, reason="有条件跳过不执行")
    6: @pytest.mark.xfail(reason="描写信息")：预期失败的用例 不统计到测试结果中。
"""
"""
    7: @pytest.mark.run(order=n): n的值越小，越先运行--更改用例执行的优先级
        pip install pytest-ordering---pytest的插件
        
    8：给用例设置标签
        @pytest.mark.标签名
        在终端指定运行相同标签名的用例：pytest [参数] 用例py文件 -m=标签名
        
    9： @pytest.mark.dependency([depends=["用例名称"]])：实现用例之间的依赖
        pip install pytest-dependency
"""


'''
@pytest.mark.p1
@pytest.mark.run(order=3)
def test1():
    print("用例1")


@pytest.mark.p0
@pytest.mark.run(order=2)
def test2():
    print("用例2")


@pytest.mark.p0
@pytest.mark.run(order=1)
def test3():
    print("用例3")
'''


class TestDemo:
    @pytest.mark.dependency()
    def test01(self):
        print("用例方法")
        assert 1 == 2


@pytest.mark.dependency(depends=["TestDemo::test01"])   # 标记当前用例是否被依赖
def test1():
    print("用例1")
    assert 1 == 1


@pytest.mark.dependency(depends=["test1"])   # 标签当前的用例依赖的哪些用例
def test2():
    print("用例2")
    assert 1 == 2


@pytest.mark.dependency(depends=["test1", "test2"])
def test3():
    print("用例3")
    assert 1 == 1




if __name__ == '__main__':
    pytest.main()