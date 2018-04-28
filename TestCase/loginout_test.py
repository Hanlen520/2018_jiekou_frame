import unittest
import os
import requests
from public.TestApi import testApi
from public.read_csv import get_csv_data
from ddt import ddt, data, file_data, unpack
from conf.config import get_config


a=get_csv_data('loginout.csv')
base_url=get_config()['host']
loginout_url="/api/lebang/oauth/revoke"
title=["grant_type","client_id","client_secret","username","password","scope","device_token"]

@ddt
class Test_loginout(unittest.TestCase):
    def test_loginout(self):
        r=requests.post(base_url+a[0][1],dict(zip(title,a[0][2:-3])))
        #1.登录成功断言
        if r.json()["code"]==0:
            print(base_url+loginout_url)
            r1=requests.post(base_url+loginout_url,{"token":"Bearer"+' '+r.json()["access_token"]})

            #登出成功
            if r1.json()["code"]==0:
                self.assertEqual(r1.json()["result"],None)
            else:
                raise Exception(u"登出失败")
        else:
            raise Exception(u"登录失败")

    @data(*a)
    @unpack
    def test_loginout_fail(self,*a):
        r2 = requests.post(base_url+loginout_url, {"token":a[-1]})
        if r2.json()["code"]==282:
            self.assertEqual(r2.json()["error"],'已经登出或者 code 错误')
        else:
            raise Exception("HTTP，请求失败")


if __name__ == '__main__':
    unittest.main(verbosity=2)

