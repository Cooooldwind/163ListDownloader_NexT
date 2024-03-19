'''
ncmlistdownloader/Downloader/common.py
Core.Ver.1.0.0.240319a1
Author: CooooldWind_
Updated_Content:
1. fix: download(url, filename, stream, max_retries)
'''

from ncmlistdownloader.Common import *
import requests
from requests.adapters import HTTPAdapter
import random
import time

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
    

