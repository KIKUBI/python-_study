# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      while_demo.py
# Author:       lao_zhao
# Datetime:     2024/7/30 10:50
# Description:
# 
# ---------------------------------------------------------------------------

"""

    while循环：条件只要为True就会重复运行一段代码，一直运行到条件为False。

"""
# 格式：
"""

while bool表达式:
    循环体代码
    定义while循环的出口
else:
    else代码块  # while循环体中的代码执行时没有发生任何异常

"""
"""
    break：结束循环。循环后的else代码不执行
    continue：结束本次循环执行下次循环。循环后的else代码要执行
    pass: 占位符
"""

"""
i = 0
while i < 5:
    print("while循环体代码")
    i = i + 1  # i += 1  出口
"""
"""
str1 = "hello python"

i1 = 0
while i1 < len(str1):
    print(i1, str1[i1], i1-len(str1))
    # 逻辑判断
    if str1[i1] == " ":
        print(f"i1的值为{i1}，对应字符串的字符为空白字符")
    # 定义出口
    i1 += 1
"""
"""
# 求1-10的和
sum1 = 0
sum2 = 0

number1 = 1
while number1 < 11:
    # sum1 = sum1 + number1
    # 奇数和
    if number1 % 2 == 1:
        # number1的值为奇数
        sum1 = sum1 + number1
    else:
        sum2 = sum2 + number1
    number1 += 1  # number1 = number1 + 1

print(sum1)
print(sum2)
"""


'''
# dict1 = {}
strs = ""

res = input("请输入：")

if res.isdigit():
    # 循环取出所有的数字
    i = 0
    while i < len(res):
        # dict1[res[i]] = res.count(res[i])
        # 判断字符在字符串中的个数是否为1
        if res.count(res[i]) == 1:
            print(f"下标为{i},对应的数字为：{res[i]}, {res[i]}在字符串中有{res.count(res[i])}个")
            strs = strs + res[i]
        # 定义出口
        i += 1
else:
    print("请正确输入")

print(strs)
'''

'''
variable = 10
i = 1
while i < 5:
    print(f"i的值为：{i}")

    result = i / variable
    print(result)
    i += 1
    variable -= 5
else:
    print("while循环体代码正常执行完成")
'''

# break
'''
i = 1
while True:
    print(f"死循环----------{i}")

    if i == 100:
        # 结束循环
        break

    i += 1
else:
    print("else代码")
'''
# continue
'''
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # 结束本次循环执行下次循环
    print(f"i的值为{i}-----")
else:
    print("else代码块")
'''

# pass
'''
i = 0
while i < 5:
    i += 1
    pass


str1 = "hello"
print(str1.count("l"))
'''

# while循环嵌套while循环

i = 1
while i < 5:
    j = 1  # 如果在循环体中定义的变量，每次循环变量的值会重置
    while j < 3:
        print(f"i的值为{i}, j的值为：{j}")
        j += 1
    i += 1


list1 = ["h", "ab", "abc"]

i = 0
while i < len(list1):
    print(list1[i])
    j = 0
    while j < len(list1[i]):
        print(list1[i][j])
        j += 1
    i += 1


i = 1
while i < 10:  # 控制行数
    # print(f"i的值为：{i}=============================")
    j = 1
    while j <= i:   # 控制每行的输出内容
        # print(f"j的值为{j}")
        print(f"{j}+{i}={j+i}\t", end="")
        j += 1
    print()
    i += 1


# break continue
i = 1
while i < 5:
    j = 1
    while j < i:
        j += 1
        if j == 2:
            # break
            continue
        print(f"i的值为：{i}, j的值为：{j}")
    i += 1

print(i, j)