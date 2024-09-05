# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      eg_1.py
# Author:       lao_zhao
# Datetime:     2024/8/9 9:52
# Description:
# 
# ---------------------------------------------------------------------------
"""将数据库的数据存放到excel中"""
from study_python.day_12.example.eg_2 import ExcelFunc
from study_python.day_13.example.common.db import DB

'''
# 创建链接对象、游标对象、execute执行sql语句---commit，fetchall/fetchone
# 构造sql语句
sql_data = "select * from t_user limit 3000;"
# 创建DB类对象
db = DB()
# 使用DB类对象调用select_all执行查询sql语句
select_res = db.select_all(sql_data)
# 判断查询的结果是否不为None，不为None提取数据
if select_res is not None:
    # 创建存放数据的excel  --- 工作簿--工作表
    excel = ExcelFunc("./datas.xlsx", "t_user")
    # 给工作表设计表头
    excel.ws.append(["编号", "姓名", '地址', "公司", "手机号", "email", "创建时间"])
    # 将查询结果使用append方式追加到excel的工作表中
    # 设置编号
    number = 1
    for i in select_res:
        # 将每条查询结果转成列表
        list_i = list(i)
        # 将列表中的第一个元素的值改成number的值
        list_i[0] = number
        # number的值加1
        number += 1
        # 将列表追加到工作表中
        excel.ws.append(list_i)
    excel.wb.save(excel.excel_path)
'''


if __name__ == '__main__':
    # 构造sql语句
    sql_data = "select * from t_user limit 3000;"
    # 创建DB类对象
    db = DB()
    # 使用DB类对象调用select_all执行查询sql语句
    select_res = db.select_all(sql_data)
    # 判断查询的结果是否不为None，不为None提取数据
    if select_res is not None:
        excel = ExcelFunc("./datas_all.xlsx", "t_user")
        excel.write_table_data(list(select_res), title=["编号", "姓名", '地址', "公司", "手机号", "email", "创建时间"])
