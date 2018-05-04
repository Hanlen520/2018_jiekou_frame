import unittest
import os
import requests
from public.TestApi import testApi
from public.read_csv import get_csv_data
from ddt import ddt, data, file_data, unpack
from conf.config import get_config


base_url=get_config()['host']
print(base_url)

r=requests.get(base_url+"/api/lebang/staffs/me/detail")
print(r.status_code)

"""
#使用ddt 参数化
@ddt
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
