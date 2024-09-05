# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      conftest.py
# Author:       lao_zhao
# Datetime:     2024/9/2 16:54
# Description:
# 
# ---------------------------------------------------------------------------
import pytest
import requests

from study_python.Pytest.test_example.db import DB


@pytest.fixture(scope="session")
def fix_req():
    # 创建Session对象
    sess = requests.sessions.Session()
    yield sess


@pytest.fixture(scope="session")
def fix_db():
    db = DB()
    yield db
    db.close()


@pytest.fixture(scope="session")
def fix_dependency():
    dependency_dict = {}
    yield dependency_dict