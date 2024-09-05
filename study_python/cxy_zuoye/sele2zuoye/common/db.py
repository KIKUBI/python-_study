# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      db.py
# Author:       lao_zhao
# Datetime:     2024/8/14 15:44
# Description:
# 
# ---------------------------------------------------------------------------
import pymysql

from study_python.cxy_zuoye.sele2zuoye.common.read_ini import ReadIni


class DB:
    def __init__(self):
        """根据配置文件中数据库链接信息链接数据库，并获取链接对象，再获取游标对象"""
        # 根据配置文件中数据库链接信息链接数据库
        # 1: 创建ReadIni对象，并调用get_sql_connect_msg获取数据链接信息
        ini = ReadIni()
        host = ini.get_sql_connect_msg("host")
        port = int(ini.get_sql_connect_msg("port"))
        user = ini.get_sql_connect_msg("user")
        pwd = ini.get_sql_connect_msg("pwd")
        database = ini.get_sql_connect_msg("database")
        # 获取链接对象
        self.conn = pymysql.connect(host=host, port=port, user=user, password=pwd, database=database, charset="utf8")
        # 再获取游标对象
        self.cursor = self.conn.cursor()

    def __del__(self):
        # 先关闭游标对象再关闭链接对象
        self.cursor.close()
        self.conn.close()

    def delete(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()


if __name__ == '__main__':
    db = DB()