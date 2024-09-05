# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      string_demo.py
# Author:       lao_zhao
# Datetime:     2024/8/6 16:43
# Description:
# 
# ---------------------------------------------------------------------------
import string, random

"""
    字符串模块：
        string.ascii_letters: 获取英文字母的大小写
        string.ascii_uppercase: 获取大写的英文字母
        string.ascii_lowercase: 获取大写的英文字母
        string.digits:获取0-9之间的数字
"""


print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.digits)

print("".join(random.sample(string.ascii_letters + string.digits+r".#%&^", 16)))