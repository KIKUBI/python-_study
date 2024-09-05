# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      configparser_demo.py
# Author:       lao_zhao
# Datetime:     2024/8/9 14:00
# Description:
# 
# ---------------------------------------------------------------------------
import configparser

"""
    python中使用第三方模块configparser读取ini文件。pip install configparser

    ini文件是用来做配置文件使用。
    
    ini文件得读取：
        1: 先创建Configparser类对象。
        2: 使用Configparser类对象调用read方法读取ini文件
            read("ini文件的路径", encoding="utf-8"): 会返回读取成功文件的路径，将读取成功的ini文件的内容加载到Configparser类对象中
        3: 获取ini文件的内容。
            get("节点名称", "键")：获取节点下键对应的值，返回值内容为字符串。

"""

conf = configparser.ConfigParser()
res = conf.read("config.ini", encoding="utf-8")
print(res)

value = conf.get("节点名称", "键")
print([value])