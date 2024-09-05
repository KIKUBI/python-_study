# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      read_ini.py
# Author:       lao_zhao
# Datetime:     2024/8/14 15:27
# Description:
# 
# ---------------------------------------------------------------------------
# 读取ini配置文件
import configparser
import os


class ReadIni:
    def __init__(self):
        """动态获取ini文件的路径，创建Configparser对象，使用Configparser对象的read方法读取ini文件"""
        # 1 动态获取ini文件的路径
        # 1.1 获取当前py文件的路径
        py_path = __file__
        # 1.2 获取当前py文件的目录的路径
        py_dir = os.path.dirname(py_path)
        # 1.3 获取当前py文件的目录的的目录路径
        py_dirs = os.path.dirname(py_dir)
        # 1.4 获取config_data目录路径
        self.config_data_path = os.path.join(py_dirs, "config_data")
        # 1.5 获取ini文件路径
        ini_path = os.path.join(self.config_data_path, "config.ini")
        # 2 创建Configparser对象
        self.conf = configparser.ConfigParser()
        # 3 使用Configparser对象的read方法读取ini文件
        self.conf.read(ini_path, encoding="utf-8")

    def get_file_path(self, key):
        """根据key获取file节点下的文件名称，并获取文件对应的路径"""
        # 使用Configparser对象的get方法获取file节点下key对应的文件名
        file_name = self.conf.get("file", key)
        # 文件名和config_data的目录路径拼接获取文件的路径
        return os.path.join(self.config_data_path, file_name)

    def get_table_name(self, key):
        """根据key，获取table节点下，key对应的工作表名称"""
        return self.conf.get("table", key)

    def get_sql_connect_msg(self, key):
        """根据key，获取sql节点下，key对应的数据库链接信息"""
        return self.conf.get("sql", key)
    def get_png_path(self, key):
        """根据key，获取png节点下，key对应的图片路径"""
        return self.conf.get("png", key)