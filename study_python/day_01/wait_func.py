# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      wait_func.py
# Author:       lao_zhao
# Datetime:     2024/8/14 14:25
# Description:
# 
# ---------------------------------------------------------------------------
import os
import random
import string
import time

from faker import Faker
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""
    selenium中的三种等待方式：
        1：强制等待，time.sleep(n)
        2：隐式等待：implicitly_wait(n)：相当于全局的等待时间，每个元素定位时都会使用隐式等待的时间。
        3：显示等待：explicit_wait: 为每个元素设置等待的时间。
            WebDriverWait(浏览器对象, 总共等待的时长, 查询元素的间隔时间=0.5).until(expected_conditions.presence_of_element_located((By.定位方式, '定位的值')))
                显示等待到元素出现为止，返回值为WebElement类型。
                
            WebDriverWait(浏览器对象, 总共等待的时长, 查询元素的间隔时间=0.5).until(expected_conditions.presence_of_all_elements_located((By.定位方式, '定位的值')))
                显示等待到一组相同定位值的元素出现为止，返回值为列表，列表中的每个元素的类型为WebElement类型。
                
            WebDriverWait(浏览器对象, 总共等待的时长, 查询元素的间隔时间=0.5).until(expected_conditions.element_to_be_clickable((By.定位方式, '定位的值')))
                显示等待到元素可点击为止，返回值为WebElement类型。
            
            注意：显式等待和隐式不能混用。

"""


os.popen(r'"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=8089 --user-data-dir="D:\seleniumChromeData"')
# result = os.popen('netstat -ano|findstr "8089"').read()
# if not result.strip():
    # os.popen(r'"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=8089 --user-data-dir="D:\seleniumChromeData"')

driver_options = webdriver.ChromeOptions()
driver_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
driver_options.add_experimental_option("debuggerAddress", '127.0.0.1:8089')

driver = webdriver.Chrome(service=webdriver.ChromeService("../chromedriver.exe"), options=driver_options)


driver.maximize_window()
driver.get("http://36.139.193.99:8280/mvue/login")

# 设置隐式等待的时间为30s，相当于全局的等待时间，每个元素定位时都会使用隐式等待的时间。
driver.implicitly_wait(30)

WebDriverWait(driver, 5, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[type="text"]'))).send_keys("admin")
WebDriverWait(driver, 5, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[type="password"]'))).send_keys("123456")
WebDriverWait(driver, 5, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="登录"]'))).click()
WebDriverWait(driver, 5, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="用户中心"]'))).click()
WebDriverWait(driver, 5, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="组织管理"]'))).click()
WebDriverWait(driver, 5, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="请输入"]'))).click()
element = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul[class="el-scrollbar__view el-select-dropdown__list"]>li')))[14]

driver.execute_script("arguments[0].scrollIntoView();", element)
time.sleep(1)
element.click()

data = Faker(locale="zh_cn")
action = ActionChains(driver)


for _ in range(10):
    action.move_by_offset(436, 204).click().perform()
    time.sleep(1)
    action.reset_actions()

    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, '//*[text()="添加子组织" and @class="el-dropdown-menu__item"]')))[-1].click()

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[placeholder="请输入组织名称"]'))).send_keys(data.company())

    code = "".join(random.sample(string.ascii_letters, 16))

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[placeholder="请输入组织编码"]'))).send_keys(code)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="保存"]'))).click()