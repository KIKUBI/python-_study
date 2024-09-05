# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      requests_demo.py
# Author:       lao_zhao
# Datetime:     2024/8/28 13:59
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
    
    :param params: (可选) 地址栏传参，传参的格式为字典或列表套元组。地址栏传参的格式为：url?key1=value1&key2=value2....
                        字典的格式：{"key1": "value1", "key2": "value2"}
                        列表套元组: [("key1", "value1"),  ("key2", "value2")]
                        
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    
    :param headers: (可选) 以字典的形式配置请求的头部信息。 ----- 相当于jmeter的http消息头管理器。
                        字典的格式为：{"请求头部字段": "请求头部字段的值"}
    
    :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
    :param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
        ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
        or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content_type'`` is a string
        defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
        to add for the file.
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
baidu_url = 'https://www.baidu.com/s?ie=UTF-8&wd=成都'
# 发送请求
res2 = requests.request(method='get', url=baidu_url, headers=req_head)

print(res2.text)