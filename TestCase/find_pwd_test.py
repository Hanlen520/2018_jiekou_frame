import unittest
import os
import requests
from public.TestApi import testApi
from public.read_csv import get_csv_data
from ddt import ddt, data, file_data, unpack
from conf.config import get_config

a=get_csv_data('find_pwd.csv')
base_url=get_config()['host']
find_pwd_url="/api/lebang/staffs/me/password/find"
title=["mobile","verify_code","password"]


@ddt
class Test_find_pwd(unittest.TestCase):
    def test_find_pwds(self,*a):
        r=requests.post(base_url+find_pwd_url,data=dict(zip(title,a)))
        #1.修改成功后
        if r.json()["code"]==0:
            self.assertEqual(a[-1], r.json()["result"]["mobile"])
        #查询失败时候断言
        else:
            self.assertEqual(int(a[-2]),r.json()["code"])
            self.assertEqual(a[-1],r.json()["error"])

    def test_find_pwdf(self):
        r=requests.post(base_url+find_pwd_url,data=dict(zip(title,a)))
        #1.修改成功后
        if r.json()["code"]==0:
            self.assertEqual(a[-1], r.json()["result"]["mobile"])
        #查询失败时候断言
        else:
            self.assertEqual(int(a[-2]),r.json()["code"])
            self.assertEqual(a[-1],r.json()["error"])

if __name__ == '__main__':
    unittest.main(verbosity=2)