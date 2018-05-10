import unittest
import os
import requests
from public.TestApi import testApi
from public.read_csv import get_csv_data
from public.get_token import get_token
from ddt import ddt, data, file_data, unpack
from conf.config import get_config

base_url=get_config()['host']
a=get_csv_data('uddate_utags.csv')

"""
print(a)
for ai in a:
    r = requests.get(base_url + "/api/lebang/customer/" +ai[0] +"/" +ai[1]+"/tags",
                     headers={"Authorization": "Bearer" + ' ' + get_token()})
    print(r.json())
"""


#更新用户标签,需要登录
@ddt
class Test_update_utags(unittest.TestCase):
    @data(*a)
    @unpack
    def test_update_utags(self,*a):
        r=requests.put(base_url+"/api/lebang/customer/"+a[0]+"/"+a[1]+"/tags", headers={"Authorization": "Bearer"+' '+get_token()})
        #1.获取成功时候断言
        if r.json()["code"]==0:
            self.assertEqual([], r.json()["result"])
        #获取失败时候断言
        elif r.json()["code"]==2:
            self.assertEqual("无法找到资源",r.json()["error"])

        #请求失败
        else:
            raise Exception("请求错误！")

if __name__ == '__main__':
    unittest.main(verbosity=2)

