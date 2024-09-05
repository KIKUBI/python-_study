# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   RONGHUA
# FileName:      day01.py
# Author:       陈啸宇
# Datetime:     2024/7/26 16:55
# Description:
# ---------------------------------------------------------------------------
#1、从控制台输入3个整数，放到一个列表中输出？
# a = input("请输入第一个整数：")
# b = input("请输入第二个整数：")
# c = input("请输入第三个整数：")
# list = [a, b, c]
# print(list)
#2、将列表list1=[“hello”, “world”, “你好”, “成都”]中的每个元素拼接为一个字符串？
list1 = ["hello", "world", "你好", "成都"]
str1 = str("".join(list1))
print(str1,type(str1))
#3、修改元组tup1=(1, 2, 3, 4)中第一个元素和最后一个元素的值为”hello”和”python”？
tup1 = (1, 2, 3, 4)
list1 = list(tup1)
list1[0] = "hello"
list1[-1] = "python"
print('第3题',tuple(list1))
#4、列表list1=[1, 2, 3, -1, 30, 1, 18]，找出列表中的最大值、最小值，并对列表进行降序排列？
list1 = [1, 2, 3, -1, 30, 1, 18]
print(max(list1), min(list1), sorted(list1, reverse=True))
#5、将列表list1=[“a”, “b”, “c”]转成字符串”cba”？
list1 = ["a", "b", "c"]
str1 = str("".join(list1)[::-1])
print(str1)
#6、创建一个依次包含键-值对{'name': 'Niuniu'和'Student ID': 1}的字典my_dict_1？
my_dict_1={'name': 'Niuniu','Student ID': 1}
#7、创建一个依次包含键-值对{'name': 'Niumei'和'Student ID': 2}的字典my_dict_2？
my_dict_2={'name': 'Niumei','Student ID': 2}
#8、创建一个依次包含键-值对{'name': 'Niu Ke Le'和'Student ID': 3}的字典my_dict_3？
my_dict_3={'name': 'Niu Ke Le','Student ID': 3}
#9、创建一个空列表dict_list，依次将字典my_dict_1、my_dict_2和my_dict_3添加到dict_list里？
dict_list = []
for i in (my_dict_1,my_dict_2,my_dict_3):
    dict_list.append(i)
print('第9题',dict_list)
#有字典dict_1 = {‘a’: ‘apple’, ‘b’: ‘banana’, ‘o’: ‘orange’, ‘g’: ‘grape’}，对dict_1依次完成如下操作：
dict_1 ={'a': 'apple', 'b': 'banana', 'o': 'orange', 'g': 'grape'}
#添加字典元素 l:lemon；
dict_1['l'] = 'lemon'
#修改键a对应的值为Apple
dict_1['a'] = 'Apple'
#删除键g对应的字典元素；
dict_1.pop('g')
#获取字典的所有键，输出列表
print(list(dict_1.keys()),type(list(dict_1.keys())))
#获取字典的所有值，输出列表
print(list(dict_1.values()),type(list(dict_1.values())))
#获取字典的所有键值对，输出列表
print(list(dict_1.items()),type(list(dict_1.items())))
#有如下字典dict1，获取字典中所有的title对应的值，放到一个列表中？
dict1 = {
    "store": {
      "book": [
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "price": 8.99
      }
    ]
  }
}
listcxy = []
for i in (0,1,2):
  listcxy.append(dict1['store']['book'][i]['title'])
print(listcxy ,type(listcxy))
