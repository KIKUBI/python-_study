# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      utils.py
# Author:       lao_zhao
# Datetime:     2024/8/6 17:25
# Description:
# 
# ---------------------------------------------------------------------------
import os

list_path = []  # 存放所有的文件

def get_files(path):
    """
    获取路径下所有的文件
    :param path: 字符串形式的路径
    :return: None
    """
    # 判断路径是否为文件
    if os.path.isfile(path):
        list_path.append(path)
    # 判断路径是否为目录
    elif os.path.isdir(path):
        # 获取目录下所有的文件，返回值为列表
        files = os.listdir(path)
        # 循环列表中所有的元素
        for file in files:
            # 文件名称和目录的路径进行拼接
            file_path = os.path.join(path, file)
            # 调用函数本身对象路径进行操作
            get_files(file_path)


# 类
class Utils:
    list_path = []

    def get_files(self, path):
        """
        获取路径下所有的文件
        :param path: 字符串形式的路径
        :return: None
        """
        # 判断路径是否为文件
        if os.path.isfile(path):
            self.list_path.append(path)
        # 判断路径是否为目录
        elif os.path.isdir(path):
            # 获取目录下所有的文件，返回值为列表
            files = os.listdir(path)
            # 循环列表中所有的元素
            for file in files:
                # 文件名称和目录的路径进行拼接
                file_path = os.path.join(path, file)
                # 调用函数本身对象路径进行操作
                self.get_files(file_path)