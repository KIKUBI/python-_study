# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      execute_js.py
# Author:       lao_zhao
# Datetime:     2024/8/12 17:15
# Description:
# 
# ---------------------------------------------------------------------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=webdriver.ChromeService("../../chromedriver.exe"))
driver.maximize_window()
'''
driver.get("http://www.jd.com")

# 定位为你推荐
element = driver.find_element(By.ID, 'J_feeds')
# 让浏览器页面滚动到为你推荐
js = "arguments[0].scrollIntoView();"
# 浏览器对象执行js
driver.execute_script(js, element)
time.sleep(15)

driver.find_element(By.XPATH, '//*[@class="feed-tab__item-title-text" and text()="进口好物"]').click()
'''

driver.get("https://www.baidu.com")
driver.find_element(By.ID, 'kw').send_keys("python")
driver.find_element(By.ID, 'su').click()

time.sleep(2)

next_page = driver.find_element(By.XPATH, '//*[text()="下一页 >"]')
# js = "arguments[0].scrollIntoView();"
# driver.execute_script(js, next_page)

time.sleep(2)
next_page.click()
time.sleep(111)