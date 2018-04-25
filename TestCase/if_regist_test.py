import unittest
import os
import requests
from public.TestApi import testApi
from public.read_csv import get_csv_data
from ddt import ddt, data, file_data, unpack
from conf.config import get_config


path=os.path.join(os.path.dirname(os.path.dirname(__file__)),"TestFile\if_regist.csv")
a=get_csv_data(path)
base_url=get_config()['host']
title="mobile"


#使用ddt 参数化
@ddt
class Test_if_regist(unittest.TestCase):
    @data(*a)
    #unpack,拆分序列(元组)
    @unpack
    def test_if_regist(self,*a):
        r=requests.get(base_url+a[0]+a[1])
        #1.查询成功时候断言
        if r.json()["code"]==0:
            self.assertEqual(a[-1], r.json()["result"]["mobile"])
        #查询失败时候断言
        else:
            self.assertEqual(int(a[-2]),r.json()["code"])
            self.assertEqual(a[-1],r.json()["error"])


if __name__ == '__main__':
    unittest.main(verbosity=2)
# url=base_url+a[0][0]
# data=a[0][1]
# print(url)
# print(data)
# print(url+data)
# r = requests.get(url+data)
# print(r.json())