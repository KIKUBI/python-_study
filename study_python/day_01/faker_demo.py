# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      faker_demo.py
# Author:       lao_zhao
# Datetime:     2024/8/6 15:42
# Description:
# 
# ---------------------------------------------------------------------------
import random

from faker import Faker

"""
    pip：python对第三模块/包/库进行管理
        下载：pip install 第三模块/包/库的名称
        卸载：pip uninstall 第三模块/包/库
        查看本地环境安装了哪些第三模块/包/库：pip list

"""

list1 = ["zh_cn"]


for _ in range(20):
    data = Faker(locale=random.choice(list1))
    for _ in range(3):
        print(data.name_male(), data.address(), data.phone_number(), data.company())