'''
ncmlistdownloader/Song/__init__.py
Core.Ver.1.0.0.240325a1
Author: CooooldWind_
Updated_Content: 
1. fix: didn't import ncmlistdownloader.Common.encode_sec_key
2. markdown!
'''

from ncmlistdownloader.common import *
from ncmlistdownloader.common.encode_sec_key import *
from ncmlistdownloader.downloader import *
from ncmlistdownloader.common.global_args import *
from ncmlistdownloader.common.encode_sec_key import *
from ncmlistdownloader.editer import *

class Song():
    '''
    Song类
    ----------
    存储歌曲信息，以及各种函数。
    常用的有如下：
    1. `name` / `album` / `artist`
    2. `downloading_state` / `downloading_value`
    3. `raw_info` / `processed_info` / `url_info`
    '''

    def __init__(self, id = ""):
        self.id = id
        if self.id.find("163.com") != -1:
            self.id = url_split(str = self.id)
        self.title = ""
        self.artist = []
        self.artist_str = ""
        self.album = ""
        self.downloading_state = 0
        self.downloading_value = 0.00
        self.encode_data = {
                'c': str([{'id':str(self.id)}]),
                'csrf_token': '',
            }
        self.raw_info = dict()
        self.processed_info = dict()
        self.url_info = dict()

    def __str__(self):
        '''
        返回存有歌曲信息的字符串。
        ----------
        无参数。
        如果直接print这个类就是调用这个函数了。
        '''
        return str(self.processed_info)
    
    def get_info(self):
        '''
        获取歌曲信息
        ----------
        无参数。
        '''
        self.raw_info = NeteaseParams(
            url = SONG_INFO_API,
            encode_data = self.encode_data).get_resource()['songs'][0]
        self.title = self.raw_info['name']
        self.album = self.raw_info['al']['name']
        for i in self.raw_info['ar']:
            self.artist.append(i['name'])
        self.artist_str = artist_turn_str(self.artist)
        self.processed_info = {
            'album': self.album,
            'title': self.title,
            'artist': self.artist,
            'id': self.id
        }
        self.url_info.update({
            'album_pic': self.raw_info['al']['picUrl'],
            'song_file': SONG_FILE_API + self.id,
        })
        return self.raw_info
    
    def attribute_write(self, filename = str()):
        '''
        往文件里面写入歌曲信息
        ----------
        参数：
        1. filename: 文件名，字符串，仅mp3/flac格式
        '''
        attribute_write(filename = filename, info = self.processed_info)

    def cover_write(self, filename = str()):
        '''
        专辑封面（下载与（未实现））写入
        ----------
        参数：
        1. filename: 文件名，字符串，仅mp3/flac格式
        '''
        cover_write(filename = filename, cover_filename = None)

    