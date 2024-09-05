# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      upload_file.py
# Author:       lao_zhao
# Datetime:     2024/8/14 14:02
# Description:
# 
# ---------------------------------------------------------------------------
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

"""
    上传文件时，一定是input标签type属性为file时，直接send_keys一个文件的路径，就能实现上传文件。
    
    下拉框的处理： 
        Select(select标签的定位)
                select_by_index(option元素的编号)：根据option的编号进行选择
                select_by_value(option的value属性)：根据option的value属性进行选择
                select_by_visible_text(option的文本值)：根据option的文本值进行选择
"""

result = os.popen('netstat -ano|findstr "8089"').read()
if not result.strip():
    os.popen(r'"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=8089 --user-data-dir="D:\seleniumChromeData"')

driver_options = webdriver.ChromeOptions()
driver_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
driver_options.add_experimental_option("debuggerAddress", '127.0.0.1:8089')

driver = webdriver.Chrome(service=webdriver.ChromeService("../chromedriver.exe"), options=driver_options)

driver.maximize_window()
r'''
driver.get("http://36.139.193.99:8280/mvue/login")

driver.find_element(By.CSS_SELECTOR, '[type="text"]').send_keys("admin")
driver.find_element(By.CSS_SELECTOR, '[type="password"]').send_keys("123456")
driver.find_element(By.XPATH, '//*[text()="登录"]').click()
time.sleep(1)

driver.find_element(By.XPATH, '//*[text()="用户中心"]').click()
time.sleep(1)

driver.find_element(By.XPATH, '//*[text()="用户管理"]').click()
time.sleep(1)

driver.find_elements(By.XPATH, '//*[contains(text(),"编辑")]')[1].click()

time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '[type="file"]').send_keys(r"D:\Project\PythonDoc\test62\test62\study_selenium\day_04\1.png")
'''

url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'

driver.get(url)

element = driver.find_element(By.ID, 'cc_start_time')

Select(element).select_by_index(2)
time.sleep(2)
Select(element).select_by_value("18002400")
time.sleep(2)
Select(element).select_by_visible_text("00:00--24:00")
