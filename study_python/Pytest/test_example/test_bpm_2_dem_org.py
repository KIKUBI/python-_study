# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      test_case.py
# Author:       lao_zhao
# Datetime:     2024/9/2 16:55
# Description:
# 
# ---------------------------------------------------------------------------
import pytest


class TestBPMDem:
    host = 'http://36.139.193.99:8088'
    def test_add_dem(self, fix_req, fix_db, fix_dependency):
        # 判断Session对象中是否有token，如果有再添加维度，如果没有之间报错
        if "Authorization" in fix_req.headers.keys():
            # 配置添加维度的数据
            add_dem_url = self.host + "/api/demension/v1/dem/addDem"
            add_dem_data = {
                    "code": "二郎酱",
                    "description": "你不在的日子，我每天都在想你",
                    "isDefault": 0,
                    "name": "空空"
                }
            # 添加维度之前需要删除数据库中已存在的维度
            fix_db.delete(f"""delete from uc_demension where CODE_="{add_dem_data["code"]}";""")
            # 发送请求
            res = fix_req.request(method="post", url=add_dem_url, json=add_dem_data)
            # 断言
            try:
                assert "添加维度成功" in res.text
            except AssertionError:
                raise AttributeError("断言失败")
            else:
                dem_id = fix_db.select(f"""select ID_ from uc_demension where CODE_="{add_dem_data["code"]}";""")
                fix_dependency["demId"] = dem_id
        else:
            raise ValueError("Session对象中没有token")


class TestBPMOrg:
    host = 'http://36.139.193.99:8088'
    def test_add_org(self, fix_req, fix_db, fix_dependency,):
        if "Authorization" in fix_req.headers.keys():
        #配置组织信息
            add_org_url = self.host + "/api/org/v1/org/addOrg"
            listd = ['亢金龙', '小黄龙', '大圣残躯']
            for i in listd:
                add_org_data = {
                            "code": f"{i}plus",
                            "demId": f"{fix_dependency['demId'][0][0]}",
                            "exceedLimitNum": 0,
                            "grade": "",
                            "limitNum": 0,
                            "name": f"{i}",
                            "nowNum": 0,
                            "orderNo": 0,
                            "parentId": "0"
                    }
                # 添加维度之前需要删除数据库中已存在的维度
                fix_db.delete(f"""delete from uc_org where CODE_="{add_org_data["code"]}";""")
                org_result =fix_req.request(method="post", url=add_org_url, json=add_org_data)
                # 断言
                try:
                    assert "添加组织成功" in org_result.text
                except AssertionError:
                    raise AttributeError("断言失败")
        else:
            raise ValueError("Session对象中没有token")


if __name__ == '__main__':
    pytest.main()