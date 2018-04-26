import unittest
import os
import requests
from public.TestApi import testApi
from public.read_csv import get_csv_data
from ddt import ddt, data, file_data, unpack
from conf.config import get_config


path=os.path.join(os.path.dirname(os.path.dirname(__file__)),"TestFile\login.csv")
a=get_csv_data(path)
base_url=get_config()['host']
loginout_url="/api/lebang/oauth/revoke"
title=["grant_type","client_id","client_secret","username","password","scope","device_token"]


class Test_loginout(unittest.TestCase):
    def test_loginout(self):
        r=requests.post(base_url+a[0][1],dict(zip(title,a[0][2:-2])))
        #1.登录成功断言
        if r.json()["code"]==0:
            print(base_url+loginout_url)
            r1=requests.post(base_url+loginout_url,{"token":"Bearer"+' '+r.json()["access_token"]})
            if r1.json()["code"]==0:
                self.assertEqual(r1.json()["result"],None)
            else:
                raise Exception(u"登出失败")
        else:
            raise Exception(u"登录失败")


if __name__ == '__main__':
    unittest.main(verbosity=2)

