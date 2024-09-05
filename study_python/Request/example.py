# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      example.py
# Author:       lao_zhao
# Datetime:     2024/8/29 9:33
# Description:
# 
# ---------------------------------------------------------------------------
import requests

from study_python.request.db import DB

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
# 1.2 发送请求
login_result = requests.request(method="post", url=login_url, json=login_data)
# 提取token
token = login_result.json()["token"]
# 将token存放在请求头字典中。
req_head = {"Authorization": f"Bearer {token}"}
# 添加用户
add_user_url = host + '/api/user/v1/user/addUser'
# 添加用户之前，删除现有的用户
db = DB()
db.delete("""delete from uc_user where ACCOUNT_="zhangsan1hao";""")
# 配置添加用户的数据
add_user_data = {
    "id": "",
    "account": "zhangsan1hao",
    "address": "",
    "email": "",
    "fullname": "张三1号",
    "mobile": "",
    "password": "123456",
    "photo": "",
    "sex": "",
    "status": 1
}

# 添加用户
res = requests.request(method="post", url=add_user_url, json=add_user_data, headers=req_head)
# 用户添加成功之后在修改用户的头像
if "用户添加成功" in res.text:
    # 上传用户的头像
    upload_image_url = host + "/system/file/v1/fileUpload"
    # 配置上传文件的数据
    with open("./1.png", mode="rb") as f:
        upload_data = {"files": ("img.png", f, "image/png")}
        # 上传图片
        upload_file_res = requests.request(method="post", url=upload_image_url, files=upload_data, headers=req_head)

    # 判断上传文件是否成功，成功之后提取上传文件的id，再更新用户
    if "true" in upload_file_res.text:
        file_id = upload_file_res.json()["fileId"]
        # 更新用户的头像
        update_user_url = host + '/api/user/v1/user/updateUser'
        # 配置更新用户的数据
        update_data = {
            "createTime": "2024-08-29 10:02:48",
            "isDelete": "0",
            "id": "1828976561094238208",
            "fullname": "",
            "account": "zhangsan1hao",
            "password": "123456",
            "email": "",
            "mobile": "",
            "address": "",
            "photo": str(file_id),
            "sex": "保密",
            "from": "restful",
            "status": 1,
            "groupId": "",
            "hasSyncToWx": 0,
            "tenantId": "-1",
            "pwdCreateTime": "2024-08-29 10:02:48",
            "attributes": {},
            "enabled": True,
            "userId": "1828976561094238208",
            "username": "zhangsan1hao",
            "admin": False,
            "identityType": "user",
            "enable": True,
            "accountNonExpired": True,
            "accountNonLocked": True,
            "credentialsNonExpired": True,
            "pkVal": "1828976561094238208"
        }
        # 发送请求更新用户
        update_res = requests.request(method='post', url=update_user_url, json=update_data, headers=req_head)
        print(update_res.text)