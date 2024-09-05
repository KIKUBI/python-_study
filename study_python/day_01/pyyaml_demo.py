# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      pyyaml_demo.py
# Author:       lao_zhao
# Datetime:     2024/8/8 16:41
# Description:
# 
# ---------------------------------------------------------------------------
import yaml

"""
    python处理yaml文件，需要使用第三方模块pyyaml进行处理。pip install pyyaml

    yaml.load(yaml文件的文件对象, Loader=yaml.FullLoader): 将yaml文件的数据序列化为python的字典或列表
"""


with open("data.yaml", mode="r", encoding="utf-8") as f:
    data = yaml.load(f)

print(data, type(data))