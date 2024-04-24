'''
ncmlistdownloader/cmd/download.py
Core.Ver.1.0.1.240424a1
Author: CooooldWind_
'''

from ncmlistdownloader.cmd.common import *
from ncmlistdownloader.song import *

def download(d = None):
    if d == None or dict(d).get('type') != 'downloading_list_ncmld':
        print(format_output(raw = "Value Error!", type = "Error"))
        return
    d = dict(d)
    print(format_output(raw = '$title$ -> title, $artist$ -> artist, $album$ -> album, $id$ -> id, $$ -> $', type = 'Info'))
    ff = input_func(notice = format_output(raw = 'Input filename format', type = 'Input'))
    div = input_func(notice = format_output(raw = 'Input path', type = 'Input'))
    if div[-1] != '/' and div[-1] != '\\':
        div += '/'
    download_track: list[Song] = []
    for i in d['track']:
        tmp = Song()
        tmp.album = i['album']
        tmp.artist = i['artist']
        tmp.id = i['id']
        tmp.title = i['title']
        tmp.url_info.update({'album_pic': i['pic_url']})
        tmp.filename_format = div + ff
        tmp.filename_format.update({
            'song': tmp.get_formated_filename('mp3'),
            'pic': tmp.get_formated_filename('jpg'),
            'lyric': tmp.get_formated_filename('lrc'),
        })
        download_track.append(tmp)
    for i in download_track:
        i.multi_run()
    