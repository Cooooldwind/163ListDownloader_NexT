'''
ncmlistdownloader/__init__.py
Core.Ver.1.0.0.240310a1
Author: CooooldWind_
'''
from Song import Song
from Common import artist_turn_str
import pprint

test = Song("https://music.163.com/song?id=1493077219&userid=1577080369")
pprint.pprint(test.get_info())
print(artist_turn_str(info = test.artist, split_word = '/'))