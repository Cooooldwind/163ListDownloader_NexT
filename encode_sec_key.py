'''
version: 1.0.0.231112a
docstring: 网易云weapi解码
author: CooooldWind_, 半岛的孤城
'''

import random
import json
from base64 import b64encode
import requests
from Crypto.Cipher import AES
from encoding_args import *

class NeteaseParams:
    '''解码类'''
    def __init__(self, encode_data, url):
        self.encode_data = encode_data
        self.url = url
        self.func_e = "010001"
        self.func_f = FUNC_F
        self.func_g = "0CoJUm6Qyw8W8jud"
        self.func_i = "vlgPRPyGhwA6F4Sq"
        self.encode_sec_key = SEC_KEY
    def to_hex(self, encode_data):
        '''16进制解码'''
        temp = 16 - len(encode_data) % 16
        return encode_data + chr(temp) * temp
    def encode_params(self, encode_data, encode_key):
        '''解码的关键函数(1)'''
        func_iv = "0102030405060708"
        encode_data = self.to_hex(encode_data)
        encode_aes = AES.new(key = encode_key.encode("utf-8"),
                            IV = func_iv.encode("utf-8"),
                            mode = AES.MODE_CBC)
        base64_sec_key = encode_aes.encrypt(encode_data.encode("utf-8"))
        return str(b64encode(base64_sec_key), "utf-8")
    def get_params(self, encode_data):
        '''解码的关键函数(2)'''
        return self.encode_params(
            self.encode_params(
                encode_data, self.func_g
            ), self.func_i
        )
    def get_resource(self):
        '''获取资源'''
        get_data = {
            'params': self.get_params(json.dumps(self.encode_data)),
            'encSecKey': self.encode_sec_key
        }
        get_headers = {
            'User-Agent': random.choice(USER_AGENTS)
        }
        return requests.post(self.url, data = get_data, headers = get_headers, timeout = 10).json()
