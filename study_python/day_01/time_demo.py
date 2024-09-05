# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      time_demo.py
# Author:       lao_zhao
# Datetime:     2024/8/7 10:14
# Description:
# 
# ---------------------------------------------------------------------------
import time
import datetime

"""
    睡眠n：time.sleep(n)
    纪元时间--时间戳：time.time()
    时间元组：time.localtime([时间戳])
            注意：如果time.localtime()没有指定时间戳，就是获取当前系统的时间元组，如果指定时间戳，就获取的是时间戳的时间元组
            
    英文格式时间：time.asctime()
    格林威治时间：time.gmtime()
"""
"""
    时间的转换：
        纪元时间转时间元组：time.localtime([时间戳])
        时间元组转纪元时间: time.mktime(时间元组)
        
        时间元组进行字符串的格式化：time.strftime("时间显示的格式"[, 时间元组])
                # : %Y: 年 
                    %m: 月
                    %d: 日
                    %H: 小时
                    %M: 分
                    %S: 秒
        讲字符串格式的时间转时间元组：time.strptime("字符串格式的时间", "时间显示的格式")
"""
# datetime
"""
    now = datetime.datetime.now(): 获取当前系统的时间
    now.strftime("时间显示的格式"): 对datetime.datetime类型进行字符串的格式化
    datetime.datetime.strptime("字符串格式的时间", "时间显示的格式"): 将字符串格式的时间转成datetime.datetime
"""


'''
print(time.time(), type(time.time()), int(time.time()))


res = time.localtime()
print(res.tm_yday)
print(res.tm_wday)


i = 1622997094

res1 = time.localtime(i)
print(res1)

print(time.asctime())  # xxxx年xx月xx日 xx:xx:xx
print(time.gmtime())
'''


'''
time_tu = time.localtime()
print(time_tu)

time_num = time.mktime(time_tu)
print(time_num)

# 1722997550
i = 1722997550
res = time.localtime(i)
print(res)


result = time.strftime("%Y年%m月%d天 %H:%M:%S", res)
print(result, type(result))

time.sleep(2)
# 2024年08月07天 10:30:58

time_str = "2024/08/07 10:25:50"

res = time.strptime(time_str, "%Y/%m/%d %H:%M:%S")
print(res)
print(time.mktime(res))
'''

# datetime

# 获取当前时间
now = datetime.datetime.now()
print(now)

res = now.strftime("%Y-%m-%d %H:%M:%S")
print(res)

# time
"""
time_res = time.strptime(res, "%Y-%m-%d %H:%M:%S")
print(time_res)
print(time.mktime(time_res))
"""

t1 = "2024-08-07 11:33:49"
t2 = "2024-08-07 11:13:49"

res1 = datetime.datetime.strptime(t1, "%Y-%m-%d %H:%M:%S")
print(res1, type(res1))

res2 = datetime.datetime.strptime(t2, "%Y-%m-%d %H:%M:%S")
print(res2, type(res2))

print(res1 - res2)


result1 = time.strptime(t1, "%Y-%m-%d %H:%M:%S")
result2 = time.strptime(t2, "%Y-%m-%d %H:%M:%S")
result_1 = time.mktime(result1)
result_2 = time.mktime(result2)
print(result_1 - result_2)