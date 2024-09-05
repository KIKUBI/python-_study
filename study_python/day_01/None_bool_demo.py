# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      None_bool_demo.py
# Author:       lao_zhao
# Datetime:     2024/7/29 11:30
# Description:
# 
# ---------------------------------------------------------------------------

"""
    在python中使用None表示空(null, nil)

"""
# i1 = None
# i2 = None
# print(i1 == i2)
# print(i2 is i1)


"""
    python中使用bool类型来表示真(True)和假(False).
    注意：
        数值类型中，非0为True，0为False。
        None在做判断时，None为False
        字符串、列表、元组、字典、集合：非空为True, 空为False。
"""


'''
i = 0.0
if i:
    print("i的值不为0")
else:
    print("i的值为0")
'''

'''
i = None
if i:
    print("i的值不为None")
else:
    print("i的值为None")
'''

'''
s1 = " "
l1 = [1]
t1 = (1,)
d1 = {1: 10}
s_1 = {1}

if s_1:
    print("不为空")
else:
    print("为空")
'''


b1 = True  # 做数学元素 True为1， False为0
b2 = False

print(b1 + 1)
print(b2 + 10)