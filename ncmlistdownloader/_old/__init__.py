"""
ncmlistdownloader/__init__.py
Core.Ver.1.1.1.240510
Author: CooooldWind_
"""

from pathlib import Path
import time
import getpass
from ncmlistdownloader.playlist import *
from ncmlistdownloader.common import *
from ncmlistdownloader.common.global_args import *


def main():
    for i in CMD_START_WORDS:
        print(i)
    print(f"[*]{CORE_VERSION}")
    c = {"MUSIC_U": str(getpass.getpass("Cookies(Press Enter if you have not): ", ))}
    id = str(input("ID: "))
    p = Playlist(id)
    if c['MUSIC_U'] == "":
        p.get_info()
    else:
        p.get_info(cookies=c)
    print("Playlist info-reading succeed.")
    d = str(input("Dir: "))
    if d == "":
        d = str(Path.home()) + "/Downloads/ncmld_downloads/"
    fnf = str(input("Filename format: "))
    if fnf == "":
        fnf = "$title$ - $artist$"
    if d[-1] != "/" and d[-1] != "\\":
        d += "/"
    d = d.replace("\\", "/")
    auto_mkdir(d)
    for i in p.track:
        i.filename_format = d + fnf
    p.multiprocessing_get_detail()
    while p.mp_succeed == False:
        time.sleep(1)
    l_finally = ""
    if c['MUSIC_U'] != "":
        l_str = ['standard', 'higher', 'exhigh', 'lossless']
        l = int(input("You have Cookies. Input the level(1~4): "))
        l_finally = l_str[l - 1]
    for i in p.track:
        i.song_download_enhanced(level = l_finally, cookies = c)
        music_filename = i.song_download()
        if music_filename == -1:
            print(i.title + " cannot download.")
            continue
        cover_filename = i.cover_download()
        lyric_filename = i.lyric_get()
        i.attribute_write(music_filename)
        i.cover_write(music_filename, cover_filename)
        i.lyric_write(music_filename, lyric_filename)
        print(i.title + " succeed.")
    print("Succeed. Files at:", d)
