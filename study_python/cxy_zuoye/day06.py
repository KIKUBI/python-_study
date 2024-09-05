# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   RONGHUA
# FileName:      day06.py
# Author:       陈啸宇
# Datetime:     2024/8/6 16:05
# Description:
# ---------------------------------------------------------------------------
import random
from faker import Faker
class dizhi:
    def __init__(self):
        self.data = Faker(locale="zh_CN")
        self.c = [chr(i) for i in range(65,91)]     # 大写字母 A 到 Z
        self.C = [chr(i) for i in range(97,123)]    # 小写字母 a 到 z
    def addr(self,m,n):
        for j in range(m):
            list1 = list(self.data.address())
            for i in range(len(list1)):
                if list1[i] in self.c or list1[i] in self.C:
                    list1[i] = str(random.randint(1,n))
            self.address = ''.join(list1[0:list1.index('座')+1])
            self.address = self.address.replace(self.address[-1],'栋')
            print(self.address)

cxy = dizhi()
cxy.addr(10,11)