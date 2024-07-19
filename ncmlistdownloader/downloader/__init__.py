"""
ncmlistdownloader/Downloader/__init__.py
Core.Ver.x.x.x.240719
Author: CooooldWind_
"""

import threading
import requests
from requests.adapters import HTTPAdapter


class OriginFile(threading.Thread):
    def __init__(self, url: str):
        threading.Thread.__init__(self)
        self.session = requests.session()
        self.session.mount("http://", HTTPAdapter(max_retries=3))
        self.session.mount("https://", HTTPAdapter(max_retries=3))
        self.head = self.session.head(url=url,allow_redirects=True)
        self.url = self.head.url
        self.tot_size = 0 # 文件体积
        try:
            self.tot_size = int(dict(self.head.headers)['Content-Length'])
        except:
            self.tot_size = 0
        self.now_size = 0 # 当前下载的文件大小
        self.data = bytes() # 文件缓冲在这里了
        self.percentage = 0.00 # 百分比
        
    def run(self):
        try:
            source = self.session.get(url=self.url,stream=True)
            for now_data in source.iter_content(chunk_size=1024):
                self.data += now_data
                self.now_size += len(now_data)
                self.percentage = self.now_size / self.tot_size  // 0.001 / 1000 # 保留三位小数
        except Exception as exception: 
            print(exception)
        finally:
            return self.data
