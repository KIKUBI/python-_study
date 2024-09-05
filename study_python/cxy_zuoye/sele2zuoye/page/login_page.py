# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      login_page.py
# Author:       lao_zhao
# Datetime:     2024/8/14 16:07
# Description:
# 
# ---------------------------------------------------------------------------
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

from study_python.cxy_zuoye.sele2zuoye.common.read_png import ReadPng
from study_python.cxy_zuoye.sele2zuoye.config_data.settings import *


class LoginPage:
    def __init__(self, browser="c"):
        self.readpngq = ReadPng()
        """启动浏览器"""
        self.browser = browser.lower()
        if self.browser == "c":
            os.popen(CHROME_POPEN)
            chrome_opt = webdriver.ChromeOptions()
            chrome_opt.binary_location = CHROME_DRIVER
            chrome_opt.add_experimental_option("debuggerAddress", "127.0.0.1:9099")
            self.driver = webdriver.Chrome(service=webdriver.ChromeService(CHROME_DRIVER_PATH), options=chrome_opt)
        else:
            os.popen(EDGE_POPEN)
            edge_opt = webdriver.EdgeOptions()
            edge_opt.binary_location = EDGE_DRIVER
            edge_opt.add_experimental_option("debuggerAddress", "127.0.0.1:9098")
            self.driver = webdriver.Edge(service=webdriver.EdgeService(EDGE_DRIVER_PATH), options=edge_opt)

        # self.driver.maximize_window()

        self.driver.get("http://36.139.193.99:8280/mvue/login")

    def login_func(self, username, password):
        # 使用显式等待
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[type="text"]'))).send_keys(username)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[type="password"]'))).send_keys(password)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="登录"]'))).click()
        return self.driver.get_screenshot_as_file(f'{self.readpngq.read_png()}/login.png')