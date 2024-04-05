'''
ncmlistdownloader/__init__.py
Core.Ver.1.0.0.240404b4-2
Author: CooooldWind_
'''
from ncmlistdownloader.playlist import *

def main():
    print("163ListDownloader CMD Ver.")
    print("Core.Ver.1.0.0.240404b4 / Made by CooooldWind_")
    print("Warning: It's an Beta Version. It may has a lot of bugs.")
    print("If you met them, click the links below:")
    print("Gitee: https://gitee.com/CooooldWind/163ListDownloader_NexT/issues")
    print("GitHub: https://github.com/CooooldWind/163ListDownloader_NexT/issues")
    id = str(input("ID: "))
    p = Playlist(id)
    p.get_info()
    p.get_detail_info()
    print("Playlist info-reading succeed.")
    d = str(input("Dir: "))
    if d == '':
        d = '%USERPROFILE%/Downloads/ncmlistdownloader/'
    fnf = str(input("Filename format: "))
    if fnf == '':
        fnf = '$title$ - $artist$'
    if d[-1] != '/' and d[-1] != '\\':
        d += '/'
    d = d.replace('\\', '/')
    for i in p.track:
        i.filename_format = d + fnf
        j = i.song_download()
        if j == -1:
            print(i.title + 'cannot download.')
            continue
        i.cover_download()
        i.lyric_get()
        i.attribute_write()
        i.cover_write()
        i.lyric_write()
    print('Succeed.')
