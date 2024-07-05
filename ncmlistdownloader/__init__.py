"""
ncmlistdownloader/__init__.py
Ver.1.2.0.240705
Author: CooooldWind_
"""

from pathlib import Path
import time
from ncmlistdownloader.playlist import *
from ncmlistdownloader.common import *
from ncmlistdownloader.common.global_args import *
from ncmlistdownloader.editer import cover_compress

def t_or_f(s = str()) -> bool:
    return (s.capitalize == "True" or s.capitalize == "T" or s == "")


def main():
    for i in CMD_START_WORDS:
        print(i)
    print(f"[*]{CORE_VERSION}")
    c_str = str(input("Cookies(Press Enter if you have not): "))
    c = {"MUSIC_U": c_str}
    if c_str != "":
        print("Got cookies! ")
    else:
        print("No cookies! ")
    id = str(input("ID/URL: "))
    p = Playlist(id)
    if c["MUSIC_U"] == "":
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
    print("Make some settings!")
    # cover_download, lyric_get, attribute_write, lyric_write, cover_compress, gb18030/utf-8
    bb,cc,dd,ee,ff,gg = True,True,True,True,-1,True
    bb = t_or_f(str(input("1: cover_download & write(T/F): ")))
    cc = t_or_f(str(input("2: lyric_get(T/F): ")))
    dd = t_or_f(str(input("3: attribute_write(T/F): ")))
    ee = t_or_f(str(input("4: lyric_write(T/F): ")))
    ff = int(input("5: cover_compress(int): "))
    if ff <= 0: ff = -1
    gg = t_or_f(str(input("6: gb18030/utf-8(T/F): ")))
    print(bb,cc,dd,ee,ff,gg)
    if c["MUSIC_U"] != "":
        l_str = ["standard", "higher", "exhigh", "lossless"]
        l = int(input("You have Cookies. Input the level(1~4): "))
        l_finally = l_str[l - 1]
    n = 0
    for i in p.track:
        if c_str != "":
            ude = i.song_download_enhanced(level=l_finally, cookies=c)
            if ude == "None":
                ude = i.song_download_enhanced(level="standard", cookies=c)
                if ude == "None":
                    print(i.title + " cannot download.")
                    continue
        music_filename = i.song_download()
        if music_filename == -1:
            print(i.title + " cannot download.")
            continue
        if bb: cover_filename = i.cover_download()
        if cc: 
            if not gg: lyric_filename = i.lyric_get("utf-8")
            else: lyric_filename = i.lyric_get()
        if dd: i.attribute_write(music_filename)
        if ff != -1: cover_compress(ff, cover_filename)
        if bb: i.cover_write(music_filename, cover_filename)
        if ee: i.lyric_write(music_filename, lyric_filename)
        n += 1
        print(f"{n}/{p.track_count}: {i.title} Succeed.")
    print("Succeed. Files at:", d)

if __name__ == "__main__": main()