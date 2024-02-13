'''
__init__.py
Version: 1.0.0.240213a
Author: CooooldWind_
'''
import threading
import random
import time
import requests
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
            self.id = [str(id)]
            self.user_id = str(user_id)
            self.encode_data = {
                'c': self.id,
                'csrf_token': '',
                'userId': self.user_id
            }
            self.info = {}
            self.response = None
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
        def song_download(self, level, dir, filename):
            '下载音乐'
            song_request_url = SONG_FILE_API_2 + "id=" + self.info['id']
            song_request_url = song_request_url + "&level=" + LEVEL[level + 1]
            response = requests.get(url = song_request_url, timeout = 5).json()['data'][0]
            self.info.update({'song_url': response['url']})
            self.info.update({'song_type': response['type']})
            music_filename = dir + filename + '.' + response['type']
            with open(music_filename, 'wb+') as music_file:
                rate = int(0)
                source = requests.get(self.info['song_url'],
                                      stream = True,
                                      allow_redirects = True,
                                      timeout = 5)
                for data in source.iter_content(chunk_size = 1024):
                    music_file.write(data)
                    rate += len(data)
                    if random.randint(0,1000) % 200 == 0:
                        time.sleep(0.01)
            return 0
        def lyric_download(self, dir, filename):
            '''下载歌词'''
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
        def cover_download(self, dir, filename, size = -1):
            '''封面下载'''
            with open(dir + filename + '.jpg', 'wb+') as cover_file:
                source = requests.get(url = self.info['cover_url'],
                                      stream = True,
                                      allow_redirects = True,
                                      timeout = 5)
                rate = int(0)
                for data in source.iter_content(chunk_size = 1024):
                    cover_file.write(data)
                    rate += len(data)
                    if random.randint(0,1000) % 200 == 0:
                        time.sleep(0.01)
            size = int(size)
            if size == -1:
                return -1
            cover_file = Image.open(dir + filename + '.jpg')
            cover_file = cover_file.convert("RGB")
            cover_file_type = cover_file.format
            cover_file_out = cover_file.resize((size, size))
            cover_file_out.save(dir + filename + '.jpg', cover_file_type)
            return 0
        def attribute_write(self, dir, filename, type):
            '''属性填写'''
            if type == "flac":
                music_file = FLAC(dir + filename + ".flac")
            elif type == "mp3":
                music_file = EasyMP3(dir + filename + ".mp3")
            else: return -1
            music_file['title'] = self.info['name']
            music_file['album'] = self.info['album']
            tmp = ""
            for i in self.info['artist']:
                tmp = tmp + i
                if i != self.info['artist'][-1]:
                    tmp = tmp + "; "
            music_file['artist'] = tmp
            music_file.save()
            return 0
        def cover_write(self, dir, filename, type, cover_dir, cover_filename):
            '''写入专辑封面'''
            if type == "flac":
                music_file = FLAC(dir + filename + ".flac")
            elif type == "mp3":
                music_file = ID3(dir + filename + ".mp3")
            else: return -1
            with open(cover_dir + cover_filename + '.jpg', 'rb+') as cover_file:
                if type == "flac":
                    music_file.clear_pictures()
                    cover = Picture()
                    cover.data = cover_file.read()
                    cover.mime = 'image/jpeg'
                    music_file.add_picture(cover)
                elif type == "mp3":
                    music_file['APIC'] = APIC(encoding = 3,
                                              mime = 'image/jpeg',
                                              type = 3,
                                              desc = 'Cover',
                                              data = cover_file.read())
            music_file.save()
            return 0
        def lyric_write(self, dir, filename, type, lyric_dir, lyric_filename):
            '''写入歌词'''
            with open(lyric_dir + lyric_filename + '.lrc', 'r+', encoding = 'utf-8') as lyric_file:
                lyric = lyric_file.read()
                if type == "flac":
                    music_file = FLAC(dir + filename + ".flac")
                    music_file['lyrics'] = lyric_file.read()
                elif type == "mp3":
                    music_file = ID3(dir + filename + ".mp3")
                    music_file.setall("USLT", [USLT(
                        encoding = Encoding.UTF8,
                        format = 2,
                        type = 1,
                        text = lyric
                    )])
                else:
                    return -1
                music_file.save()
            return 0
