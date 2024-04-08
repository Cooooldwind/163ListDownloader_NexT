'''
ncmlistdownloader/__init__.py
Core.Ver.1.0.0.240408a1
Author: CooooldWind_
'''
from pathlib import Path
from ncmlistdownloader.playlist import *
from ncmlistdownloader.common import *
from ncmlistdownloader.common.global_args import *

def main():
    for i in CMD_START_WORDS:
        print(i)
    print('Core.Ver.1.0.0.240408a1')
    id = str(input("ID: "))
    p = Playlist(id)
    p.get_info()
    p.get_detail_info()
    print("Playlist info-reading succeed.")
    d = str(input("Dir: "))
    if d == '':
        d = str(Path.home()) + '/Downloads/ncmld_downloads/'
    fnf = str(input("Filename format: "))
    if fnf == '':
        fnf = '$title$ - $artist$'
    if d[-1] != '/' and d[-1] != '\\':
        d += '/'
    d = d.replace('\\', '/')
    auto_mkdir(d)
    for i in p.track:
        i.filename_format = d + fnf
    p.get_detail_info()
    for i in p.track:
        music_filename = i.song_download()
        if music_filename == -1:
            print(i.title + ' cannot download.')
            continue
        i.cover_download()
        i.lyric_get()
        i.attribute_write()
        i.cover_write()
        i.lyric_write()
        print(i.title + ' succeed.')
    print('Succeed. Files at:', d)
