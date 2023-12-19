'''
__init__.py
Version: 1.0.0.231218a
Author: CooooldWind_
'''
import encode_sec_key
from global_args import PLAYLIST_URL, SONG_INFO_URL
import pprint

class Playlist(object):
    '''Playlist类'''
    def __init__(self, id):
        self.id = str(id)
        self.encode_data = {
            'csrf_token': "",
            'id': self.id,
            'n': "0"
        }
    def get(self):
        result = encode_sec_key.NeteaseParams(
            encode_data = self.encode_data,
            url = PLAYLIST_URL).get_resource()
        self.creater = result['playlist']['userId']
        self.track_id = result['playlist']['trackIds']
        self.tracks = [self.Song({'id': i['id']}, str(self.creater)) for i in self.track_id]
    class Song(object):
        def __init__(self, id, user_id):
            self.id = [str(id)]
            self.user_id = str(user_id)
            self.encode_data = {
                'c': self.id,
                'csrf_token': '',
                'userId': self.user_id
            }
            self.info = dict()
        def get(self):
            result = encode_sec_key.NeteaseParams(
                encode_data = self.encode_data,
                url = SONG_INFO_URL).get_resource()['songs'][0]
            self.info.update({'album': result['al']['name']})
            self.info.update({'id': result['al']['id']})
            self.info.update({'artists': i['name'] for i in result['ar']})
            self.info.update({'name': result['name']})

test_p = Playlist("2391850012")
test_p.get()
for i in range(100):
    test_p.tracks[i].get()
    print(test_p.tracks[i].info['name'])