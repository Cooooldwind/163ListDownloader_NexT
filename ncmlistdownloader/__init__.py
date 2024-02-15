'''
list_downloader/__init__.py
Core.Ver.1.0.0.240213a
Author: CooooldWind_
'''
import threading
import random
import time
import requests
import os
import eyed3
from PIL import Image
from mutagen.flac import FLAC, Picture
from mutagen.mp3 import EasyMP3
from mutagen.id3 import ID3, APIC, USLT, Encoding
from . import encode_sec_key
from .global_args import PLAYLIST_API, SONG_INFO_API, SONG_FILE_API_2, LEVEL, LYRIC_API

def clean(s):
    '''清空有悖于标准的字符的函数。'''
    dirty = ["/","\\",":","*","\"","?","|","<",">"]
    for i in dirty:
        s = s.replace(i,"")
    return s

class Playlist:
    '''
    Playlist类。

    用tracks表示每一首歌。

    tracks里面都是Song类。
    '''
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
        '''初步获取数据：歌单内的歌曲都是些什么。'''
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
        '''
        Song子类，存储每个歌曲。

        包括元信息，各种函数。

        常用的有info['id'/'name'/'artist'/'album']和downloading_info['id'/'state'/'value']
        '''
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
            '''
            获取更加详细的数据。

            （其实就是元信息）
            '''
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
        def song_download(self, dir = str(), filename = str(), level = 1):
            '''
            下载音乐。

            参数：

            dir：存储路径（结尾必须是“/”或“\”）；

            filename：文件名（不含后缀）；

            level：音质（默认为1，从低到高，不超过8）。
            '''
            if level > 8 or level < 1:
                return -1
            filename = clean(filename)
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
        def lyric_download(self, dir = str(), filename = str()):
            '''
            下载歌词。

            参数：

            dir：存储路径（结尾必须是“/”或“\”）；

            filename：文件名（不含后缀）。
            '''
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
        def cover_download(self, dir = str(), filename = str(), size = -1):
            '''
            封面下载。

            参数：

            dir：存储路径（结尾必须是“/”或“\”）；

            filename：文件名（不含后缀）；

            size：图片分辨率，单位为像素（默认-1，-1表示不修改尺寸）。
            '''
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
        def attribute_write(self, dir = str(), filename = str(), type = str()):
            '''
            属性填写。

            参数：

            dir：存储路径（结尾必须是“/”或“\”）；

            filename：文件名（不含后缀）；

            type：文件类型（flac/mp3）。
            '''
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
        def cover_write(self, dir = str(), filename = str(), type = str(), cover_dir = str(), cover_filename = str()):
            '''
            写入专辑封面。

            参数：

            dir：存储路径（结尾必须是“/”或“\”）；

            filename：文件名（不含后缀）；

            type：文件类型（flac/mp3）；

            cover_dir：封面的存储路径（结尾必须是“/”或“\”）；

            cover_filename：封面的文件名（不含后缀）；
            '''
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
                    music_file.add(APIC(encoding = 3,
                                        mime = 'image/jpeg',
                                        type = 3,
                                        desc = u'Cover',
                                        data = cover_file.read()))
                    self.downloading_info['value'] = 0.7
            music_file.save()
            self.downloading_info['value'] = 1
            return 0
        def lyric_write(self, dir = str(), filename = str(), type = str(), lyric_dir = str(), lyric_filename = str()):
            '''
            写入歌词。

            参数：

            dir：存储路径（结尾必须是“/”或“\”）；

            filename：文件名（不含后缀）；

            type：文件类型（flac/mp3）；

            lyric_dir：歌词的存储路径（结尾必须是“/”或“\”）；

            lyric_filename：歌词的文件名（不含后缀）；
            '''
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
        def initialize(self, tc_sum = int(), fnf = "$name$ - $artist$", lv = 1, d = "download/"):
            '''
            初始化参数。

            参数：

            tc_sum：多线程的线程数：默认8；

            fnf：文件名的格式，以下是文件名格式的规范:

            用"$xxx$"表示一些内容：

            "$id$"是歌曲id；"$name$"是歌曲名称；

            "$artist$"是歌手；"$album$"是专辑；

            输入"$"用"$$"；

            lv: 品质（由低到高1~8）默认1；

            d：存储路径（结尾必须是“/”或“\”）默认创建子文件夹“download/”。
            '''
            if d != self.d and d != "":
                self.d = d
            else:
                try:
                    os.makedirs("download/")
                except FileExistsError:
                    pass
            self.tc = threading.Semaphore(tc_sum)
            self.fnf = fnf
            self.lv = lv
        def run(self):
            '''给多线程使用的启动函数'''
            with self.tc:
                fn = str(self.fnf)
                fn = fn.replace("$id$", self.info['id'])
                fn = fn.replace("$artist$", self.info['artist_str'])
                fn = fn.replace("$name$", self.info['name'])
                fn = fn.replace("$album$", self.info['album'])
                fn = fn.replace("$$", "$")
                self.song_download(level = self.lv, dir = self.d, filename = fn)
                tp = self.info['song_type']
                self.lyric_download(dir = self.d, filename = fn)
                self.cover_download(dir = self.d, filename = fn) #封面下载
                self.attribute_write(dir = self.d, filename = fn, type = tp) #属性填写
                self.cover_write(self.d, fn, tp, self.d, fn) #封面注入到属性
                self.lyric_write(self.d, fn, tp, self.d, fn) #歌词注入到属性
