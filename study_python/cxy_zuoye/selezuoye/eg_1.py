# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      eg_1.py
# Author:       lao_zhao
# Datetime:     2024/8/13 9:44
# Description:
# 
# ---------------------------------------------------------------------------
import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=webdriver.ChromeService("../../chromedriver.exe"))
driver.maximize_window()

driver.get("http://47.109.99.224:8090/korei/login.jsp")

driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("1")
driver.find_element(By.TAG_NAME, 'a').click()

driver.find_element(By.XPATH, '//*[text()="系统管理"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[text()="门店管理"]').click()
time.sleep(1)


for _ in range(10):
    driver.switch_to.frame("mdgl")
    # 创建一个集合存储所有的数据
    data_set = set()
    # 获取所有的行
    trs = driver.find_elements(By.XPATH, '//*[@id="storeItem"]//tbody/tr')
    # 循环所有的行
    for tr in trs:
        # 获取每行中的格子td
        tds = tr.find_elements(By.TAG_NAME, "td")
        # 创建一个列表存储每行每个格子中的数据
        row_set = set()
        # 循环所有的格子
        for td in tds[1:4]:
            row_set.add(td.text)
        # 将集合的元素添加到前面的大集合中
        data_set.update(row_set)

    # 随机获取一行
    random_tr = random.choice(trs)
    # 获取这行下的td
    tds = random_tr.find_elements(By.TAG_NAME, "td")
    # 获取最后一个td
    last_td = tds[-1]
    # 获取最后一个td下的第二个a标签
    last_td.find_elements(By.TAG_NAME, "a")[1].click()

    # 定义iframe
    iframe = driver.find_element(By.CSS_SELECTOR, '[src^="/korei/korei/store/edit.ht"]')
    # 再次进入iframe
    driver.switch_to.frame(iframe)
    # store_name  store_addr  store_phone
    store_phone = "138" + "".join(random.sample(string.digits, 8))

    phone_ele = driver.find_element(By.ID, 'phone')
    # 清空原有的手机号
    phone_ele.clear()

    # 判断手机号是否再集合中
    if store_phone in data_set:
        store_phone = "158" + "".join(random.sample(string.digits, 8))

    # 从新输入手机号
    phone_ele.send_keys(store_phone)

    # 回到父级页面
    driver.switch_to.parent_frame()
    # 定位确定
    driver.find_element(By.XPATH, '//*[@class="l-dialog-btn-inner" and text()="确定"]').click()

    # 定义iframe
    iframe = driver.find_element(By.CSS_SELECTOR, '[id^="ligerwindow"]')
    # 再次进入iframe
    driver.switch_to.frame(iframe)
    time.sleep(2)
    # 定位确定
    driver.find_element(By.XPATH, '//div[@class="l-dialog"]/table[@class="l-dialog-table"]//div[text()="确定"]').click()
    # 回到父页面
    driver.switch_to.default_content()


time.sleep(111)