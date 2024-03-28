'''
ncmlistdownloader/Playlist/__init__.py
Core.Ver.1.0.0.240328a1
Author: CooooldWind_
'''
from ncmlistdownloader.common import *
from ncmlistdownloader.common.encode_sec_key import *
from ncmlistdownloader.song import *

class Playlist():
    def __init__(self, id = ""):
        self.id = id
        self.tracks: list[Song] = []
        self.creater = ""
    def get_info(self):
        pass