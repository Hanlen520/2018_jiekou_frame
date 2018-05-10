import unittest
import os
import requests
from public.TestApi import testApi
from public.read_csv import get_csv_data
from public.get_token import get_token
from ddt import ddt, data, file_data, unpack
from conf.config import get_config

base_url=get_config()['host']
alltags_url='/api/lebang/customer/tags'


"""
r = requests.get(base_url +alltags_url,
                 headers={"Authorization": "Bearer" + ' ' + get_token()})
print(r.json()["result"][0])
"""

#获取全部标签,需要登录
class Test_get_alltags(unittest.TestCase):
    def test_get_alltags(self):
        r=requests.get(base_url+alltags_url, headers={"Authorization": "Bearer"+' '+get_token()})
        #1.获取成功时候断言
        if r.json()["code"]==0:
            self.assertEqual(5, len(r.json()["result"]))
            self.assertEqual({'type': '其他', 'tags': [{'id': 23, 'name': '自己做饭'},
            {'id': 24, 'name': '常点外卖'}, {'id': 25, 'name': '无饮水机'}]},r.json()["result"][0])
            
        #请求失败
        else:
            raise Exception("请求错误！")

if __name__ == '__main__':
    unittest.main(verbosity=2)

