'''
ncmlistdownloader/__init__.py
Core.Ver.1.0.4.240427
Author: CooooldWind_
'''
from pathlib import Path
import time
from ncmlistdownloader.playlist import *
from ncmlistdownloader.common import *
from ncmlistdownloader.common.global_args import *

def main():
    for i in CMD_START_WORDS:
        print(i)
    print(f'[*]{CORE_VERSION}')
    id = str(input("ID: "))
    p = Playlist(id)
    p.get_info()
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
    p.multiprocessing_get_detail()
    while p.mp_succeed == False:
        time.sleep(1)
    for i in p.track:
        music_filename = i.song_download()
        if music_filename == -1:
            print(i.title + ' cannot download.')
            continue
        cover_filename = i.cover_download()
        lyric_filename = i.lyric_get()
        i.attribute_write(music_filename)
        i.cover_write(music_filename, cover_filename)
        i.lyric_write(music_filename, lyric_filename)
        print(i.title + ' succeed.')
    print('Succeed. Files at:', d)
