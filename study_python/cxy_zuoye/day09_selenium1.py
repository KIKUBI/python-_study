# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   RONGHUA
# FileName:      day09_selenium1.py
# Author:       陈啸宇
# Datetime:     2024/8/12 17:36
# Description:
# ---------------------------------------------------------------------------
import time

import faker
from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)
driver.get("http://47.109.99.224:8090/korei/login.jsp")
driver.find_element(By.CSS_SELECTOR,'[type="text"]').send_keys("admin")
driver.find_element(By.CSS_SELECTOR,'[type="password"]').send_keys("1")
driver.find_element(By.CSS_SELECTOR,'a[class^="land_inputSite"]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[text()="系统管理"]').click()
time.sleep(0.5)
driver.find_element(By.XPATH,'//*[text()="门店管理"]').click()
time.sleep(0.5)
date = faker.Faker(locale="zh_CN")
for i in range(1,10):
    #进入1
    element1 = driver.find_element(By.XPATH, '//*[@id="mdgl"]')
    driver.switch_to.frame(element1)
    driver.find_element(By.XPATH,f'//*[@id="storeItem"]/tbody/tr[{i}]//*[text()="编辑"]').click()
    #进入2
    element2 = driver.find_element(By.CSS_SELECTOR, '[id^="ligerwindow"]')
    driver.switch_to.frame(element2)
    ix=driver.find_element(By.CSS_SELECTOR, '[id =name]')
    ix.clear()
    ix.send_keys(date.company()[:10])
    iz = driver.find_element(By.CSS_SELECTOR, '[id =address]')
    iz.clear()
    iz.send_keys(date.address()[:10])
    iy = driver.find_element(By.CSS_SELECTOR, '[id = phone]')
    iy.clear()
    iy.send_keys(date.phone_number())
    #退出到1
    driver.switch_to.parent_frame()
    driver.find_element(By.XPATH,'//*[@class="l-dialog-btn-inner" and text()="确定"]').click()
    time.sleep(0.5)
    #进入到2
    element3 = driver.find_element(By.CSS_SELECTOR,'[id^="ligerwindow"]')
    driver.switch_to.frame(element3)
    driver.find_element(By.XPATH,'//*[@class="l-dialog-btn-inner" and text()="确定"]').click()
    #退出到0
    driver.switch_to.default_content()
