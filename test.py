import requests
import json
import hashlib
import base64
import pprint
from Crypto.Cipher import AES
from ncmlistdownloader.encode import NeteaseParams
from ncmlistdownloader.global_args import *

# 设置请求体
phone = str(input("phone:"))
password = str(input("password:"))

d = {
    'phone': phone,
    'password': password,
    "rememberLogin":"true",
    "checkToken":"",
    "csrf_token": ""
}
p = NeteaseParams(url = "", encode_data=d)
dd = p.get_data()

# 构造登录请求并保持Session状态
session = requests.Session()
session.post('http://music.163.com/weapi/login/cellphone', data=dd)

pprint.pprint(session.cookies)