# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      lambda_function.py
# Author:       lao_zhao
# Datetime:     2024/8/1 10:18
# Description:
# 
# ---------------------------------------------------------------------------



def demo():
    print("demo函数")


demo()

print(demo)


a = demo  # 函数的重命名

demo()
a()

# 匿名函数---没有名称的函数
# lambda函数
# 格式：
# lambda 形参: 形参操作

x = (lambda x: x+1)(10)
print(x)


# 结果1 if bool表达式 else 结果2
func1 = lambda x, y: y - x if y > x else x - y

result = func1(10,1)
print(result)


def func1(x, y):
    if y > x:
        # return y - x
        print("hello")
    else:
        # return x -y
        print("python")


func1(10, 1)