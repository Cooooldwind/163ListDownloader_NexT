'''
ncmlistdownloader/Playlist/__init__.py
Core.Ver.1.0.0.240330a2
Author: CooooldWind_
Update_Context:
1. Playlist.get_info()
'''
from ncmlistdownloader.common import *
from ncmlistdownloader.common.encode_sec_key import *
from ncmlistdownloader.common.global_args import *
from ncmlistdownloader.song import *

class Playlist():
    def __init__(self, id = ""):
        self.id = id
        self.track: list[Song] = []
        self.creator_id = ""
        self.raw_info = {}
        self.track_count = int(0)
        self.creator = ""
        self.track_id = []
    def get_info(self):
        self.raw_info = NeteaseParams(url = PLAYLIST_API,
                                      encode_data = {
                                          'csrf_token': '',
                                          'id': self.id,
                                      }).get_resource()['playlist']
        self.creator_id = self.raw_info['userId']
        self.track_count = self.raw_info['trackCount']
        self.creator = self.raw_info['creator']['nickname']
        for i in self.raw_info['playlist']['trackIds']:
            self.track_id.append(str(i['id']))
        return self.raw_info