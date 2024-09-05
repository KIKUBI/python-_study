# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      dict_demo.py
# Author:       lao_zhao
# Datetime:     2024/7/26 14:39
# Description:
# 字典
# ---------------------------------------------------------------------------


"""
    字典：由键值对组成，键值对的格式：{键1:值1, 键2: 值2}

    字典的声明：
        变量 = dict()
        变量 = {}
        变量 = {key: value}
    注意：字典的键只能为不可变类型--字典中的值可以为任意类型
            int，float(浮点数可能会丢失精度), 字符串, 元组(元组中的元素如果有列表/字典不可以)
"""
"""
    字典的特点：
        1：字典在3.7以前是无序的，3.7版本以后是有序的。
        2：字典的元素为键值对，字典为可变类型。
    
    字典的操作：
        获取：
            字典[key] ：获取字典中key对应的值,如果key不存在要报错
            get(key): 获取字典中key对应的值,如果key不存在不报错
            keys(): 获取字典中所有的key，可以转成列表. list(dict_keys)
            values(): 获取字典中所有的value，可以转成列表. list(dict_values)
            items(): 获取字典中所有的键值对，可以转成列表. list(dict_items)
        增加：
        更改：
        删除：
        
"""

'''
dict1 = dict()
print(dict1, type(dict1))

dict2 = {}
print(dict2, type(dict2))

dict3 = {"name": "tom", "Age": 18, "price": 3.14}
print(dict3)
'''
# 字典的键必须为不可变类型-
'''
d1 = {
    1.1: "成都",
    2: "绵阳",
    "address": ["成都高新区", "孵化园"],
    {"name": "tome"}: 100,
    (1, 2, 3, {"1": "2"}): "可选项",
    # [3, 4, 5]: "错误项"
}
print(d1)


d2 = {
    "data": [
        {1: "A"},
        {2: "B"}
    ],
    "data1": 33.123,
    "data2": {"name": "张三"},
    "data3": (1, 2, 3),
    "data4": "数据",
    "data5": (1,)
}

print(d2)
'''

# 获取
# 字典[key]
dict1 = {
    1: [1, 2, 3],
    2: "hello",
    3: "python",
    "name": "张三",
    "status": "我想睡觉！！"
}

print(dict1[1])
print(dict1[2])
print(dict1[3])
print(dict1["status"])

# get(key)
print(dict1.get("status1"))   # None-->空   null  nil None

# keys, values, items

dict1_keys = dict1.keys()
print(dict1_keys, type(dict1_keys))   # 可迭代和不可得迭代
print(list(dict1_keys))

dict1_values = dict1.values()
print(dict1_values, type(dict1_values))
print(list(dict1_values))

dict1_items = dict1.items()
print(dict1_items, type(dict1_items))
print(list(dict1_items))

# for i in dict1.keys():
#     print(i)