# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      pymysql_demo.py
# Author:       lao_zhao
# Datetime:     2024/8/8 14:01
# Description:
# 
# ---------------------------------------------------------------------------
import datetime

import pymysql
from faker import Faker

"""
    pymysql是python用来操作mysql数据库的。pymysql是第三方模块，需要下载。pip install pymysql
    
    
    pymysql操作mysql数据库的流程：
        1：链接数据库获取链接对象。   链接对象 = pymysql.connect(host, port, user, password, database, charset="utf8")
        2：根据链接对象获取游标对象。   游标对象 = 链接对象.cursor()
        3：使用游标对象的execute方法执行sql语句。
            注意：
                1：如果sql语句执行之后会影响表的数据结构。执行完sql语句之后需要使用链接对象提交。
                    游标对象.execute(sql增/删/改)
                    链接对象.commit()
                2：如果sql语句是查询语句。需要使用游标对象的fetchall/fetchone方法获取查询结果。
"""


# 创建链接对象
db = pymysql.connect(
                host="172.20.190.11",
                port=3306,   # 端口号必须为整形
                user="root",
                password="123456",
                database="test62",
                charset="utf8"
            )

# 创建游标对象
cursor = db.cursor()


# 执行sql语句
# insert语句
'''
insert_str = f"insert into t_user(name, address, company, phone, email, create_time) values ('张三2', '四川成都', '科技公司', '13777777777', 'zhangsan@qq.com','{datetime.datetime.now()}')"
# 使用游标对象的execute方法执行sql语句
row = cursor.execute(insert_str)
print(row)

# 链接对象提交
db.commit()
'''

'''
data = Faker(locale="zh_cn")

for _ in range(10000):
    sql_data = f"""insert into t_user(name, address, company, phone, email, create_time) 
                values ('{data.name()}', '{data.address()}', '{data.company()}', '{data.phone_number()}', '{data.email()}','{datetime.datetime.now()}');"""
    row = cursor.execute(sql_data)
    db.commit()
    if row == 1:
        print("插入数据成功")
    else:
        print("插入数据失败")
'''

# update语句
'''
update_str = """update t_user set name="张三2" where id=1;"""
row = cursor.execute(update_str)
print(row)
db.commit()
'''
'''
for i in range(1, 11):
    update_str = f"""update t_user set name="张三{i}号" where id={i};"""
    print(update_str)
    row = cursor.execute(update_str)
    db.commit()
    print(row)
'''

# delete语句
'''
del_str = """delete from t_user where id in (1, 2, 3, 4, 5)"""
row = cursor.execute(del_str)
print(row)
db.commit()
'''

# select语句
select_str = "Select id, name from t_user where id = 1;"
row = cursor.execute(select_str)
print(row)
# fetchall/fetchone
# fetchall获取所有的查询结果，返回值为二维元组
# select_result = cursor.fetchall()
# print(select_result)


# fetchone获取一条查询结果，返回值为元组，如果没有查询结果/查询结果取完，返回None。
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())

# for _ in range(row):
#     print(cursor.fetchone())