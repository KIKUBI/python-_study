# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      main.py
# Author:       lao_zhao
# Datetime:     2024/8/14 15:21
# Description:
# 
# ---------------------------------------------------------------------------
import random

from study_python.cxy_zuoye.sele2zuoye.common.db import DB
from study_python.cxy_zuoye.sele2zuoye.common.read_excel import ReadExcel

from study_python.cxy_zuoye.sele2zuoye.page.org_page import OrgPage

if __name__ == '__main__':
    db = DB()
    excel = ReadExcel()
    org = OrgPage(browser=random.choice("c"))

    case_datas = excel.get_data()

    for data in case_datas:
        excel.write_result(row=data[-1], result="断言成功")
        if data[-3]:
           db.delete(data[-3])

        res = org.add_org(data[0], data[1],data[-1])

        if res == data[-2]:
            excel.write_result(row=data[-1], result="断言成功")
        else:
            excel.write_result(row=data[-1], result="断言失败")
    org.quitweb()
