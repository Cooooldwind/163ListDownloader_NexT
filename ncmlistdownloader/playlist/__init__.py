'''
ncmlistdownloader/playlist/__init__.py
Core.Ver.1.0.0.240411a1
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

    def get_info(self):
        self.raw_info = NeteaseParams(url = PLAYLIST_API,
                                      encode_data = {
                                          'csrf_token': '',
                                          'id': self.id,
                                      }).get_resource()['playlist']
        self.creator_id = self.raw_info['userId']
        self.track_count = self.raw_info['trackCount']
        self.creator = self.raw_info['creator']['nickname']
        self.title = self.raw_info['name']
        for i in self.raw_info['trackIds']:
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

    def auto_get_info(self):
        self.get_info()
        self.get_detail_info()