# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      re_demo.py
# Author:       lao_zhao
# Datetime:     2024/8/29 15:20
# Description:
# 
# ---------------------------------------------------------------------------
import re
from decimal import Decimal

"""
    正则表达式：
        .: 匹配任意的一个字符，除了换行符
        |: 或者
        \: 转义符
        []: 字符集
        \d: 匹配任意一个数字
        \D: 匹配任意一个非数字
        \s: 匹配任意一个空白字符
        \S: 匹配任意一个非空白字符
        \w: 匹配任意一个单词字符
        \W: 匹配任意一个非单词字符
        {n}: 前面一个字符匹配n次
        {n,m}: 前面一个字符匹配n次到m次
        {n,}: 前面一个字符匹配n次到多次
        *: 前面一个字符匹配0次到多次
        +: 前面一个字符匹配1次到多次
        ?: 在字符后-->前面一个字符匹配0次到1次
           在次数后-->关闭正则表达式的贪婪模式
        (): 如果正则表达式中存在小括号，表示子正则表达式，子正则表达式的两边需要指定左右边界。最后会返回子正则表达式的匹配结果
        ^: 单独使用表达式非，和$结合使用表示开始符
        $: 结束符
"""

"""
    re.findall("正则表达式", 字符串)：以正则表达式匹配字符串，将匹配的结果以列表的形式返回。
    re.split("正则表达式", 字符串): 以正则表达式分割字符串，将分割后的结果以列表的形式返回。
    re.sub("正则表达式", 新的字符, 字符串[, 次数])：以正则表达式匹配字符串将匹配到的结果替换为新的字符串, 也可以指定替换的次数。
        特点：re.sub("正则表达式", 新的字符, 字符串)：如果正则表达式中存在子正则表达式，可以在替换的新字符中可以使用子正则表达式匹配的内容，格式为\n--n表示第几个字正则表达式
        
    re.match("正则表达式", 字符串): 以正则表达式匹配字符串的开始，如果能匹配到，返回Match对象，如果匹配不到返回None, 只匹配一次。
    re.search("正则表达式", 字符串): 以正则表达式匹配字符串, 如果能匹配到，将返回匹配到的第一个结果，返回Match对象，如果匹配不到结果返回None。
    re.fullmatch("正则表达式", 字符串): 以正则表达式完整匹配字符串，如果能匹配上返回Match对象，如果不能完全匹配返回None。
    
    re.compile("正则表达式"): 返回正则表达式的正则对象。正则对象中有findall等方法。
"""
"""
    Match对象的操作：
        group([n]): 默认获取整个的匹配结果，如果指定n，表示获取第n个子正则表达式的匹配结果
        groups(): 获取所有的子正则表达式的匹配结果，返回值为元组
        span([n]): 默认获取整个的匹配结果在字符串中的下标位置，可以指定n，表示获取第n个子正则表达式匹配结果在字符串中的下标位置。
"""



str1 = "hel1.lo pyt-3h3.112313on成都-100"

res = re.findall(r"-?\d+\.?\d*", str1)
print(res)
'''
sum1 = 0
for i in res:
    if i.endswith("."):
        i = i.strip(".")

    # Decimal("3.11") - Decimal("1.5")
    sum1 = Decimal(str(sum1)) + Decimal(str(float(i)))

print(sum1)

print(3.11-1.5)
print(Decimal("3.11") - Decimal("1.5"))
'''

'''
str1 = "hel1.lo pyt-3h3.11中国2313on成都-100"
res = re.split(r"[a-zA-Z成都中国\s]", str1)
print(res)

sum2 = 0
for i in res:
    if i.endswith("."):
        i = i.strip(".")
    elif i == "":
        continue

    sum2 = Decimal(str(sum2)) + Decimal(i)

print(sum2)
'''


str1 = "hel1.l-op-yt3h3.11中国2313on"


re_obj = re.compile(r"\w+\.[a-zA-Z0-9\.-]+(.{2})(\w+)")

res = re_obj.fullmatch(str1)
print(res)

# res1 = re.fullmatch(r"\w+\.[a-zA-Z0-9\.-]+(.{2})(\w+)", str1)
# print(res1)
# print(res1.group(1))
# print(res1.groups())
# print(res1.span(2))


# res1 = re.search(r"\s", str1)
# print(res1)

# res1 = re.match(r"\w+", str1)
# print(res1)


str2 = "13812340000"
res = re.sub(r"(\d{3})(\d{4})(\d{4})", r"\1****\3", str2)
print(res)