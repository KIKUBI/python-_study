# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      example.py
# Author:       lao_zhao
# Datetime:     2024/8/13 16:43
# Description:
# 
# ---------------------------------------------------------------------------
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from study_python.cxy_zuoye.selezuoye.db import DB
from study_python.cxy_zuoye.selezuoye.excel import cxy_excel
from study_python.cxy_zuoye.selezuoye.login_func_page import LoginFunc


class OrgFunc(LoginFunc):

    def __init__(self, browser="c"):
        # 调用父类的构造方法
        super().__init__(browser=browser)
        # 先登录
        self.login_func(username="admin", password="123456")
        self.driver.find_element(By.XPATH, '//*[text()="用户中心"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[text()="组织管理"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@class="el-link--inner" and starts-with(text(), "组织管理")]').click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="请输入"]').click()
        time.sleep(2)
        dem = self.driver.find_elements(By.CSS_SELECTOR, '[class="el-scrollbar__view el-select-dropdown__list"] > li')[4]
        self.driver.execute_script("arguments[0].scrollIntoView();", dem)
        time.sleep(2)
        if dem.is_enabled():
            dem.click()
        self.action = ActionChains(self.driver)

    def add_org_func(self, org_name, org_code):
        self.action.move_by_offset(435, 204).click().perform()
        time.sleep(2)
        self.action.reset_actions()

        # 定位添加子组织
        self.driver.find_elements(By.XPATH, '//*[@class="el-dropdown-menu__item" and text()="添加子组织"]')[-1].click()
        time.sleep(2)

        # 添加组织的核心
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="请输入组织名称"]').send_keys(org_name)
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="请输入组织编码"]').send_keys(Keys.LEFT_CONTROL+"a")
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="请输入组织编码"]').send_keys(Keys.LEFT_CONTROL+"x")
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="请输入组织编码"]').send_keys(org_code)
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[text()="保存"]').click()
        time.sleep(1.5)
        # 获取服务器返回的结果
        res = self.driver.find_element(By.CSS_SELECTOR, '[class="el-message__content"]').text
        # 截图
        self.driver.get_screenshot_as_file(f"{org_name}_{org_code}.png")
        return res



if __name__ == '__main__':
    cxyexcl = cxy_excel()
    lz = cxyexcl.reday_excel()
    db = DB()
    org = OrgFunc()
    for z in lz[:]:
        if z[0] =='None':
            z[0] = ''
        elif z[1] == 'None':
            z[1] = ''
        elif z[0] =='None' and z[1] == 'None':
            z[0] = ''
            z[1] = ''
        else:
            if z[-2] !='':
                db.delete(z[-2])
            result = org.add_org_func(org_name=z[0], org_code=z[1])
            if z[-1] == result:
                cxyexcl.write_excel('断言成功',z)
            else:
                cxyexcl.write_excel('断言失败',z)