# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      requests_demo.py
# Author:       lao_zhao
# Datetime:     2024/8/28 13:59
# Description:
# 
# ---------------------------------------------------------------------------
import json
import requests
from study_python.Request.db import DB

"""
    requests: 功能：模拟http协议的请求。requests默认使用http协议的1.1版本。---2.0(http2)
"""
# request函数的形参
"""
    :param method: 以字符串的形式传参http协议的请求方法。比如：'get','post','put','delete'....
    :param url: 以字符串的形式传入请求的url。
    
    :param params: (可选) 地址栏传参，传参的格式为字典或列表套元组。地址栏传参的格式为：url?key1=value1&key2=value2....
                        字典的格式：{"key1": "value1", "key2": "value2"}
                        列表套元组: [("key1", "value1"),  ("key2", "value2")]
                        
    :param data: (可选) 请求体中，以媒体类型为application/x-www-form-urlencoded【表单】进行传参，传参的格式为字典或列表套元组
                    application/x-www-form-urlencoded【表单】进行传参：请求体中数据的格式为：key1=value1&key2=value2....
                        字典的格式：{"key1": "value1", "key2": "value2"}
                        列表套元组: [("key1", "value1"),  ("key2", "value2")]
                        
    :param json: (可选) 请求体中，以媒体类型为application/json进行传参，传参的格式为json可序列化的python对象[要么字典要么列表]
    
    :param headers: (可选) 以字典的形式配置请求的头部信息。 ----- 相当于jmeter的http消息头管理器。
                        字典的格式为：{"请求头部字段": "请求头部字段的值"}
    
    :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
    
    :param files: (可选) 请求体中上传文件，对应的媒体类型为：multipart/form-data. 以字典的形式进行上传文件。
                        字典的格式1: {"上传文件的参数名": 文件对象}
                        字典的格式2: {"上传文件的参数名": ("上传文件名称", 文件对象)}
                        字典的格式3: {"上传文件的参数名": ("上传文件名称", 文件对象, "上传文件所对应的媒体类型")}
    
    :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
    :param timeout: (optional) How many seconds to wait for the server to send data
        before giving up, as a float, or a :ref:`(connect timeout, read
        timeout) <timeouts>` tuple.
    :type timeout: float or tuple
    :param allow_redirects: (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to ``True``.
    :type allow_redirects: bool
    :param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
    :param verify: (optional) Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use. Defaults to ``True``.
    :param stream: (optional) if ``False``, the response content will be immediately downloaded.
    :param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
"""
"""
    Response类型为请求服务器成功之后服务器返回数据的类型。
    
        text: 获取服务器响应体数据，返回值类型为字符串
        content: 获取服务器响应体数据，返回值类型为bytes类型
        json(): 如果服务器响应体数据为json类型的数据，可以直接使用json()方法将响应体数据序列化为python对象[字典/列表]

"""

req_head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}
# get请求不传参
'''
sugou_url = 'https://www.baidu.com/'
# 配置请求头部字段
req_head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}
# 发送请求
res = requests.request(method='gEt', url=sugou_url, headers=req_head)

print(res, type(res))
print(res.text)
'''

# get请求地址栏传参-方式1
'''
# https://www.baidu.com/s?ie=UTF-8&wd=%E6%88%90%E9%83%BD
baidu_url = 'https://www.baidu.com/s'
# 配置传参-字典
query_data1 = {"ie": "UTF-8", "wd": "成都"}
# 配置传参-列表套元组
query_data2 = [("ie", "UTF-8"), ("wd", "python")]

# 发送请求
res1 = requests.request(method="get", url=baidu_url, headers=req_head, params=query_data2)

print(res1.text)
'''
# get请求地址栏传参-方式2
'''
baidu_url = 'https://www.baidu.com/s?ie=UTF-8&wd=成都'
# 发送请求
res2 = requests.request(method='get', url=baidu_url, headers=req_head)

print(res2.text)
'''

# 请求体进行表单传参
# 科瑞登录
'''
login_url = 'http://47.109.99.224:8090/korei/login.ht'
login_data = {"username": "admin", "password": "1"}
login_data_list = [("username", "admin"), ("password", "1")]
# 发送请求
res = requests.request(method="post", url=login_url, data=login_data_list)

print(res.text)
'''

