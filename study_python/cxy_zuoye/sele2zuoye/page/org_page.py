# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      org_page.py
# Author:       lao_zhao
# Datetime:     2024/8/14 16:17
# Description:
# 
# ---------------------------------------------------------------------------
import random
import time

from faker import Faker
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

from study_python.cxy_zuoye.sele2zuoye.common.read_png import ReadPng
from study_python.cxy_zuoye.sele2zuoye.page.login_page import LoginPage


class OrgPage(LoginPage):
    def __init__(self, browser="c"):
        super().__init__(browser=browser)
        self.login_func("admin", "123456")

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="用户中心"]'))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="组织管理"]'))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="el-link--inner" and starts-with(text(), "组织管理")]'))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[placeholder="请输入"]'))).click()

        dems = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul[class="el-scrollbar__view el-select-dropdown__list"] > li')))
        element = random.choice(dems)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        element.click()

        self.action = ActionChains(self.driver)
        self.readpng = ReadPng()
    def add_org(self, org_name, org_code,i):
        self.action.move_by_offset(436, 204).perform()
        time.sleep(1)
        self.action.reset_actions()
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="el-dropdown-menu__item" and text()="添加子组织"]')))[-1].click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[placeholder="请输入组织名称"]'))).send_keys(org_name)
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[placeholder="请输入组织编码"]'))).send_keys(Keys.LEFT_CONTROL+"a")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[placeholder="请输入组织编码"]'))).send_keys(Keys.LEFT_CONTROL+"x")
        # WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[placeholder="请输入组织编码"]'))).clear()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[placeholder="请输入组织编码"]'))).send_keys(org_code)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="保存"]'))).click()
        content = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="el-message__content"]'))).text
        # 截图
        self.driver.get_screenshot_as_file(f'{self.readpng.read_png()}/org{i}.png')
        print(self.readpng.read_png())
        return content
    def quitweb(self):
        self.driver.close()


if __name__ == '__main__':
    org = OrgPage()
    data = Faker(locale="zh_cn")
    for _ in range(10):
        text = org.add_org(data.company(), "")
        print(text)
