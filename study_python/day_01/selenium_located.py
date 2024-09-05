# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      selenium_located.py
# Author:       lao_zhao
# Datetime:     2024/8/12 9:24
# Description:
# 
# ---------------------------------------------------------------------------
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
    webdriver(浏览器驱动文件): 每个浏览器都有自己的webdriver
        selenium的原理或webdriver的功能：
            webdriver会启动浏览器服务，服务启动后会启动浏览器。webdriver会解析python代码，
            将解析后的python代码发送给浏览器服务，浏览器服务将解析后python代码的动作让的浏览器执行，浏览器执行完之后，webdriver会接受浏览器执行之后的结果。
    

"""
"""
    selenium的八大定位：
        id：根据id属性定位
        name：根据name属性定位
        class_name: 根据class属性定位, 注意使用class属性值定位时，如果值中存在空格需要使用点代替空格。
        tag_name: 根据标签名(元素名)定位
        link_text: 根据超链接的文本定位
        partial_link_text: 根据超链接的部分文本定位
        
        xpath：根据xpath定位--可以根据标签的文本定位
            /: 子节点
            //：任意节点
            @: 当前节点
            *：通配符
            []: 过滤器
                [n]: 获取的是第n个标签
                [@属性名="值"]：根据标签的属性值定位
                [text()="文本值"]：根据标签的文本值定位
                [contains(@属性名, "值")]：根据标签的属性是否包含一个值进行定位
                [starts-with(@属性名, "值")]：根据标签的属性是否以一个开始值进行定位
                [ends-with(@属性名, "值")]]：根据标签的属性是否以一个结束值进行定位----停用
                
                [@属性名1="值1" and @属性名2="值2"]: 根据标签的多个属性值定位
                
        css_selector: 根据样式表达式定位--没法根据标签的文本定位。
                #id: 根据标签的id属性定位
                .class.class: 根据标签的class属性值定位
                标签名：根据标签的名称定位
                标签名#id: 根据标签的名称及标签的id属性定位
                标签名.class.class: 根据标签的名称及标签的class属性定位
                
                标签名[属性名="属性的值"]: 根据标签名称及标签的属性值定位
                [属性名="属性的值"]：根据标签的属性值定位
                [属性名1="属性的值1"][属性名2="属性的值2"]：根据标签的多个属性值定位
                [属性名^="属性的值"]: 根据标签的属性的开始值定位
                [属性名*="属性的值"]: 根据标签的属性的包含值定位
                [属性名$="属性的值"]: 根据标签的属性的结束值定位
                
                >: 子节点
                父级节点 > 子标签名:first-child: 定位第一个子标签
                父级节点 > 子标签名:last-child: 定位最后一个子标签
                父级节点 > 子标签名:nth-child(n): 定位第n个子标签
                父级节点 > 子标签名:nth-child(n) +/~ 兄弟标签名: 根据当前标签定位兄弟标签
"""
"""
    浏览器的操作-[Webdriver]：
        get("url"): 访问对应的url
        find_element(By.定位方式, "定位的值")：浏览器根据定位方式和定位的值，定位页面中的元素
        
        
        maximize_window(): 最大化浏览器的唱窗口
"""
"""
    元素(标签)的操作-[WebElement]：
        send_keys("值")：给对应的元素输入一个值
        click(): 点击元素/标签
"""

driver = webdriver.Chrome(service=webdriver.ChromeService("../chromedriver.exe"))

print(driver, type(driver))

driver.maximize_window()

driver.get("https://www.baidu.com")
# driver.get("http://47.109.99.224:8090/korei/login.jsp")

# id
"""
element = driver.find_element(By.ID, "kw")
element.send_keys("python")

