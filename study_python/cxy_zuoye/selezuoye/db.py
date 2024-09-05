# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      db.py
# Author:       lao_zhao
# Datetime:     2024/8/13 17:29
# Description:
# 
# ---------------------------------------------------------------------------
import pymysql


class DB:
    def __init__(self):
        self.conn = pymysql.connect(
            host="36.139.193.99",
            port=3306,
            user="root",
            password="Rhrc@2024",
            database="eip8",
            charset="utf8"
        )
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def delete(self, sql_data):
        sql = sql_data.lower().strip()
        if sql.startswith("delete"):
            try:
                self.cursor.execute(sql_data)
                self.conn.commit()
            except Exception as e:
                print(f"错误的类型为：{e.__class__.__name__}, 错误的描述为：{e}")
                raise e
        else:
            raise ValueError("sql语句错误")