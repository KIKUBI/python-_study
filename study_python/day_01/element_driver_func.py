# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      element_driver_func.py
# Author:       lao_zhao
# Datetime:     2024/8/13 15:21
# Description:
# 
# ---------------------------------------------------------------------------
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

"""
    元素的操作：
        send_keys("value"): 给元素发送一个值。
        click(): 点击元素
        clear(): 清空元素的值
        get_attribute("属性名")：获取元素属性的值
        is_enable(): 判断元素是否可点击
        text: 获取元素的文本
        
        find_element(By.定位方式, "定位值")：查找元素
        find_elements(By.定位方式, "定位值")：查找多个元素，返回值为列表
"""
"""
    浏览器的操作：
        get('url'): 访问url
        
        find_element(By.定位方式, "定位值")：查找元素
        find_elements(By.定位方式, "定位值")：查找多个元素，返回值为列表
        
        maximize_window(): 浏览器的窗口最大化
        minimize_window(): 浏览器的窗口最小化
        get_window_size(): 获取浏览器的窗口大小
        
        title: 获取浏览器当前打开网页的title标签的值
        current_url: 获取当前网页的url
        
        forward(): 前进
        back(): 后退
        refresh(): 刷新
        
        close(): 关闭浏览器的网页
        quit(): 退出浏览器
        
        page_source: 获取当前网页中所有的数据
        get_screenshot_as_file("png图片路径")：浏览器的窗口截图
        
        execute_script("js"[, 元素])：执行js代码.
                记住滚动。js="arguments[0].scrollIntoView();"
                
                获取token: js='return sessionStorage.getItem("key")'
                          js='return localStorage.getItem("key")'
        
        iframe标签的切换：
        switch_to.frame(iframe标签的id或iframe标签的定位)：进入iframe标签嵌套的网页
        switch_to.parent_frame(): 回到父级页面
        switch_to.default_content(): 回到主页面
        
        句柄的切换：
        switch_to.window("句柄")：浏览器进行网页窗口的切换
        window_handles: 获取当前浏览器所有网页的句柄，返回值为列表
        current_window_handle: 获取当前窗口的句柄
        
        alert弹窗的处理
        switch_to.alert.accept(): 点击alert弹窗的确认
        switch_to.alert.dismiss(): 点击alert弹窗的取消
        switch_to.alert.send_keys("value"): 向alert弹窗发送值
        switch_to.alert.text: 获取alert弹窗的文本
"""

driver = webdriver.Chrome(service=webdriver.ChromeService("../chromedriver.exe"))


driver.get("https://www.baidu.com")
print(driver.get_window_size())

driver.maximize_window()

print(driver.get_window_size())
print(driver.title)

driver.find_element(By.ID, "kw").send_keys("python")
driver.find_element(By.ID, "su").click()
print(driver.current_url)
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)
# driver.refresh()


time.sleep(2)
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
# driver.execute_script('window.scrollTo(0,1500)')
# driver.execute_script("document.documentElement.scrollTop=5000")
# print(driver.page_source)

# driver.get_screenshot_as_file("./xx.png")

#
# driver.find_element(By.XPATH, '//*[text()="新闻"]').click()
# driver.find_element(By.XPATH, '//*[text()="hao123"]').click()

# print(driver.window_handles)
# handles = driver.window_handles
# time.sleep(2)
# driver.switch_to.window(handles[1])
#
# driver.close()
#
# print(driver.window_handles)

# driver.quit()
# print(driver.get_cookies())


''''
driver.get("http://36.139.193.99:8280/mvue/login")
driver.find_element(By.CSS_SELECTOR, '[type="text"]').send_keys("admin")
driver.find_element(By.CSS_SELECTOR, '[type="password"]').send_keys("123456")
driver.find_element(By.XPATH, '//*[text()="登录"]').click()
time.sleep(2)

print(driver.execute_script('return sessionStorage.getItem("currentUser")'))
'''
time.sleep(20)