# json格式传参
'''
# bpm登录
bpm_host = 'http://36.139.193.99:8088'
bpm_login_url = bpm_host + '/auth'
bpm_login_data = {
            "password": "DAg7dTicBaxc9KLI74IKKAuDzml5xgQxpAn+xlzjGb82LYnsi26HfCOgSuk3V8bSva74gNVQ7j51OaAcD4Gymid5G7WAhlmfMgE7SSVUYB7iQ0M3N6Sv+yS0tbRnNwMmc/bh1DmkiFwDmUnUliZhVcQwm1PCl4GgPpzmv7GuxSw=",
            "username": "admin"
        }
# 发送登录请求
res = requests.request(method='post', url=bpm_login_url, json=bpm_login_data)
print(res.text, type(res.text))
# 获取服务器返回token
token = json.loads(res.text)["token"]
print(token)
# 将token配置在一个字典中，这个字典就是请求的头部信息
bpm_req_head = {"Authorization": f"Bearer {token}"}
# =========================================================
# 添加维度
add_dem_url = bpm_host + '/api/demension/v1/dem/addDem'
# 配置添加维度的数据
add_dem_data = {
            "code": "addDem",
            "description": "requests添加的维度",
            "isDefault": 1,
            "name": "requests添加的维度"
        }

# 添加之前删除数据库中现有的维度
db = DB()
del_dem = """delete from uc_demension where CODE_="addDem";"""
db.delete(del_dem)
# 发送请求
add_dem_res = requests.request(method="post", url=add_dem_url, json=add_dem_data, headers=bpm_req_head)
# =========================================================
# 根据维度编码获取维度信息
get_dem_msg_url = bpm_host + '/api/demension/v1/dem/getDem'
# 配置请求数据
query_data = {"code": "addDem"}
# 发送请求
get_dem_res = requests.request(method="get", url=get_dem_msg_url, params=query_data, headers=bpm_req_head)
# 提取维度id
dem_id = json.loads(get_dem_res.text)['id']

# =========================================================
# 添加组织
add_org_url = bpm_host + '/api/org/v1/org/addOrg'
# 配置添加组织的数据
add_org_data = [{
            "code": "addOrg",
            "demId": dem_id,
            "exceedLimitNum": 0,
            "grade": "",
            "limitNum": 0,
            "name": "requests添加的组织",
            "nowNum": 0,
            "orderNo": 0,
            "parentId": "0"
        },
        {
            "code": "addOrg1",
            "demId": "",
            "exceedLimitNum": 0,
            "grade": "",
            "limitNum": 0,
            "name": "requests添加的组织",
            "nowNum": 0,
            "orderNo": 0,
            "parentId": "0"
        },
]
for data in add_org_data:
    # 添加组织之前删除组织
    del_org = f"""delete from uc_org where CODE_="{data['code']}";"""
    db.delete(del_org)
    # 发送请求添加组织
    add_org_res = requests.request(method="post", url=add_org_url, json=data, headers=bpm_req_head)
    print(add_org_res.text)
    
'''

# 上传文件
# 登录
bpm_host = 'http://36.139.193.99:8088'
bpm_login_url = bpm_host + '/auth'
bpm_login_data = {
            "password": "DAg7dTicBaxc9KLI74IKKAuDzml5xgQxpAn+xlzjGb82LYnsi26HfCOgSuk3V8bSva74gNVQ7j51OaAcD4Gymid5G7WAhlmfMgE7SSVUYB7iQ0M3N6Sv+yS0tbRnNwMmc/bh1DmkiFwDmUnUliZhVcQwm1PCl4GgPpzmv7GuxSw=",
            "username": "admin"
        }
# 发送登录请求
login_res = requests.request(method="post", url=bpm_login_url, json=bpm_login_data)
# 登录成功，获取服务器返回token
result_content = json.loads(login_res.text)
# 提取服务器返回的token，并将token存在一个字典中
bpm_req_head = {"Authorization": f"Bearer {result_content['token']}"}
# 上传文件-使用登录成功的token
# 配置上传文件的数据
file_upload_url = bpm_host + '/system/file/v1/fileUpload'
# 配置上传的文件
# 获取文件对象
"""
    r/w/a
    r+/w+/a+
    b
    rb wb ab
    
    with xxx as 变量:
        ...
"""


# 发送请求



# # 关闭文件对象
# file_obj.close()

with open("./11.jpg", mode="rb") as f:
    # 字典的格式1: {"上传文件的参数名": 文件对象}
    file_dict1 = {"files": f}
    # 字典的格式2: {"上传文件的参数名": ("上传文件名称", 文件对象)}
    file_dict2 = {"files": ("♠♣▣▤▥▦▩.png", f)}
    # 字典的格式3: {"上传文件的参数名": ("上传文件名称", 文件对象, "上传文件所对应的媒体类型")}
    file_dict3 = {"files": ("♠♣▣▤▥▦▩.png", f, "中国/成都")}

    result = requests.request(method="post", url=file_upload_url, files=file_dict3, headers=bpm_req_head)
    print(result.text)

    context = result.content
    print(type(context), context)

    s1 = context.decode("utf-8")  # bytes类型转字符串。 bytes数据.decode(["编码格式"])
    print(type(s1), s1)

    b1 = s1.encode("utf-8")   # 字符串转bytes类型。 字符串数据.encode(["编码格式"])
    print(type(b1), b1)
    print("-"*100)

    j1 = result.json()
    print(type(j1), j1)