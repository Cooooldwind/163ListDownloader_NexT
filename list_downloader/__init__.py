'''
__init__.py
Version: 1.0.0.240213a
Author: CooooldWind_
'''
import threading
import random
import time
import requests
import os
from PIL import Image
from mutagen.flac import FLAC, Picture
from mutagen.mp3 import EasyMP3
from mutagen.id3 import ID3, APIC, USLT, Encoding
from . import encode_sec_key
from .global_args import PLAYLIST_API, SONG_INFO_API, SONG_FILE_API_2, LEVEL, LYRIC_API

class Playlist:
    '''Playlist类'''
    def __init__(self, id):
        self.id = str(id)
        self.encode_data = {
            'csrf_token': "",
            'id': self.id,
            'n': "0"
        }
        self.creater = None
        self.track_id = None
        self.tracks = None
    def get_resource(self):
        '''获取数据'''
        result = encode_sec_key.NeteaseParams(
            encode_data = self.encode_data,
            url = PLAYLIST_API).get_resource()
        try:
            self.creater = result['playlist']['userId']
        except KeyError:
            return -1
        self.track_id = result['playlist']['trackIds']
        self.tracks = [self.Song({'id': i['id']}, str(self.creater)) for i in self.track_id]
        return 0
    class Song(threading.Thread):
        '''Song子类'''
        def __init__(self, id, user_id):
            threading.Thread.__init__(self)
            self.tc = threading.Semaphore(8)
            self.id = [str(id)]
            self.user_id = str(user_id)
            self.encode_data = {
                'c': self.id,
                'csrf_token': '',
                'userId': self.user_id
            }
            self.info = {}
            self.response = None
            self.downloading_info = {
                'id': None,
                'state': 0,
                'value': 0.00
            }
            self.finish = False
            self.d = "download/"
            self.fnf = None
            self.lv = 1
        def get_resource(self):
            '''获取更加详细的数据'''
            pure_response = encode_sec_key.NeteaseParams(
                encode_data = self.encode_data,
                url = SONG_INFO_API)
            self.response = pure_response.get_resource()['songs'][0]
            self.info.update({'album': self.response['al']['name']})
            self.info.update({'id': str(self.response['id'])})
            self.info.update({'name': self.response['name']})
            self.info.update({'cover_url': self.response['al']['picUrl']})
            tmp = []
            for i in self.response['ar']:
                tmp.append(i['name'])
            self.info.update({'artist': tmp})
            tmp = ""
            for i in self.response['ar']:
                tmp += i['name']
                if i != self.response['ar'][-1]:
                    tmp += ", "
            self.info.update({'artist_str': tmp})
            self.downloading_info['id'] = self.info['id']
        def song_download(self, level, dir, filename):
            '下载音乐'
            self.downloading_info['state'] = 1
            self.downloading_info['value'] = 0
            song_request_url = SONG_FILE_API_2 + "id=" + self.info['id']
            song_request_url = song_request_url + "&level=" + LEVEL[level - 1]
            response = requests.get(url = song_request_url, timeout = 20).json()['data'][0]
            self.info.update({'song_url': response['url']})
            self.info.update({'song_type': response['type']})
            music_filename = dir + filename + '.' + response['type']
            with open(music_filename, 'wb+') as music_file:
                rate = int(0)
                source = requests.get(self.info['song_url'],
                                      stream = True,
                                      allow_redirects = True,
                                      timeout = 20)
                totalsize = int(source.headers['Content-Length'])
                for data in source.iter_content(chunk_size = 1024):
                    music_file.write(data)
                    rate += len(data)
                    self.downloading_info['value'] = round(rate / totalsize, 2)
                    if random.randint(0,1000) % 200 == 0:
                        time.sleep(0.01)
            self.downloading_info['value'] = 1
            return 0
        def lyric_download(self, dir, filename):
            '''下载歌词'''
            self.downloading_info['state'] = 2
            self.downloading_info['value'] = 0
            lyric_filename = dir + filename + '.lrc'
            with open(lyric_filename, 'w+', encoding = 'utf-8') as lyric_file:
                encode_data = {'csrf_token':"",
                            'id':self.info['id'],
                            'lv':'-1',
                            'tv':'-1'}
                response = encode_sec_key.NeteaseParams(
                    encode_data = encode_data,
                    url = LYRIC_API
                ).get_resource()
                lyric_file.write(response['lrc']['lyric'].replace("\n",'\n'))
            self.downloading_info['value'] = 1
        def cover_download(self, dir, filename, size = -1):
            '''封面下载'''
            self.downloading_info['state'] = 3
            self.downloading_info['value'] = 0
            with open(dir + filename + '.jpg', 'wb+') as cover_file:
                rate = int(0)
                source = requests.get(url = self.info['cover_url'],
                                      stream = True,
                                      allow_redirects = True,
                                      timeout = 20)
                totalsize = int(source.headers['Content-Length'])
                for data in source.iter_content(chunk_size = 1024):
                    cover_file.write(data)
                    rate += len(data)
                    self.downloading_info['value'] = round(rate / totalsize / 2, 2)
                    if random.randint(0,1000) % 200 == 0:
                        time.sleep(0.01)
            self.downloading_info['value'] = 0.5
            size = int(size)
            if size == -1:
                self.downloading_info['value'] = 1
                return 0
            cover_file = Image.open(dir + filename + '.jpg')
            self.downloading_info['value'] = 0.6
            cover_file = cover_file.convert("RGB")
            self.downloading_info['value'] = 0.7
            cover_file_type = cover_file.format
            cover_file_out = cover_file.resize((size, size))
            self.downloading_info['value'] = 0.9
            cover_file_out.save(dir + filename + '.jpg', cover_file_type)
            self.downloading_info['value'] = 1
            return 0
        def attribute_write(self, dir, filename, type):
            '''属性填写'''
            self.downloading_info['state'] = 4
            self.downloading_info['value'] = 0
            if type == "flac":
                music_file = FLAC(dir + filename + ".flac")
            elif type == "mp3":
                music_file = EasyMP3(dir + filename + ".mp3")
            else: return -1
            self.downloading_info['value'] = 0.3
            music_file['title'] = self.info['name']
            music_file['album'] = self.info['album']
            self.downloading_info['value'] = 0.5
            tmp = ""
            for i in self.info['artist']:
                tmp = tmp + i
                if i != self.info['artist'][-1]:
                    tmp = tmp + "; "
            self.downloading_info['value'] = 0.7
            music_file['artist'] = tmp
            music_file.save()
            self.downloading_info['value'] = 1
            return 0
        def cover_write(self, dir, filename, type, cover_dir, cover_filename):
            '''写入专辑封面'''
            self.downloading_info['state'] = 5
            self.downloading_info['value'] = 0
            if type == "flac":
                music_file = FLAC(dir + filename + ".flac")
            elif type == "mp3":
                music_file = ID3(dir + filename + ".mp3")
            else: return -1
            self.downloading_info['value'] = 0.3
            with open(cover_dir + cover_filename + '.jpg', 'rb+') as cover_file:
                if type == "flac":
                    music_file.clear_pictures()
                    cover = Picture()
                    cover.data = cover_file.read()
                    cover.mime = 'image/jpeg'
                    music_file.add_picture(cover)
                    self.downloading_info['value'] = 0.7
                elif type == "mp3":
                    music_file['APIC'] = APIC(encoding = 3,
                                              mime = 'image/jpeg',
                                              type = 3,
                                              desc = 'Cover',
                                              data = cover_file.read())
                    self.downloading_info['value'] = 0.7
            music_file.save()
            self.downloading_info['value'] = 1
            return 0
        def lyric_write(self, dir, filename, type, lyric_dir, lyric_filename):
            '''写入歌词'''
            self.downloading_info['state'] = 6
            self.downloading_info['value'] = 0
            with open(lyric_dir + lyric_filename + '.lrc', 'r+', encoding = 'utf-8') as lyric_file:
                lyric = lyric_file.read()
                if type == "flac":
                    self.downloading_info['value'] = 0.3
                    music_file = FLAC(dir + filename + ".flac")
                    music_file['lyrics'] = lyric
                    self.downloading_info['value'] = 0.7
                elif type == "mp3":
                    self.downloading_info['value'] = 0.3
                    music_file = ID3(dir + filename + ".mp3")
                    music_file.setall("USLT", [USLT(
                        encoding = Encoding.UTF8,
                        format = 2,
                        type = 1,
                        text = lyric
                    )])
                    self.downloading_info['value'] = 0.7
                else:
                    return -1
                music_file.save()
            self.downloading_info['value'] = 1
            self.finish = True
            return 0
        def initialize(self, tc, fnf, lv, d = "download/"):
            if d != self.d and d != "":
                self.d = d
            else:
                try:
                    os.makedirs("download/")
                except FileExistsError:
                    pass
            self.tc = tc
            self.fnf = fnf
            self.lv = lv
        def run(self):
            with self.tc:
                fn = str(self.fnf)
                fn = fn.replace("$id$", self.info['id'])
                fn = fn.replace("$artist$", self.info['artist_str'])
                fn = fn.replace("$name$", self.info['name'])
                fn = fn.replace("$album$", self.info['album'])
                fn = fn.replace("$$", "$")
                self.song_download(self.lv, self.d, fn) #歌曲下载。第一个参数是音质，1~8如下。
                tp = self.info['song_type']
                self.lyric_download(self.d, fn) #歌词下载
                self.cover_download(self.d, fn) #封面下载
                self.attribute_write(self.d, fn, tp) #属性填写
                self.cover_write(self.d, fn, tp, self.d, fn) #封面注入到属性
                self.lyric_write(self.d, fn, tp, self.d, fn) #歌词注入到属性
