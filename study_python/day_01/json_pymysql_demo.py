# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      json_pymysql_demo.py
# Author:       lao_zhao
# Datetime:     2024/8/8 15:59
# Description:
# 
# ---------------------------------------------------------------------------
import pymysql
import json


conn = pymysql.connect(host="172.20.190.11",
                    port=3306,   # 端口号必须为整形
                    user="root",
                    password="123456",
                    database="test62",
                    charset="utf8"
               )
cursor = conn.cursor()

select_sentence = "select * from t_user limit 10;"
row = cursor.execute(select_sentence)

all_data = []
if row:
    select_result = cursor.fetchall()

    for row in select_result:
        row_dict = {}
        print(row)
        row_dict["id"] = row[0]
        row_dict["name"] = row[1]
        row_dict["address"] = row[2]
        row_dict["company"] = row[3]
        row_dict["phone"] = row[4]
        row_dict["email"] = row[5]
        # 处理时间
        create_time = row[6]
        create_time = create_time.strftime("%Y-%m-%d %H:%M:%S")
        row_dict["createTime"] = create_time
        all_data.append(row_dict)


with open("all_data1.json", mode="w", encoding="utf-8") as fp:
    json.dump(all_data, fp, ensure_ascii=False)