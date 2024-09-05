# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      json_demo.py
# Author:       lao_zhao
# Datetime:     2024/8/8 15:22
# Description:
# 
# ---------------------------------------------------------------------------
import json


"""
    json格式的数据：就是python中字典或列表的相互嵌套。
    json格式的数据其实就是一个字符串，称为json格式的字符串
"""
"""
    loads(json格式字符串)：将json格式的字符串转成(序列化)python的字典或列表
    load(json文件的文件对象): 将json文件的文件对象所对应的json数据序列化为python的字典或列表(对象)
    
    dumps(字典或列表[, ensure_ascii=False]): 将python的字典或列表/元组反序列化为json格式的字符串。
    dump(字典或列表, 文件对象[, ensure_ascii=False]): 将python的字典或列表/元组反序列化之后写入到json文件中。

"""

'''
with open("data.json", mode="r", encoding="utf-8") as f:
    text = f.read()
    # print(text, type(text))

result = json.loads(text)
print(result, type(result))

print(result.keys())
print(result.values())
'''

'''
with open("data.json", mode="r", encoding="utf-8") as f:
    res = json.load(f)

print(res, type(res))
'''

'''
datas = """
{
    "state":true,
    "message":"获取成功",
    "value":[
            {
                "id":"1806019323476156416",
                "alias":"onlineUserManager",
                "menuId":"1376480241760997376",
                "parentMenuId":"3441027",
                "href":"",
                "name":"在线用户",
                "userId":"1",
                "pkVal":"1806019323476156416"
            }
        ],
    "code":200
}
"""

res = json.loads(datas)
print(res["value"][0]["id"], type(res))
'''


dict1 = {
    "state": True,
    "message": "获取成功",
    "value": (
                {
                    "id": "1806019323476156416",
                    "alias": "onlineUserManager",
                    "menuId": "1376480241760997376",
                    "parentMenuId": "3441027",
                    "href": "",
                    "name": "在线用户",
                    "userId": "1",
                    "pkVal": "1806019323476156416"
                },{
                    "id": "1806019323476156416",
                    "alias": "onlineUserManager",
                    "menuId": "1376480241760997376",
                    "parentMenuId": "3441027",
                    "href": "",
                    "name": "在线用户",
                    "userId": "1",
                    "pkVal": "1806019323476156416"
                }
    ),
    "code": 20.0
}


# res = json.dumps(dict1, ensure_ascii=False)
# print(res, type(res))

with open("data1.json", mode="w", encoding="utf-8") as f:
    json.dump(dict1, f, ensure_ascii=False)