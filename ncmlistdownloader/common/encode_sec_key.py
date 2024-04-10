'''
网易云WeAPI解码
Core.Ver.1.0.0.240410a1
Author: CooooldWind_, 半岛的孤城
References: 
1. 网易云解参数（获取网易云歌词，获取评论同理）[https://www.bilibili.com/read/cv12754897/]
'''

import random
import json
from base64 import b64encode
import requests
from Crypto.Cipher import AES
from ncmlistdownloader.common.global_args import USER_AGENTS, FUNC_F, SEC_KEY

class NeteaseParams:
    '''
    WeAPI解码类
    ----------
    参数：
    1. `encode_data`: 传入的参数
    2. `url`: API的URL
    '''
    def __init__(self, encode_data, url):
        self.encode_data = encode_data
        self.url = url
        self.func_e = "010001"
        self.func_f = FUNC_F
        self.func_g = "0CoJUm6Qyw8W8jud"
        self.func_i = "vlgPRPyGhwA6F4Sq"
        self.encode_sec_key = SEC_KEY
    def __to_hex(self, encode_data):
        '''16进制解码'''
        temp = 16 - len(encode_data) % 16
        return encode_data + chr(temp) * temp
    def __encode_params(self, encode_data, encode_key):
        '''解码的关键函数(1)'''
        func_iv = "0102030405060708"
        encode_data = self.__to_hex(encode_data)
        encode_aes = AES.new(key = encode_key.encode("utf-8"),
                            IV = func_iv.encode("utf-8"),
                            mode = AES.MODE_CBC)
        base64_sec_key = encode_aes.encrypt(encode_data.encode("utf-8"))
        return str(b64encode(base64_sec_key), "utf-8")
    def __get_params(self, encode_data):
        '''解码的关键函数(2)'''
        return self.__encode_params(
            self.__encode_params(
                encode_data, self.func_g
            ), self.func_i
        )
    def get_resource(self, cookies = None):
        '''获取资源'''
        get_data = {
            'params': self.__get_params(json.dumps(self.encode_data)),
            'encSecKey': self.encode_sec_key
        }
        get_headers = {
            'User-Agent': random.choice(USER_AGENTS)
        }
        response = requests.post(self.url,
                             data = get_data,
                             headers = get_headers,
                             cookies = cookies,
                             timeout = 10)
        return response.json()
