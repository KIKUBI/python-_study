# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      os_demo.py
# Author:       lao_zhao
# Datetime:     2024/8/7 9:58
# Description:
# 
# ---------------------------------------------------------------------------
import os

"""
    os.path.getsize(path): 获取文件的字节数大小
    os.path.getctime(path): 获取文件的创建时间
    os.path.getmtime(path): 获取文件的修改时间
    os.path.getatime(path): 获取文件的访问时间

"""

print(__file__)
print(os.path.dirname(__file__))
dir = os.path.dirname(__file__)
other_py_path = os.path.join(dir, "example.py")
print(other_py_path)

# 文件的大小-字节数
print(os.path.getsize(other_py_path))

# 获取文件相关的时间
print(os.path.getctime(other_py_path))
print(os.path.getmtime(other_py_path))

print(int(os.path.getmtime(other_py_path)) - int(os.path.getctime(other_py_path)))

print(os.path.getatime(other_py_path))