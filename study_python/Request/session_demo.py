# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      session_demo.py
# Author:       lao_zhao
# Datetime:     2024/8/29 14:01
# Description:
# 
# ---------------------------------------------------------------------------
import random
import requests


"""
    sessions.Session()类对象的功能：
        1: 自动存储和发送cookie。
            Session类对象发送请求之后，如果服务器有返回cookie数据(服务器在响应头中以set-cookie字段响应cookie数据)，Session类对象会提取服务器
            返回的cookie，并存储在Session类对象的cookies属性中, 下次发送请求时，会将cookies存储的cookie数据会发送给服务器。
        2: Session类对象会自动关联请求头部信息。
            Session类对象headers就是请求头部，headers的值如果发送改变，以后的请求都会使用改变之后的headers的值。

    缺点：跨域名时没法使用。
"""
# requests接口之间的关联
"""
    cookie的关联：
        手动：请求服务器，服务器如果有返回cookie数据，需要手动将服务器返回的cookie数据提取出来，下次请求时，将提取的cookie以cookies关键字发送给服务器。
        自动：使用Session类对象发送请求时，Session类对象就会自动存储和发送cookie
        
    token关联：
        手动：请求服务器，服务器如果有返回token数据，需要手动提取服务器返回token，并将token存放在一个字典中，下次请求时，将存放token的字典以headers关键字发送给服务器。
        自动：使用Session类对象发送请求时，将token更新到Session对象的headers中，以后的请求都会使用更新过后的Session的headers。

    接口之间的请求数据的关联-当前接口需要使用上一个接口服务器返回的数据时，需要在上一个接口服务器返回的数据中提取当前接口依赖的数据，在再当前接口请求时发送给服务器。
"""

# 自动存储和发送cookie。
'''
# 配置科瑞登录的数据
login_url = 'http://47.109.99.224:8090/korei/login.ht'
login_data = {"username": "admin", "password": "1"}
# 创建Session类对象
korei_session = requests.sessions.Session()
# 请求的头部信息
print(korei_session.headers)
print(korei_session.cookies.get_dict())
# 使用Session类对象发送请求
res = korei_session.request(method="post", url=login_url, data=login_data)
print("-"*100)
print(korei_session.headers)
print(korei_session.cookies, type(korei_session.cookies))


# 上传文件
file_upload_url = 'http://47.109.99.224:8090/korei/platform/system/sysFile/fileUpload.ht'
# 配置上传文件的数据
with open("data.txt", mode="rb") as f:
    # 配置上传文件的数据
    upload_data = {"file": f}
    # 使用Session类对象上传文件
    res1 = korei_session.request(method="post", url=file_upload_url, files=upload_data)
    print(res1.text)
'''


# Session类对象会自动关联请求头部信息
# 配置bpm登录数据
# 请求公共数据
host = "http://36.139.193.99:8088"
# 登录
login_url = host + "/auth"
# 1.1配置登录数据
login_data = {
    "username": "admin",
    "password": "i0m88K4KwaWgwLaz4kDeGcsAQhZapnL26cE3bCgMY+00BUuTAll9H/yk46LKXN8IF03tEQ9nMyPvbEa5j"
                "3noxSBk/LaWmfT59u6eJS1Saehdrehm0MqHal+hbJ5+4HFY2Udb76RGqJh3JWEZTwGGkiyDUtydvdzr2PQGOZqbNS0="
}
# 创建Session类对象
bpm_session = requests.sessions.Session()
# bpm_session = requests.Session()
# 请求之前的headers的值
print(bpm_session.headers)
# 使用Session类对象发送请求
res = bpm_session.request(method="post", url=login_url, json=login_data)
# 提取服务器返回的token
token = res.json().get('token')
# 将token的值存放到Session类对象的headers中。
bpm_session.headers["Authorization"] = f"Bearer {token}"


# 添加维度
add_dem_url = host + "/api/demension/v1/dem/addDem"

dem_code = 'addDem'+str(random.randint(1, 100000000))
add_dem_data = {
            "code": f"{dem_code}",
            "description": "addDem",
            "isDefault": 0,
            "name": f"SessionAddDem{str(random.randint(1, 100000000))}"
        }

# 使用Session对象发送请求
res = bpm_session.post(url=add_dem_url, json=add_dem_data)

# 根据维度编码获取维度信息
get_dem_msg_url = host + "/api/demension/v1/dem/getDem"
get_dem_msg_data = {"code": dem_code}
# 发送请求
res2 = bpm_session.request(method="get", url=get_dem_msg_url, params=get_dem_msg_data)
print(res2.json())

print(bpm_session.headers)


bd_session = requests.sessions.Session()
res = bd_session.request(method="get", url="https://www.baidu.com", verify=False)
print(res.text)