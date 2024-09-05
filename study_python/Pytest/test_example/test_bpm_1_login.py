# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      test_bpm_login.py
# Author:       lao_zhao
# Datetime:     2024/9/2 17:31
# Description:
# 
# ---------------------------------------------------------------------------



class TestBPMLogin:
    host = 'http://36.139.193.99:8088'

    def test_login(self, fix_req):
        # 构造登录数据
        login_url = self.host + '/auth'
        login_data = {
            "username": "admin", "password": "e6sFAeI1rLdzBgm3WzD/294rAtu9uI+0JSwNEexkatU+Pdzx8Y0qxGQyYy4"
                                             "xTtGos4fDe2WSUtDkO2v8ri1u66TFGr2+EuUGdo1hKadDbbmroUjeZk07s"
                                             "d4qhbuV740TLTdL7uHpg7Fod4MWDwSsMmg/EaFFahjKRCjNGPsV5Rw="}
        # 使用Session对象发送请求，Session对象就是fix_req自定义固件
        res = fix_req.request(method="post", url=login_url, json=login_data)
        try:
            assert "超级管理" in res.text
        except AssertionError:
            print("登录接口有bug")
            raise AssertionError("断言失败")
        else:
            # 更新token到Session对象的headers中
            fix_req.headers["Authorization"] = f"Bearer {res.json().get('token')}"