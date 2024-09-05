# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      db.py
# Author:       lao_zhao
# Datetime:     2024/9/2 17:11
# Description:
# 
# ---------------------------------------------------------------------------
import pymysql


class DB:
    def __init__(self):
        self.conn = pymysql.connect(
            host='36.139.193.99',
            port=3306,
            user="root",
            password='Rhrc@2024',
            database='eip8'
        )
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def delete(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def select(self, sql):
        self.cursor.execute(sql)
        select_res = self.cursor.fetchall()
        return select_res