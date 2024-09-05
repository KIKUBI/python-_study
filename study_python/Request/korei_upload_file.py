# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      korei_upload_file.py
# Author:       lao_zhao
# Datetime:     2024/8/29 10:22
# Description:
# 
# ---------------------------------------------------------------------------
import requests

"""
    requests: 功能：模拟http协议的请求。requests默认使用http协议的1.1版本。---2.0(http2)
"""
# request函数的形参
"""
    :param method: 以字符串的形式传参http协议的请求方法。比如：'get','post','put','delete'....
    :param url: 以字符串的形式传入请求的url。
    
    :param headers: (可选) 以字典的形式配置请求的头部信息。 ----- 相当于jmeter的http消息头管理器。
                        字典的格式为：{"请求头部字段": "请求头部字段的值"}

    :param cookies: (可选) cookie可以使用字典或CookieJar类型发送给服务器。

    :param params: (可选) 地址栏传参，传参的格式为字典或列表套元组。地址栏传参的格式为：url?key1=value1&key2=value2....
                        字典的格式：{"key1": "value1", "key2": "value2"}
                        列表套元组: [("key1", "value1"),  ("key2", "value2")]

    :param data: (可选) 请求体中，以媒体类型为application/x-www-form-urlencoded【表单】进行传参，传参的格式为字典或列表套元组
                    application/x-www-form-urlencoded【表单】进行传参：请求体中数据的格式为：key1=value1&key2=value2....
                        字典的格式：{"key1": "value1", "key2": "value2"}
                        列表套元组: [("key1", "value1"),  ("key2", "value2")]

    :param json: (可选) 请求体中，以媒体类型为application/json进行传参，传参的格式为json可序列化的python对象[要么字典要么列表]

    
    :param files: (可选) 请求体中上传文件，对应的媒体类型为：multipart/form-data. 以字典的形式进行上传文件。
                        字典的格式1: {"上传文件的参数名": 文件对象}
                        字典的格式2: {"上传文件的参数名": ("上传文件名称", 文件对象)}
                        字典的格式3: {"上传文件的参数名": ("上传文件名称", 文件对象, "上传文件所对应的媒体类型")}
                        
    
    :param allow_redirects: (可选) 开启或关闭http协议的自动重定向。默认值为True(开启)。
    
    :param timeout: (可选) 设置链接服务器的链接超时时间。
    :param proxies: (可选) 配置代理IP地址。
    
    :param verify: (可选) 开启或关闭CA认证。默认为True(开启)。
    :param cert: (可选) 以元组的形式配置ssl的pem文件内容。---慎用。
    :param stream: (可选) 开启或关闭以流的模式下响应体数据。默认为False(关闭)。
"""

"""
    Response类型：
        响应体数据：
            text: 字符串
            content： bytes
            json(): 将服务器返回的json数据序列化为python对象
        
        响应头数据：
            headers： 获取响应头数据，返回值类型当作字典使用。
            cookies: 获取服务器响应的cookie数据，返回值类型为CookJar类型--CookieJar类型也可以当作字典使用
            
        状态行：
            status_code: 获取响应的状态码
            reason: 获取状态码的描述信息

        其他操作:
            elapsed: 获取服务器响应时间
            encoding: 获取服务器响应数据的编码格式
            url: 获取服务器响应数据的url
"""
"""
    CookieJar类型的操作：cookie数据是key=value的格式。
        keys(): 获取所有cookie的key
        values(): 获取所有cookie的value
        items(): 获取所有cookie的键值对
        list_paths(): 获取所有cookie的路径
        list_domains(): 获取所有cookie的域名
        update(字典)：更新cookie的值
        get_dict(): 将CookieJar类型转成字典
"""


login_url = 'http://47.109.99.224:8090/korei/login.ht'
login_data = {"username": "admin", "password": "1"}

# 登录
# korei_res = requests.request(method="post", url=login_url, data=login_data, allow_redirects=False)
korei_res = requests.request(method="post", url=login_url, data=login_data, allow_redirects=False)
# 其他操作：
print(korei_res.status_code)
print(korei_res.reason)
print(korei_res.elapsed)
print(korei_res.encoding)
print(korei_res.url)

korei_cookie = korei_res.cookies
cookie_dict = korei_cookie.get_dict()
print(cookie_dict)
# 获取响应头
'''
header = korei_res.headers
print(type(header))
print(header)
# 获取服务器返回的cookie
korei_cookie = korei_res.cookies
print(korei_cookie)
# 将CookieJar转成字典
cookie_dict = korei_cookie.get_dict()
print(cookie_dict)
# 给字典添加一个键值对
cookie_dict["CURRENT_SYSTEM"] = "1"
cookie_dict["python"] = "hello"
# cookie_dict["JSESSIONID"] = "hello korei"
'''
# CookieJar类型的操作
'''
print(type(korei_cookie))
# keys
print(korei_cookie.keys())
# values
print(korei_cookie.values())
# items
print(korei_cookie.items())
# list_paths
print(korei_cookie.list_paths())
# list_domains
print(korei_cookie.list_domains())
# get_dict
print(korei_cookie)
print(korei_cookie.get_dict())
# update
korei_cookie.update({"key": "value"})
print(korei_cookie)
print(korei_cookie["CURRENT_SYSTEM"])
'''

# # 上传文件
file_upload_url = 'http://47.109.99.224:8090/korei/platform/system/sysFile/fileUpload.ht'
# 配置上传文件的数据
with open("../cxy_demo/img/cxy.png", mode="rb") as f:
    file_dict = {"file": ("../cxy_demo/img/cxy.png", f, "text/plain")}
    # 上传文件
    res = requests.request(method="post", url=file_upload_url, files=file_dict, cookies=cookie_dict)
    print(res.text)