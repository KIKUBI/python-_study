# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   RONGHUA
# FileName:      study_python.py
# Author:       陈啸宇
# Datetime:     2024/7/22 15:18
# Description:
# ---------------------------------------------------------------------------
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listx = []

for j in range(1, len(liste) + 1):
    i = liste[j-1]
    if i % 2 == 0:
        s1 = liste.pop(j-1)  # 弹出索引为 j-1 的元素
        listx.append(s1)
print(listx)
