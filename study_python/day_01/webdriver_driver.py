# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      webdriver_driver.py
# Author:       lao_zhao
# Datetime:     2024/8/14 9:48
# Description:
# 
# ---------------------------------------------------------------------------
import os
import time

from selenium import webdriver

"""

    os.popen(终端名称[, mode="r"]): 执行终端名称，返回一个文件对象，文件对象的模式为r。

"""

# chrome
'''
# # os.system('"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=8089 --user-data-dir="D:\seleniumChromeData"')
os.popen('"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=8089 --user-data-dir="D:\seleniumChromeData"')

# 设置启动浏览器服务器的选型
options = webdriver.ChromeOptions()
# 设置启动浏览器的路径
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# 设置浏览器服务器对应的ip和端口
options.add_experimental_option("debuggerAddress", "127.0.0.1:8089")

# 默认启动的测试相关的浏览器服务
driver = webdriver.Chrome(service=webdriver.ChromeService("../chromedriver.exe"), options=options)
driver.maximize_window()
driver.get("http://36.139.193.99:8280/mvue/login")

time.sleep(5)
'''
'''
# os.system("ipconfig")
# print(res)
# res = os.popen("ipconfig").read()
# with open("1.txt", mode="w", encoding="utf-8") as f:
#     f.write(res)

res = os.popen('netstat -ano|findstr "8089"').read()
# print(res.split(" "), type(res))
# print([res.split(" ")[-1]], type(res))
# print([res.split(" ")[-1].strip()], type(res))

str_pid = res.split(" ")[-1].strip()
print(str_pid)


# os.popen(r'taskkill /f /pid '+str_pid)
os.popen(r'taskkill /f /im chrome.exe')
'''

# edge
'''
os.popen(r'"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=8099 --user-data-dir="D:\seleniumEdgeData')

options = webdriver.EdgeOptions()
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
options.add_experimental_option("debuggerAddress", "127.0.0.1:8099")

driver = webdriver.Edge(service=webdriver.EdgeService("../msedgedriver.exe"), options=options)
driver.maximize_window()
driver.get("https://www.baidu.com")
'''