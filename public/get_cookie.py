import requests
from conf.config import get_config
from public.read_csv import get_csv_data

a=get_csv_data('login.csv')
base_url=get_config()['host']
title=["grant_type","client_id","client_secret","username","password","scope","device_token"]

s = requests.Session()
r=s.post(base_url+a[0][1],dict(zip(title,a[0][2:-2])))
# cookies=requests.utils.dict_from_cookiejar(r.cookies)
print(dict(zip(title,a[0][2:-2])))
# print(r.headers)
# print(r.json())
# print(r.cookies)
# print(r.cookies.get_dict())
# print(r.headers)

