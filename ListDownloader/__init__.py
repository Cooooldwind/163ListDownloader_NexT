'''
__init__.py
Version: 1.0.0.231222a
Author: CooooldWind_
'''
from . import encode_sec_key
from .global_args import PLAYLIST_API, SONG_INFO_API, SONG_FILE_API_2, LEVEL, LYRIC_API
from PIL import Image
from mutagen.flac import FLAC
from mutagen.id3 import ID3,APIC
import threading
import requests
import random
import time

class Playlist:
    '''Playlist类'''
    def __init__(self, id):
        self.id = str(id)
        self.encode_data = {
            'csrf_token': "",
            'id': self.id,
            'n': "0"
        }
    def get_resource(self):
        '''获取数据'''
        result = encode_sec_key.NeteaseParams(
            encode_data = self.encode_data,
            url = PLAYLIST_API).get_resource()
        self.creater = result['playlist']['userId']
        self.track_id = result['playlist']['trackIds']
        self.tracks = [self.Song({'id': i['id']}, str(self.creater)) for i in self.track_id]
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
        def get_resource(self):
            '''获取更加详细的数据'''
            with threading.Semaphore(32):
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
        def song_download(self, level, dir, filename):
            '下载音乐'
            song_request_url = SONG_FILE_API_2 + "id=" + self.info['id'] + "&level=" + LEVEL[level + 1]
            response = requests.get(url = song_request_url).json()['data'][0]
            self.info.update({'song_url': response['url']})
            music_file = open(dir + filename + '.' + response['type'], 'wb+')
            rate = int(0)
            source = requests.get(self.info['song_url'], stream = True, allow_redirects = True)
            for data in source.iter_content(chunk_size = 1024):
                music_file.write(data)
                rate += len(data)
                '别一直干活，人总是要休息的，服务器也一样，别累坏人家了'
                if random.randint(0,1000) % 200 == 0:
                    time.sleep(0.01)     
            music_file.close()
        def lyric_download(self, dir, filename):
            '''下载歌词'''
            lyric_file = open(dir + filename + '.lrc','w+',encoding = 'utf-8')
            encode_data = {'csrf_token':"",
                        'id':self.info['id'],
                        'lv':'-1',
                        'tv':'-1'}
            response = encode_sec_key.NeteaseParams(
                encode_data = encode_data,
                url = LYRIC_API
            ).get_resource()
            lyric_file.write(response['lrc']['lyric'].replace("\n",'\n'))
            lyric_file.close()
        def cover_download(self, dir, filename, size = -1):
            '''封面下载'''
            cover_file = open(dir + filename + '.jpg', 'wb+')
            source = requests.get(url = self.info['cover_url'], stream = True, allow_redirects = True)
            rate = int(0)
            for data in source.iter_content(chunk_size = 1024):
                cover_file.write(data)
                rate += len(data)
                '别一直干活，人总是要休息的，服务器也一样，别累坏人家了'
                if random.randint(0,1000) % 200 == 0:
                    time.sleep(0.01)     
            cover_file.close()
            size = int(size)
            if size == -1: return
            cover_file = Image.open(dir + filename + '.jpg')
            cover_file = cover_file.convert("RGB")
            cover_file_type = cover_file.format
            cover_file_out = cover_file.resize((size, size))
            cover_file_out.save(dir + filename + '.jpg', cover_file_type)
        def attribute_write(self, dir, filename, type, ):
            if type == "flac":
                music_file = FLAC(dir + filename + ".flac")
                music_file['title'] = self.info['name']
                music_file['album'] = self.info['album']
                tmp = ""
                for i in self.info['artist']:
                    tmp = tmp + i
                    if i != self.info['artist'][-1]: tmp = tmp + "; "
                music_file['artist'] = tmp
                music_file.save()
                print(music_file.values())
            
