# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      range_demo.py
# Author:       lao_zhao
# Datetime:     2024/7/29 14:01
# Description:
# 
# ---------------------------------------------------------------------------

"""
    range序列：range序列是一个不可变的序列，元素为整形，range序列中的元素是根据range序列的区间取确定的。


        range(结束值): 开始值(为0)到结束值-1之间根据步长(为1)取值。
        range(开始值, 结束值): 开始值到结束值-1之间根据步长(为1)取值。
        range(开始值, 结束值, 步长)：开始值到结束值-1之间根据步长取值。
            注意：步长为正整数，开始值需要小于结束值
                 步长为负整数，开始值需要大于结束值

"""

# print(list(range(1, 3, 1)))
#
# print(list(range(10)))   # range(0, 10, 1)
#
# print(list(range(1, 10)))
#
# str1 = "hello"
#
# print(list(range(len(str1))))

# number = range(1, -1, 1)
# print(list(number))

# number1 = range(10, 1, -1)
# print(list(number1))

nums = range(2, 101, 2)
print(list(nums))
print(sum(nums))
