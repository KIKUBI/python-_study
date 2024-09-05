# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      conftest.py
# Author:       lao_zhao
# Datetime:     2024/9/2 16:15
# Description:
# 
# ---------------------------------------------------------------------------
import pytest

from study_python.Pytest.test_example.db import DB


@pytest.fixture(scope="session")
def fix_session():
    print("session级别------------setup功能")
    yield
    print("session级别------------teardown功能")


@pytest.fixture(scope="package")
def fix_package():
    print("package级别------------setup功能")
    yield
    print("package级别------------teardown功能")


@pytest.fixture(scope="module")
def fix_module():
    print("module级别------------setup功能")
    yield
    print("module级别------------teardown功能")


@pytest.fixture(scope="class")
def fix_class():
    print("class级别------------setup功能")
    yield
    print("class级别------------teardown功能")


@pytest.fixture(scope="function")
def fix_function():
    print("function级别------------setup功能")
    yield
    print("function级别------------teardown功能")


@pytest.fixture()
def fix1():
    print("默认级别------------setup功能")
    yield "hello"
    print("默认级别------------teardown功能")


@pytest.fixture(scope="session", autouse=True)
def db_fix():
    print("setup中创建DB对象")
    db = DB()
    yield db
    print("teardown功能中关闭数据库")
    db.close()
