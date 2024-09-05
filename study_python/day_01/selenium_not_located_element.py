# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      selenium_not_located_element.py
# Author:       lao_zhao
# Datetime:     2024/8/13 10:49
# Description:
# 
# ---------------------------------------------------------------------------
import time

from faker import Faker
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

"""
    selenium中元素定位不到的原因：
        1: 是否有iframe标签
            浏览器对象.switch_to.frame("iframe标签的定位/iframe的id")：进入嵌套的网页
            浏览器对象.switch_to.parent_frame(): 回到父页面
            浏览器对象.switch_to.default_content(): 回到主页面
        2：元素未加载
            滚动到元素周围，先让元素加载，再定位
            浏览器对象.execute_script("arguments[0].scrollIntoView();", 元素)
            
        3：元素已加载未显示
            需要使用鼠标操作的对象，将鼠标移动到元素位置，将元素显示出来再定位。
            鼠标对象的创建：ActionChains(浏览器对象)
            鼠标对象的操作：
                    move_by_offset(x, y): 将鼠标移动到指定的坐标位置
                    move_to_element(元素)：将鼠标移动到指定的元素位置
                    注意： 
                        1：move_by_offset和move_to_element的鼠标动作都会被存储，所有需要调用ActionChains对象的perform释放失败的存储的动作
                        2：将鼠标移动后，尽量点击下。鼠标的点击的动作也会被存储，所有也需要perform。
                    
                    reset_actions(): 重置鼠标事件，鼠标操作之后一定要重置，如果不重置下次操作不生效。
            
        4：是否有句柄的切换
            句柄：浏览器对象每次操作之后打开的网页，每个网页都一个唯一的字符串标记，这个字符串就是网页的句柄。
            浏览器对象.window_handles : 获取浏览器所有的句柄
            浏览器对象.current_window_handle: 获取当前网页的句柄
            浏览器对象.switch_to.window("句柄")：句柄的切换，网页的切换
            
        5：是否有alert弹窗
            alert窗口的操作：
                点击确认：浏览器对象.switch_to.alert.accept()
                点击取消：浏览器对象.switch_to.alert.dismiss()
                向alert窗口输入内容：浏览器对象.switch_to.alert.send_keys("value")
                获取alert弹窗的文本：浏览器对象.switch_to.alert.text
        6：定位的值是否书写错误
"""

'''
driver = webdriver.Chrome(service=webdriver.ChromeService("../chromedriver.exe"))
driver.maximize_window()
driver.get("http://36.139.193.99:8280/mvue/login")
driver.find_element(By.CSS_SELECTOR, '[type="text"]').send_keys("admin")
driver.find_element(By.CSS_SELECTOR, '[type="password"]').send_keys("123456")
driver.find_element(By.XPATH, '//*[text()="登录"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[text()="用户中心"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[text()="组织管理"]').click()

# 创建鼠标对象
action = ActionChains(driver)
data = Faker(locale="zh_cn")

for _ in range(10):
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '[placeholder="请输入"]').click()
    time.sleep(1)
    dem_element = driver.find_elements(By.CSS_SELECTOR, '[class="el-scrollbar__view el-select-dropdown__list"] > li')
    js = "arguments[0].scrollIntoView();"
    driver.execute_script(js, dem_element[10])
    time.sleep(2)
    # dem_element[10].click()
    print(dem_element[10].is_enabled())
    if dem_element[10].is_enabled():
        dem_element[10].click()

    # 将鼠标移动到指定的坐标位置，再点击一下
    action.move_by_offset(435, 204).click()
    # 释放ActionChains存储的动作
    action.perform()
    # 鼠标操作之后，需要强制睡眠2-3秒
    time.sleep(2)
    # 重置鼠标对象
    action.reset_actions()

    # 定位一组有相同属性的元素
    child_orgs = driver.find_elements(By.XPATH, '//*[text()="添加子组织"]')
    child_orgs[-1].click()

    time.sleep(1)
    # 添加组织
    org_name = data.company()
    org_code = data.phone_number()
    driver.find_element(By.CSS_SELECTOR, '[placeholder="请输入组织名称"]').send_keys(org_name)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '[placeholder="请输入组织编码"]').clear()
    driver.find_element(By.CSS_SELECTOR, '[placeholder="请输入组织编码"]').send_keys(org_code)
    driver.find_element(By.XPATH, '//*[text()="保存"]').click()
    time.sleep(1.5)
    result = driver.find_element(By.CSS_SELECTOR, '[class="el-message__content"]').text
    print(result)
    # 截图
    driver.get_screenshot_as_file(f"./组织的名称={org_name}_组织的编码={org_code}.png")

# logout = driver.find_element(By.XPATH, '//*[text()="退出系统"]')
# print(logout)
# logout.click()
logot = driver.find_element(By.CSS_SELECTOR, 'div[class="avatar-wrap el-popover__reference"] > span[class="el-avatar el-avatar--circle"]')
# 将鼠标移动到指定的元素位置
action.move_to_element(logot).click().perform()
time.sleep(2)
# 重置鼠标对象
action.reset_actions()
driver.find_element(By.XPATH, '//*[text()="退出系统"]').click()
'''


driver = webdriver.Chrome(service=webdriver.ChromeService("../chromedriver.exe"))
driver.maximize_window()
'''
driver.get("https://www.baidu.com")

driver.find_element(By.XPATH, '//*[text()="新闻"]').click()

time.sleep(2)

# 获取当前浏览器所有句柄
print(driver.window_handles)
window_handles = driver.window_handles
# 获取当前网页的句柄
print(driver.current_window_handle)
# 切换句柄
driver.switch_to.window(window_handles.pop())
print("切换之后的句柄", driver.current_window_handle)

driver.find_element(By.XPATH, '//*[@id="pane-news"]//ul[1]/li[6]').click()


print("----", window_handles)
print(driver.window_handles)
'''

driver.get(r"D:\Project\PythonDoc\test62\test62\study_selenium\day_03\demo.html")
driver.find_element(By.ID, "1").click()

time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)

driver.find_element(By.ID, "2").click()
time.sleep(2)
# driver.switch_to.alert.dismiss()
driver.switch_to.alert.accept()
time.sleep(2)

driver.find_element(By.ID, "3").click()
time.sleep(2)
driver.switch_to.alert.send_keys("1000")
# 获取alert弹窗的文本
print(driver.switch_to.alert.text)
time.sleep(2)
driver.switch_to.alert.accept()

time.sleep(111)