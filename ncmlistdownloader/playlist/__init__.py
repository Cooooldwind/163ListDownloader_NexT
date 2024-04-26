'''
ncmlistdownloader/playlist/__init__.py
Core.Ver.1.0.3.240426
Author: CooooldWind_
'''
from ncmlistdownloader.common import *
from ncmlistdownloader.common.encode_sec_key import *
from ncmlistdownloader.common.global_args import *
from ncmlistdownloader.song import *
import threading

class Playlist():
    def __init__(self, id: str):
        self.id = id
        if self.id.find("163.com") != -1:
            self.id = url_split(url = self.id)
        self.track: list[Song] = []
        self.creator_id = ""
        self.raw_info = {}
        self.track_count = int(0)
        self.creator = ""
        self.track_id = []
        self.title = ""
        self.mp_succeed = False

    def get_info(self, cookies = None):
        self.raw_info = NeteaseParams(url = PLAYLIST_API,
                                      encode_data = {
                                          'csrf_token': '',
                                          'id': self.id,
                                      }).get_resource(cookies = cookies)
        if self.raw_info['code'] != 200:
            return -1
        self.creator_id = self.raw_info['playlist']['userId']
        self.track_count = self.raw_info['playlist']['trackCount']
        self.creator = self.raw_info['playlist']['creator']['nickname']
        self.title = self.raw_info['playlist']['name']
        for i in self.raw_info['playlist']['trackIds']:
            self.track_id.append(str(i['id']))
        for truck_id in self.track_id:
            self.track.append(Song(id = truck_id))
        return self.raw_info
    
    def get_detail_info(self):
        threads: list[threading.Thread] = []
        for i in self.track:
            thread = threading.Thread(target = i.multi_get_info)
            thread.start()
            threads.append(thread)
        for i in threads:
            i.join()
        self.mp_succeed = True

    def auto_get_info(self, cookies = dict()):
        if self.get_info(cookies = cookies) != -1:
            self.get_detail_info()
        else: return -1

    def done_sum(self):
        count = 0
        for i in self.track:
            if i.is_get == True:
                count += 1
        return count
    
    def multiprocessing_get_detail(self):
        p = threading.Thread(target = self.get_detail_info)
        p.start()
