# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   RONGHUA
# FileName:      day02.py
# Author:       陈啸宇
# Datetime:     2024/7/29 18:05
# Description:
# ---------------------------------------------------------------------------
# 1.输入一个字符串，输出不重复的字符？
#比如按输入：ababcd，输出：cd
str1 = list(input("请输入一个字符串："))
set1 = list(set(str1))
s1 = set1.copy()
for i in str1[:]:
    if i in s1:
        str1.remove(i)
        s1.remove(i)
print(''.join(sorted(''.join(set(set1)-set(str1)))))
# str1 = list(input("请输入一个字符串："))
# zzz = []
# for i in str1:
#     if str1.count(i)==1:
#         zzz.append(i)
# print(''.join(zzz))
# 2.将字符串 s = “ajldjlajfdljfddd”，去重并从小到大排序输出”adfjl”。
s = "ajldjlajfdljfddd"
set1 = set(s)
print(''.join(sorted(list(set1))))
# 3.strs = ["flower","flow","flight"]查找列表中各个字符串的相同部分
strs = ["flower","flow","flight"]
set1,set2,set3 = set(strs[0]),set(strs[1]),set(strs[2])
print(list(set1&set2&set3))
# 4.学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。使用if条件判断来表示。分数使用控制台输入
score = input("请输入一个分数：").strip()
if score.count('.') == 1:
    score1 = ''.join(score.split('.'))
    if score1.isdigit() :
        score2 = float(score)
        if score2 <= 100 and score2 >=0:
            if score2 >= 90:
                print("A")
            elif score2 >= 60 and score2 <= 89:
                print("B")
            else:
                print("C")
        else:
            print('请输入0-100之间的数字')
    else:
        print("请输入正确的数字!")