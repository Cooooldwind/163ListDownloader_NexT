'''
ncmlistdownloader/Song/__init__.py
Core.Ver.1.0.0.240310a1
Author: CooooldWind_
'''
from Common.global_args import SONG_INFO_API
from Common.encode_sec_key import NeteaseParams
import Common

class Song():
    '''
    Song类
    ----------
    存储歌曲信息，以及各种函数。
    常用的有如下：
    1. name/album/artist
    2. downloading_state, downloading_value
    '''
    def __init__(self, id = ""):
        self.id = id
        if self.id.find("163.com") != -1:
            self.id = Common.url_split(str = self.id)
        self.title = ""
        self.artist = []
        self.album = ""
        self.downloading_state = 0
        self.downloading_value = 0.00
        self.encode_data = {
                'c': str([{'id':str(self.id)}]),
                'csrf_token': '',
            }
        self.pure_info = dict()
    def __str__(self):
        info = {
            'album': self.album,
            'title': self.title,
            'artist': self.artist,
            'id': self.id
        }
        return str(info)
    def dict(self):
        info = {
            'album': self.album,
            'title': self.title,
            'artist': self.artist,
            'id': self.id
        }
        return info
    def get_info(self):
        '''
        获取歌曲信息
        ----------
        无参数。
        '''
        self.pure_info = NeteaseParams(
            encode_data = self.encode_data,
            url = SONG_INFO_API
        ).get_resource()['songs'][0]
        self.title = self.pure_info['name']
        self.album = self.pure_info['al']['name']
        for i in self.pure_info['ar']:
            self.artist.append(i['name'])
        return self.pure_info
    