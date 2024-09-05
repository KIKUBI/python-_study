# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      random_demo.py
# Author:       lao_zhao
# Datetime:     2024/8/6 15:20
# Description:
# 
# ---------------------------------------------------------------------------
import random


"""
    random--伪随机
    
        random.randrange(初始值, 结束值, 步长)：随机获取初始值到结束值之间根据步长的一个随机数
        random.randint(初始值, 结束值):随机获取初始值到结束值之间随机数
        random.sample(有序的可迭代类型, k=number): 随机从可迭代类型中取k个元素，k必须小于可迭代类型的长度，返回列表
        random.choice(有序的可迭代类型): 随机从有序的可迭代类型中取一个元素
"""

print(random.randrange(10))
print(random.randint(1, 10))

# for _ in range(100):
#     phone_number = "1" + str(random.randint(3, 9)) + str(random.randint(100000000, 999999999))
#     print(phone_number)

str1 = "随机获取初始值到结束值之间根据步长的一个随机数"
list1 = {1: 2, 5: 4, 100: 200, 4: 400}

# res = random.sample(list1.items(), 3)
# print(res)


dict1 = {2: "李四1", 1: "王五", 3: "王五2", 4: "王五4"}

# print(random.choice(list1))
name = dict1[random.choice(list(dict1.keys()))]
print(name)


s1 = {1, 2, 3, 4, 5}
print(random.choice(s1))