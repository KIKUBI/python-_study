# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      iframe_func.py
# Author:       lao_zhao
# Datetime:     2024/8/12 16:07
# Description:
# 
# ---------------------------------------------------------------------------
import time

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=webdriver.ChromeService("../../chromedriver.exe"))
driver.maximize_window()
driver.get("http://47.109.99.224:8090/korei/login.jsp")
driver.find_element(By.NAME, 'username').send_keys("admin")
driver.find_element(By.NAME, 'password').send_keys("1")
driver.find_element(By.TAG_NAME, 'a').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[text()="系统管理"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[text()="门店管理"]').click()


data = Faker(locale="zh_cn")

for i in range(10):
    # 进入嵌套的网页
    driver.switch_to.frame("mdgl")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[text()="添加"]').click()

    # 定位点击添加之后弹窗的嵌套网页
    other_html = driver.find_element(By.CSS_SELECTOR, '[src^="/korei/korei/store/edit.ht"]')
    # 再次进入到嵌套的网页中
    driver.switch_to.frame(other_html)
    time.sleep(2)
    # 定义添加门店的信息标签
    driver.find_element(By.ID, 'name').send_keys(f"{data.company()[:10]}")
    driver.find_element(By.ID, 'address').send_keys(f"{data.address()[:10]}")
    driver.find_element(By.ID, 'phone').send_keys(f"{data.phone_number()}")
    # 回到父级的iframe标签
    driver.switch_to.parent_frame()
    driver.find_element(By.XPATH, '//*[text()="确定"]').click()

    # 再次进入嵌套的iframe标签
    other_html1 = driver.find_element(By.CSS_SELECTOR, '[src^="/korei/korei/store/edit.ht"]')
    driver.switch_to.frame(other_html)
    time.sleep(0.5)
    driver.find_element(By.XPATH,
                        '//div[@class="l-dialog"]//div[text()="确定" and @class="l-dialog-btn-inner"]').click()

    # 回到主页面
    driver.switch_to.default_content()
time.sleep(111)