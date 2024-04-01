'''
ncmlistdownloader/Downloader/__init__.py
Core.Ver.1.0.0.240401a2
*Didn't test the new function.
Author: CooooldWind_
'''

import random
import time
import threading
import requests
from requests.adapters import HTTPAdapter
from ncmlistdownloader.common import *
from ncmlistdownloader.common.encode_sec_key import *

def calc_divisional_range(total_size, chunk_sum):
    '''
    calc_divisional_range
    '''
    step = total_size // chunk_sum
    arr = list(range(0, total_size, step))
    result = []
    for i in range(len(arr) - 1):
        s_pos, e_pos = arr[i], arr[i + 1] - 1
        result.append([s_pos, e_pos])
    result[-1][-1] = total_size - 1
    return result

class OriginFile:
    '''
    OriginFile
    '''
    def __init__(self, url = ""):
        self.headers = dict(requests.head(url = url).headers)
        self.total_size = int(self.headers['Content-Length'])
        self.chunks = calc_divisional_range(self.total_size, self.total_size // 1048576)
        self.url = url

    def auto_start(self, filename = str()):
        '''
        自动寻找合适的方式下载。
        默认<=1MB使用单线程，其他多线程。
        '''
        if self.total_size <= 1048576 * 1:
            self.single_thread_start(filename = filename)
        else:
            self.multi_thread_start(thread_sum = 8, filename = filename)

    def single_thread_start(self, stream = True, max_retries = 3, filename = str()):
        '''
        单线程运行参数。
        异步策略。
        '''
        arg_dict = {
                'url': self.url,
                'chunk': [0,1],
                'stream': stream,
                'max_retries': max_retries,
                'thread_sum': 1,
                'filename': filename
            }
        downloader = Downloader(**arg_dict)
        downloader.start()

    def multi_thread_start(self, stream = True, max_retries = 3, thread_sum = 4, filename = str()):
        '''
        多线程运行参数
        '''
        downloader_list: list[Downloader] = []
        for i in self.chunks:
            arg_dict = {
                'url': self.url,
                'chunk': i,
                'stream': stream,
                'max_retries': max_retries,
                'thread_sum': thread_sum,
                'filename': filename
            }
            downloader_list.append(Downloader(**arg_dict))
        for i in downloader_list:
            i.start()

class Downloader(threading.Thread):
    '''
    每个（部分）文件的下载
    '''
    def __init__(self,
                 url = "",
                 chunk = None,
                 stream = True,
                 max_retries = 3,
                 thread_sum = 4,
                 filename = str()):
        if not chunk:
            raise ValueError("\"chunk\" must be a list.")
        threading.Thread.__init__(self)
        self.start_pos = chunk[0]
        self.end_pos = chunk[1]
        self.url = url
        self.stream = stream
        self.session = requests.Session()
        self.session.mount('http://', HTTPAdapter(max_retries = max_retries))
        self.session.mount('https://', HTTPAdapter(max_retries = max_retries))
        self.source = self.session.get(url = self.url,
                                  stream = self.stream,
                                  allow_redirects = True,
                                  timeout = (5,10),
                                  headers = {
                                      "Range": f"bytes={self.start_pos}-{self.end_pos}"
                                  })
        self.headers = dict(self.source.headers)
        self.total_size = int(self.headers['Content-Length'])
        self.thread_sum = thread_sum
        self.filename = filename

    def single_run(self):
        '''
        异步策略进行的下载函数
        '''
        self.source = self.session.get(url = self.url,
                                      stream = self.stream,
                                      allow_redirects = True,
                                      timeout = (5,10))
        self.headers = dict(self.source.headers)
        self.total_size = int(self.headers['Content-Length'])
        with open(self.filename, 'wb+') as file:
            file.seek(self.start_pos)
            rate = 0
            for data in self.source.iter_content(chunk_size = 1024):
                file.write(data)
                rate += len(data)
                if random.randint(0,1000) % 200 == 0:
                    time.sleep(0.01)

    def run(self):
        '''
        Threading使用的start参数重定向。
        '''
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