driver.find_element(By.ID, 'su').click()
"""

# name
"""
driver.find_element(By.NAME, "wd").send_keys("成都小吃")
driver.find_element(By.ID, 'su').click()
"""

# class_name
'''
driver.find_element(By.CLASS_NAME, "s_ipt").send_keys("学习python")
driver.find_element(By.CLASS_NAME, 'bg.s_btn').click()
'''

# tag_name
'''
driver.find_element(By.NAME, 'username').send_keys("admin")
driver.find_element(By.NAME, 'password').send_keys(1)
driver.find_element(By.TAG_NAME, "a").click()
'''

# link_text
"""
# driver.find_element(By.LINK_TEXT, '新闻').click()
"""
# partial_link_text
"""
# driver.find_element(By.PARTIAL_LINK_TEXT, 'hao12').click()
"""

# xpath
"""
# driver.find_element(By.XPATH, '/html/body/form/div/div/div/div[1]/input').send_keys("admin")
# driver.find_element(By.XPATH, '//*[@type="text"]').send_keys("admin")
# driver.find_element(By.XPATH, '/html/body/form/div/div/div/div[2]/input').send_keys("1")
# driver.find_element(By.XPATH, '//input[@type="password"]').send_keys("1")
# driver.find_element(By.XPATH, '//a').click()

# driver.find_element(By.XPATH, '//a[@class="mnav c-font-normal c-color-t" and @href="http://tieba.baidu.com/"]').click()
# driver.find_element(By.XPATH, '//a[text()="新闻"]').click()

# driver.find_element(By.XPATH, '//a[text()="新闻" and @class="mnav c-font-normal c-color-t"]').click()

# driver.find_element(By.XPATH, '//a[contains(text(), "闻")]').click()
# driver.find_element(By.XPATH, '//a[contains(text(), "闻") and @class="mnav c-font-normal c-color-t"]').click()
# driver.find_element(By.XPATH, '//a[contains(@class, "mnav c-font-normal") and text()="新闻"]').click()

driver.find_element(By.XPATH, '//a[starts-with(text(), "hao")]').click()
driver.find_element(By.XPATH, '//a[starts-with(text(), "贴") and contains(@class, "c-font-normal")]').click()
"""

# css_selector
# driver.find_element(By.CSS_SELECTOR, '#kw').send_keys("python")
# driver.find_element(By.CSS_SELECTOR, '.s_ipt').send_keys("python")
# driver.find_element(By.CSS_SELECTOR, '#su').click()
# driver.find_element(By.CSS_SELECTOR, '.bg.s_btn').click()

# driver.find_element(By.XPATH, '//*[@type="text"]').send_keys("Admin")
# driver.find_element(By.XPATH, '//*[@type="password"]').send_keys("1")
# driver.find_element(By.CSS_SELECTOR, 'a').click()


# driver.find_element(By.CSS_SELECTOR, 'input#kw').send_keys("星期一")
# driver.find_element(By.CSS_SELECTOR, 'input#su').click()

# driver.find_element(By.CSS_SELECTOR, 'input#kw.s_ipt').send_keys("星期二")
# driver.find_element(By.CSS_SELECTOR, 'input.bg.s_btn#su').click()

# driver.find_element(By.CSS_SELECTOR, '[id="kw"]').send_keys("星期三")
# driver.find_element(By.CSS_SELECTOR, '[id="su"]').click()

# driver.find_element(By.CSS_SELECTOR, '[id="kw"][name="wd"][class="s_ipt"]').send_keys("星期四")
# driver.find_element(By.CSS_SELECTOR, 'input[value="百度一下"]').click()


# driver.find_element(By.CSS_SELECTOR, 'a[href^="https://www.hao123.com"]').click()
# driver.find_element(By.CSS_SELECTOR, '[href$="src=from_pc"]').click()
# driver.find_element(By.CSS_SELECTOR, '[href*="www.hao123.com"]').click()

# driver.find_element(By.XPATH, '//*[@id="s-top-left"]/a[5]').click()
# driver.find_element(By.CSS_SELECTOR, '[id="s-top-left"] > a:first-child').click()
# driver.find_element(By.CSS_SELECTOR, '[id="s-top-left"] > div:last-child').click()  # 最后一个子标签的名称一定要正确
# driver.find_element(By.CSS_SELECTOR, '[id="s-top-left"] > a:nth-child(5)').click()
# driver.find_element(By.CSS_SELECTOR, '[id="s-top-left"] > a:nth-child(5) + a').click()  # 定位兄弟标签
# driver.find_element(By.CSS_SELECTOR, '[id="s-top-left"] > a:nth-child(5) ~ a').click()

time.sleep(111)
