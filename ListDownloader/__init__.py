'''
__init__.py
Version: 1.0.0.231222a
Author: CooooldWind_
'''
from . import encode_sec_key
from .global_args import PLAYLIST_URL, SONG_INFO_URL
import threading

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
            url = PLAYLIST_URL).get_resource()
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
                result = encode_sec_key.NeteaseParams(
                    encode_data = self.encode_data,
                    url = SONG_INFO_URL).get_resource()['songs'][0]
                self.info.update({'album': result['al']['name']})
                self.info.update({'id': result['al']['id']})
                self.info.update({'artists': i['name'] for i in result['ar']})
                self.info.update({'name': result['name']})
