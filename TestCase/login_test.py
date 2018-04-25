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

title=["grant_type","client_id","client_secret","username","password","scope,device_token"]


@ddt
class Test_login(unittest.TestCase):
    @data(*a)
    @unpack
    def test_login(self,*a):
        r=requests.post(base_url+a[1],dict(zip(title,a[2:-2])))
        #1.登录成功断言
        if r.json()["code"]==0:
            self.assertEqual(int(a[-1]), r.json()["result"]["expires_in"])
        else:
            self.assertEqual(int(a[-2]), r.json()["code"])
            self.assertEqual(a[-1], r.json()["error"])


if __name__ == '__main__':
    unittest.main(verbosity=2)

