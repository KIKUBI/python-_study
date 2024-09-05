# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      jsonpath_demo.py
# Author:       lao_zhao
# Datetime:     2024/8/29 16:52
# Description:
# 
# ---------------------------------------------------------------------------
import json
import re

import jsonpath


"""
    jsonpath: 功能：使用jsonpath表达式匹配python中字典中的键值对或列表的元素
    pip install jsonpath
    
    jsonpaht表达式：
        $: 根节点
        .：子节点
        ..: 任意节点
        *: 通配符
        @: 当前节点对象
        []:
            [n]：获取第n个子节点
            [n1, n2]：根据多个下标获取子节点
            [n1:n2]：根据下标的切片获取子节点
            ['key']：获取key对应的值
            ['key1','key2']:获取多个key对应的值
            [?(bool表达式)]：根据表达式过滤子节点
"""
"""
    jsonpath(python的字典或列表, r'jsonpath表达式')：根据jsonpath表达式匹配python中字典中的键值对或列表的元素，返回值类型为列表。
"""


data = """
{
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
            },
            {
                "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
            },
            {
                "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99
            },
            {
                "category": "fiction",
                "author": "J. R. R. Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
            }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    },
    "expensive": 10
}
"""

dict1 = json.loads(data)

# 获取字典中store的数据
print("获取字典中store的数据", jsonpath.jsonpath(dict1, r"$.store"))
# 获取字典中store下book对应的值
print("获取字典中store下book对应的值", jsonpath.jsonpath(dict1, r"$.store.book"))
# 获取字典中store下book下第一个元素的值
print("获取字典中store下book下第一个元素的值", jsonpath.jsonpath(dict1, r"$.store.book[0]"))
# 获取book下第一个元素和第二个元素的值
print("获取book下第一个元素和第二个元素的值", jsonpath.jsonpath(dict1, r"$.store.book[0,1]"))
# 获取book下第二本书和最后一本书
print("获取book下第二本书和最后一本书", jsonpath.jsonpath(dict1, r"$.store.book[1,3]"))
# 获取book下第二本书到最后一本书
print("获取book下第二本书到最后一本书", jsonpath.jsonpath(dict1, r"$.store.book[1:4]"))
# 获取book下第二本书到最后一本书的价格
print("获取book下第二本书到最后一本书的价格", jsonpath.jsonpath(dict1, r"$.store.book[1:4].price"))
# 获取book下第二本书到最后一本书的价格和作者
print("获取book下第二本书到最后一本书的价格和作者", jsonpath.jsonpath(dict1, r"$.store.book[1:4].['price','author']"))
# 获取book节点下价格大于10的书籍
print("获取book节点下价格大于10的书籍", jsonpath.jsonpath(dict1, r"$..book.[?(@.price>10)]"))
# 获取book节点下价格大于10的书籍作者为J. R. R. Tolkien的书籍
print("获取book节点下价格大于10的书籍作者为J. R. R. Tolkien的书籍", jsonpath.jsonpath(dict1, r'$..book.[?(@.price>10 and @.author=="J. R. R. Tolkien")]'))
# 获取book节点下价格小于于10的或者有isbn的key的书籍
print("获取book节点下价格小于于10的或者有isbn的key的书籍", jsonpath.jsonpath(dict1, r"$..book.[?(@.price<10 or @.isbn)]"))  # 判断某个key是否存在时一定放在条件的最后
print("获取book节点下价格小于于10的或者有isbn的key的书籍", jsonpath.jsonpath(dict1, r"$..book.[?(@.isbn or @.price<10)]"))


with open("tb.json", mode="r", encoding="utf-8") as f:
    obj = json.load(f)

items = jsonpath.jsonpath(obj, r"$.data.itemsArray")

for item in items[0]:
    print("title", re.sub(r"[<>spancls=H/\s]", "", jsonpath.jsonpath(item, r"$.title")[0]), end="\t")
    print("price", jsonpath.jsonpath(item, r"$.price"), end="\t")
    print("付款人数", jsonpath.jsonpath(item, r"$.realSales"))