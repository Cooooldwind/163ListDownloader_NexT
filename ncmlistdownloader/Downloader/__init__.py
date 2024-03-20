'''
ncmlistdownloader/Downloader/__init__.py
Core.Ver.1.0.0.240320a1
Author: CooooldWind_
Updated_Content:
1. Downloader()
'''

from ncmlistdownloader.Common import *
from ncmlistdownloader.Common.encode_sec_key import *
import requests
from requests.adapters import HTTPAdapter
import random
import time
import threading

class Downloader(threading.Thread):
    def __init__(self, url = "", stream = True, max_retries = 3):
        self.session = requests.Session()
        self.session.mount('http://', HTTPAdapter(max_retries = max_retries))
        self.session.mount('https://', HTTPAdapter(max_retries = max_retries))
        source = self.session.get(url = url,
                                  stream = stream,
                                  allow_redirects = True,
                                  timeout = (5,10))

'''
def download(url = "", filename = "", stream = True, max_retries = 3):
    session = requests.Session()
    session.mount('http://', HTTPAdapter(max_retries = max_retries))
    session.mount('https://', HTTPAdapter(max_retries = max_retries))
    with open(filename, 'wb') as file:
        rate = 0
        source = session.get(url = url,
                              stream = stream,
                              allow_redirects = True,
                              timeout = (5, 15))
        if stream:
            for data in source.iter_content(chunk_size = 1024):
                file.write(data)
                rate += len(data)
                if random.randint(0,1000) % 200 == 0:
                    time.sleep(0.01)
        else: file.write(source.content)
    
def response_get(url = "", data = dict()):
    return NeteaseParams(url = url, encode_data = data).get_resource()
'''