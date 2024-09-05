# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      db.py
# Author:       lao_zhao
# Datetime:     2024/8/29 9:54
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
            database="eip8"
        )
        self.cursor = self.conn.cursor()

    def delete(self, sql):
        if sql.lower().strip().startswith("delete"):
            try:
                self.cursor.execute(sql)
            except Exception as e:
                print(f"执行时报错，错误为{e}")
                raise e
            else:
                self.conn.commit()
        else:
            raise ValueError("sql语句错误")