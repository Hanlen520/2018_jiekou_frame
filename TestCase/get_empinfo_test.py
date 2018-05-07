import unittest
import os
import requests
from public.TestApi import testApi
from public.read_csv import get_csv_data
from public.get_token import get_token
from ddt import ddt, data, file_data, unpack
from conf.config import get_config

base_url=get_config()['host']

#获取当前员工信息,需要登录
class Test_eminfo(unittest.TestCase):
    #用户登录了
    def test_eminfo1(self):
        r=requests.get(base_url+"/api/lebang/staffs/me/detail", headers={"Authorization": "Bearer"+' '+get_token()})
        #1.查询成功时候断言
        if r.json()["code"]==0:
            self.assertEqual("菜头1234", r.json()["result"]["nickname"])
            self.assertIn("http://7xnc5a.com2",r.json()["result"]["avatar_url"])
        #请求失败
        else:
            raise Exception("请求错误！")
    #用户未登录
    def test_eminfo2(self):
        r = requests.get(base_url + "/api/lebang/staffs/me/detail")
        self.assertEqual(123,r.json()['code'])
        self.assertEqual("请重新登录",r.json()["error"])

if __name__ == '__main__':
    unittest.main(verbosity=2)


