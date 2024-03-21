'''
ncmlistdownloader/Downloader/__init__.py
Core.Ver.1.0.0.240321a1
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

def calc_divisional_range(total_size, sum):
    step = total_size // sum
    arr = list(range(0, total_size, step))
    result = []
    for i in range(len(arr) - 1):
        s_pos, e_pos = arr[i], arr[i + 1] - 1
        result.append([s_pos, e_pos])
    result[-1][-1] = total_size - 1
    return result

class OriginFile:
    def __init__(self, url = ""):
        headers = {"Range": f"bytes=1-2"}
        self.headers = dict(requests.head(url = url).headers)
        self.total_size = int(self.headers['Content-Length'])
        self.chunks = calc_divisional_range(self.total_size, 10)
        self.url = url

    def start(self, stream = True, max_retries = 3, thread_sum = 4, filename = str()):
        downloader_list = list()
        for i in self.chunks:
            downloader_list.append(Downloader(url = self.url,
                                              chunk = i,
                                              stream = stream,
                                              max_retries = max_retries,
                                              thread_sum = thread_sum,
                                              filename = filename))
        for i in downloader_list:
            i.start()
    
class Downloader(threading.Thread):
    '''
    每个部分文件的下载
    '''
    def __init__(self, url = "", chunk = [], stream = True, max_retries = 3, thread_sum = 4, filename = str()):
        threading.Thread.__init__(self)
        self.start_pos = chunk[0]
        self.end_pos = chunk[1]
        self.session = requests.Session()
        self.session.mount('http://', HTTPAdapter(max_retries = max_retries))
        self.session.mount('https://', HTTPAdapter(max_retries = max_retries))
        self.source = self.session.get(url = url,
                                  stream = stream,
                                  allow_redirects = True,
                                  timeout = (5,10),
                                  headers = {
                                      "Range": f"bytes={self.start_pos}-{self.end_pos}"
                                  })
        self.headers = dict(self.source.headers)
        self.total_size = int(self.headers['Content-Length'])
        self.thread_sum = thread_sum
        self.filename = filename
        
    def run(self):
        with threading.Semaphore(self.thread_sum):
            with open(self.filename, 'wb+') as file:
                file.seek(self.start_pos)
                rate = 0
                for data in self.source.iter_content(chunk_size = 1024):
                    file.write(data)
                    rate += len(data)
                    if random.randint(0,1000) % 200 == 0:
                        time.sleep(0.01)

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