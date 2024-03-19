'''
ncmlistdownloader/Song/__init__.py
Core.Ver.1.0.0.240319a4
Author: CooooldWind_
Updated_Content: line#68
'''

from ncmlistdownloader.Common import *
from ncmlistdownloader.Downloader.common import *
from ncmlistdownloader.Common.global_args import *
from ncmlistdownloader.Editer import *

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
            self.id = url_split(str = self.id)
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
        '''
        返回存有歌曲信息的字符串。
        ----------
        无参数。
        '''
        info = {
            'album': self.album,
            'title': self.title,
            'artist': self.artist,
            'id': self.id
        }
        return str(info)
    def dict(self):
        '''
        返回存有歌曲信息的字典。
        ----------
        无参数。
        '''
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
        self.pure_info = response_get(url = SONG_INFO_API, data = self.encode_data)['songs'][0]
        self.title = self.pure_info['name']
        self.album = self.pure_info['al']['name']
        for i in self.pure_info['ar']:
            self.artist.append(i['name'])
        return self.pure_info
    def attribute_write(self, filename = str()):
        '''
        往文件里面写入歌曲信息
        ----------
        参数：
        1. filename: 文件名，字符串，仅mp3/flac格式
        '''
        attribute_write(filename = filename, info = self.dict())
    def cover_write(self, filename = str()):
        '''
        专辑封面（下载与（未实现））写入
        ----------
        参数：
        1. filename: 文件名，字符串，仅mp3/flac格式
        '''
        cover_write(filename = filename, cover_filename = None)

    