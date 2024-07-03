"""
ncmlistdownloader/encode.py
Core.Ver.2.0.0.240703a2
Copyright @CooooldWind_
Following GNU_AGPLV3+ License
"""

import random
import json
from base64 import b64encode
import requests
from Crypto.Cipher import AES

# from ncmlistdownloader.global_args import USER_AGENTS, FUNC_F, SEC_KEY
import ncmlistdownloader.global_args as global_args


class NeteaseParams:
    """
    WeAPI解码类
    ----------
    参数：
    1. `encode_data`: 传入的参数
    2. `url`: API的URL
    """

    def __init__(self):
        self._func_e = "010001"
        self._func_f = global_args.FUNC_F
        self._func_g = "0CoJUm6Qyw8W8jud"
        self._func_i = "vlgPRPyGhwA6F4Sq"
        self._encode_sec_key = global_args.SEC_KEY
        self.session = requests.session()

    def _to_hex(self, encode_data):
        """16进制解码"""
        temp = 16 - len(encode_data) % 16
        return encode_data + chr(temp) * temp

    def _encode_params(self, encode_data, encode_key: str):
        """解码的关键函数(1)"""
        func_iv = "0102030405060708"
        encode_data = self._to_hex(encode_data)
        encode_aes = AES.new(
            key=encode_key.encode("utf-8"),
            IV=func_iv.encode("utf-8"),
            mode=AES.MODE_CBC,
        )
        base64_sec_key = encode_aes.encrypt(encode_data.encode("utf-8"))
        return str(b64encode(base64_sec_key), "utf-8")

    def _get_params(self, encode_data):
        """解码的关键函数(2)"""
        return self._encode_params(
            self._encode_params(encode_data, self._func_g), self._func_i
        )

    def get_resource(self, cookies=None, encode_data = None, url = ""):
        """获取资源"""
        get_data = {
            "params": self._get_params(json.dumps(encode_data)),
            "encSecKey": self._encode_sec_key,
        }
        get_headers = {"User-Agent": random.choice(global_args.USER_AGENTS)}
        response = self.session.post(
            url, data=get_data, headers=get_headers, cookies=cookies, timeout=10
        )
        return response.json()
