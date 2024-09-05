# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      demo.py
# Author:       lao_zhao
# Datetime:     2024/8/7 18:37
# Description:
# 
# ---------------------------------------------------------------------------


def demo():
    # yield 1
    # yield 2
    # yield 3
    # yield 4
    # yield 5
    # for i in range(1, 6):
    #     yield i
    # i = 1
    # while i < 6:
    #     yield i
    #     i += 1

    f = open("./file/4.txt", mode="r", encoding="utf-8")
    while True:
        content = f.read(2)
        if len(content) == 0:
            break
        yield content


d = demo()
# print(d.__next__())
# print(d.__next__())
# print(d.__next__())
# print(d.__next__())
# print(d.__next__())
f1 = open("./file/5.txt", mode="w", encoding="utf-8")
for i in d:
    f1.write(i)