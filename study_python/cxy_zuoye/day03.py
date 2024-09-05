# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   RONGHUA
# FileName:      day03.py
# Author:       陈啸宇
# Datetime:     2024/7/30 18:54
# Description:
# ---------------------------------------------------------------------------

while True:
    score = input("请输入一个分数：").strip()
    if score.count('.') == 1 or score.count('.') == 0:
        score1 = ''.join(score.split('.'))
        if score1.isdigit() :
            score2 = float(score)
            if score2 <= 100 and score2 >=0:
                if score2 >= 90:
                    print("A",score2)
                elif score2 >= 60 and score2 <= 89:
                    print("B")
                else:
                    print("C")
            else:
                print('请输入0-100之间的数字')
        elif score1 == 'q':
            break
        else:
            print("请输入正确的数字!")
#三角掏空
def cxysanjiao(aa,bb):
    for i in range(aa,bb+1):
        for j in range(bb-i):
            print(' ',end='')
        for s in range(1,2*i):
            if s == 1 or s == 2*i-1:
                print('*',end='')
            else:
                print(' ',end='')
        print()
    for z in range(aa,bb+1):
        for c in range(z-1):
            print(' ',end='')
        for x in range(1,(aa+2*bb)-2*z+1):
            if x ==1  or x == (aa+2*bb)-2*z:
                print('*',end='')
            else:
                print(' ',end='')
        print()
cxysanjiao(1,5)
#兔子序列
# “兔子数列”，指的是这样一个数列：1、1、2、3、5、8、13、21、34、……在数学上
raby = [1,1]
for g in range(2,12):
    raby.append(raby[g-1]+raby[g-2])
print(raby[g])