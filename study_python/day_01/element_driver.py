# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      element_driver.py
# Author:       lao_zhao
# Datetime:     2024/8/12 15:20
# Description:
# 
# ---------------------------------------------------------------------------
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
    浏览器的操作【WebDriver】：
        get("url"): 访问url
        find_element(By.定位方式, '定位的值')：定位页面中的元素/标签
        find_elements(By.定位方式, '定位的值'): 定位页面中有相同定位值的一组元素，返回值为列表，列表中的每个元素为WebElement类型。
        
        get_screenshot_as_file("png图片路径"): 浏览器的窗口界面截图
        
        maximize_window(): 浏览器的窗口最大化
        minimize_window(): 浏览器的窗口最小化

"""
"""
    元素的操作【WebElement】：
        send_keys("值")：给元素/标签输入的值
        click(): 点击元素
        text: 获取标签的文本
        get_attribute("属性名")：获取元素属性的值
        clear(): 清空输入框中的内容
        is_enable(): 如果元素可点击返回True，反之返回False。
        
        
        find_element(By.定位方式, '定位的值'): 【元素的二次定位】定位页面中的元素/标签，元素使用find_element再次定义元素是，定位的值一定是任意节点
        find_elements(By.定位方式, '定位的值'): 【元素的二次定位】定位页面中有相同定位值的一组元素，返回值为列表，列表中的每个元素为WebElement类型。
"""


driver = webdriver.Chrome(service=webdriver.ChromeService("../chromedriver.exe"))

# 最大化窗口
driver.maximize_window()


# 访问url
driver.get("https://www.baidu.com")
# time.sleep(2)
# # 最小化窗口
# driver.minimize_window()

div_element = driver.find_element(By.ID, 's-top-left')
print(type(div_element))
# 元素的find_element, 二次定位时的定位值一定是任意节点。
# div_element.find_element(By.XPATH, '//a[text()="新闻"]').click()
# 二次定位一组相同定位值的一组元素
'''
a_elements = div_element.find_elements(By.CSS_SELECTOR, '[class="mnav c-font-normal c-color-t"]')

for element in a_elements:
    print(element, type(element))
    element.click()
'''
# a_elements = driver.find_elements(By.XPATH, '//*[@id="s-top-left"]/a')
a_elements = driver.find_elements(By.CSS_SELECTOR, '#s-top-left > a')
for element in a_elements:
    # print(element, type(element))
    # element.click()
    # 获取元素的文本
    print(element.text)
    print(element.get_attribute("href"))

'''
driver.get('http://36.139.193.99:8280/mvue/login')
driver.find_element(By.CSS_SELECTOR, '[type="text"]').send_keys("admin")
driver.find_element(By.CSS_SELECTOR, '[type="password"]').send_keys("123456")
driver.find_element(By.XPATH, '//*[text()="登录"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[text()="用户中心"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[text()="组织管理"]').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '[placeholder="请输入"]').click()
time.sleep(1)
dems = driver.find_elements(By.CSS_SELECTOR, '[class="el-select-dropdown__item"]')
print(type(dems))
print("-"*100)
print(dems)

element = random.choice(dems)
element.click()
'''
time.sleep(111)