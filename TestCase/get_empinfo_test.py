import unittest
import os
import requests
from public.TestApi import testApi
from public.read_csv import get_csv_data
from ddt import ddt, data, file_data, unpack
from conf.config import get_config


base_url=get_config()['host']


a=get_csv_data('login.csv')
title=["grant_type","client_id","client_secret","username","password","scope","device_token"]

s = requests.Session()
r=s.post(base_url+a[0][1],dict(zip(title,a[0][2:-2])))
# print(r.json()["access_token"])
# print(r.json())


r1=requests.get(base_url+"/api/lebang/staffs/me/detail",params={"token":"Bearer"+' '+r.json()["access_token"]})
print(r1.request.headers)
print(r1.json())



"""
#获取当前员工信息,需要登录
class Test_eminfo(unittest.TestCase):
    def test_eminfo(self):
        r=requests.get(base_url+"/api/lebang/staffs/me/detail")
        #1.查询成功时候断言
        if r.json()["code"]==0:
            self.assertEqual(a[-1], r.json()["result"]["mobile"])
        #查询失败时候断言
        else:
            self.assertEqual(int(a[-2]),r.json()["code"])
            self.assertEqual(a[-1],r.json()["error"])


if __name__ == '__main__':
    unittest.main(verbosity=2)
"""

