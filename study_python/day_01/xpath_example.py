# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      xpath_example.py
# Author:       lao_zhao
# Datetime:     2024/8/12 11:07
# Description:
# 
# ---------------------------------------------------------------------------
import random
import string
import time

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

# 启动浏览器
driver = webdriver.Chrome(service=webdriver.ChromeService("../chromedriver.exe"))
# 浏览器窗口最大化
driver.maximize_window()
# 访问被测系统
driver.get("http://36.139.193.99:8280/mvue/login")
# 登录
# 定位用户名
driver.find_element(By.XPATH, '//input[@type="text"]').send_keys("admin")
# 定位密码
driver.find_element(By.XPATH, '//input[@type="password"]').send_keys("123456")
# 定位登录按钮
driver.find_element(By.XPATH, '//span[text()="登录"]').click()
# 强制让程序慢下来
time.sleep(2)
# 用户中心
driver.find_element(By.XPATH, '//*[text()="用户中心"]').click()
time.sleep(2)
# 组织管理
driver.find_element(By.XPATH, '//*[text()="组织管理"]').click()
time.sleep(2)

data = Faker(locale="zh_cn")

for i in range(10):
    # 维度管理
    driver.find_element(By.XPATH, '//*[contains(text(), "维度管理")]').click()
    time.sleep(2)

    # 添加
    driver.find_element(By.XPATH, '//*[text()="添加"]').click()
    time.sleep(2)
    #
    driver.find_element(By.XPATH, '//*[@placeholder="请输入名称"]').send_keys(data.company())
    driver.find_element(By.XPATH, '//*[@placeholder="请输入别名"]').send_keys("".join(random.sample(string.ascii_letters+string.digits, 16)))
    driver.find_element(By.XPATH, '//*[@placeholder="请输入描述"]').send_keys(f"测试添加的维度")
    driver.find_element(By.XPATH, '//*[text()="保存"]').click()

time.sleep(111)