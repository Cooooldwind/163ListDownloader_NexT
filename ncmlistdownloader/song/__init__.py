'''
ncmlistdownloader/Song/__init__.py
Core.Ver.1.0.0.240404a3
Author: CooooldWind_
'''

from ncmlistdownloader.common import *
from ncmlistdownloader.common.encode_sec_key import *
from ncmlistdownloader.common.thread_test import best_thread
from ncmlistdownloader.downloader import *
from ncmlistdownloader.common.global_args import *
from ncmlistdownloader.common.encode_sec_key import *
from ncmlistdownloader.editer import *

class Song():
    '''
    Song类
    ----------
    存储歌曲信息，以及各种函数。
    常用的有如下: 
    1. `name` / `album` / `artist`
    2. `downloading_state` / `downloading_value`
    3. `raw_info` / `processed_info` / `url_info`
    参数: 
    1. `id`: 歌曲id (其实传入url也行)
    '''

    def __init__(self, id = ""):
        self.id = id
        if self.id.find("163.com") != -1:
            self.id = url_split(url = self.id)
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
        self.lyric_encode_data = {
            'csrf_token': '',
            'id': str([{'id':str(self.id)}]),
            'lv': -1,
            'tv': -1,
        }
        self.raw_info = {}
        self.processed_info = {}
        self.url_info = {}
        self.filename_format = '$title$ - $artist$'

    def __str__(self):
        '''
        返回存有歌曲信息的字符串。
        ----------
        无参数。
        如果直接`print`这个类就是调用这个函数了。
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
    
    def multi_get_info(self):
        '''
        获取歌曲信息（多线程用）
        ----------
        无参数。
        '''
        with threading.Semaphore(8):
            self.get_info()

    def song_download(self):
        format_info = self.processed_info
        format_info.update({
            'filename': self.filename_format,
            'artist': self.artist_str,
            'album': self.album,
            'id': self.id,
            'title': self.title,
            })
        filename = format(**format_info)
        if filename.rfind('/') != -1:
            filename = filename[:filename.rfind('/')] + clean(filename[filename.rfind('/') + 1:])
        else:
            filename = clean(filename)
        file_origin = OriginFile(self.url_info['song_file'])
        if file_origin.total_size == -1:
            return -1
        file_origin.auto_start(filename = filename)

    def cover_download(self):
        format_info = self.processed_info
        format_info.update({
            'filename': self.filename_format,
            'artist': self.artist_str,
            'album': self.album,
            'id': self.id,
            'title': self.title,
            })
        filename = format(**format_info)
        if filename.rfind('/') != -1:
            filename = filename[:filename.rfind('/')] + clean(filename[filename.rfind('/') + 1:])
        else:
            filename = clean(filename)
        file_origin = OriginFile(self.url_info['album_pic'])
        if file_origin.total_size == -1:
            return -1
        file_origin.auto_start(filename = filename)

    def lyric_get(self):
        self.lyric = NeteaseParams(
            url = LYRIC_API,
            encode_data = self.lyric_encode_data
        ).get_resource()['lrc']['lyric'].replace("\n", '\n')
        format_info = self.processed_info
        format_info.update({
            'filename': self.filename_format,
            'artist': self.artist_str,
            'album': self.album,
            'id': self.id,
            'title': self.title,
            })
        filename = format(**format_info)
        if filename.rfind('/') != -1:
            filename = filename[:filename.rfind('/')] + clean(filename[filename.rfind('/') + 1:])
        else:
            filename = clean(filename)
        with open(file = filename, mode = 'w+', encoding = 'UTF-8') as file:
            file.write(self.lyric)


    def attribute_write(self, filename = str()):
        '''
        往文件里面写入歌曲信息
        ----------
        参数: 
        1. `filename`: 文件名，字符串，仅mp3/flac格式
        '''
        attribute_write(filename = filename, info = self.processed_info)

    def cover_write(self, filename = str(), cover_filename = str()):
        '''
        专辑封面写入
        ----------
        参数: 
        1. `filename`: 文件名，字符串，仅mp3/flac格式
        2. `cover_filename`: 封面的文件名, 字符串, 仅jpg格式
        '''
        cover_write(filename = filename, cover_filename = cover_filename)

    def lyric_write(self, filename = str(), lyric_filename = str()):
        lyric_write(filename = filename, lyric_filename = lyric_filename)
    

    