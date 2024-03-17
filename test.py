'''
test.py
Core.Ver.1.0.0.240317a1
Author: CooooldWind_
'''
from ncmlistdownloader.Song import *
import pprint

s = Song("2040876720")
pprint.pprint(s.get_info())
s.attribute_write("test.mp3")