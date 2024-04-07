'''
ncmlistdownloader/__init__.py
Core.Ver.1.0.0.240407b1
Author: CooooldWind_
'''
from ncmlistdownloader.playlist import *
from ncmlistdownloader.common import *

def main():
    print("163ListDownloader CMD Ver.")
    print("Core.Ver.1.0.0.240407b1 / Made by CooooldWind_")
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
    auto_mkdir(d)
    for i in p.track:
        i.filename_format = d + fnf
        music_filename = i.song_download()
        if music_filename == -1:
            print(i.title + 'cannot download.')
            continue
        cover_filename = i.cover_download()
        lyric_filename = i.lyric_get()
        i.attribute_write(music_filename)
        i.cover_write(music_filename, cover_filename)
        i.lyric_write(music_filename, lyric_filename)
        print(i.title + 'Succeed.')
    print('Succeed.')
