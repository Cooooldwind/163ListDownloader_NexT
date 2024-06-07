"""
ncmlistdownloader/music/dwonload.py
Core.Ver.2.0.0.240607a1
Copyright @CooooldWind_
Following GNU_AGPLV3+ License
"""

import time
import threading
import requests
import traceback
from requests.adapters import HTTPAdapter

class OriginFile:
    def __init__(self, url = ""):
        # 获取重定向后的url
        head = requests.head(url = url, allow_redirects=True)
        self.url = head.url
        self.headers = dict(head.headers)
        try:
            self.total_size = int(self.headers["Content-Length"])
        except: 
            print(traceback.format_exc())
            pass

    