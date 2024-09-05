# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      login_func_page.py
# Author:       lao_zhao
# Datetime:     2024/8/13 16:54
# Description:
# 
# ---------------------------------------------------------------------------
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginFunc:
    def __init__(self, browser="c"):
        """启动浏览器，访问被测系统"""
        # 将browser的值转成小写
        browser = browser.lower()
        # 判断browser的值为c启动谷歌浏览器
        if browser == "c":
            self.driver = webdriver.Chrome()
        # 判断browser的值为e启动微软自带的浏览器
        elif browser == "e":
            self.driver = webdriver.Edge()
        # 判断browser的值为f启动火狐浏览器
        elif browser == "f":
            pass
        else:
            raise ValueError("传入的浏览器名称错误")

        # self.driver.maximize_window()
        # 访问被测系统
        self.driver.get("http://36.139.193.99:8280/mvue/login")

    def login_func(self, username, password):
        """登录功能"""
        self.driver.find_element(By.CSS_SELECTOR, '[type="text"]').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, '[type="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[text()="登录"]').click()
        time.sleep(2)
        return self.driver.page_source