"""
ncmlistdownloader/cmd/download.py
Core.Ver.1.0.5.240429
Author: CooooldWind_
"""

import time
from ncmlistdownloader.cmd.common import *
from ncmlistdownloader.song import *


def download(d=None):
    if d == None or dict(d).get("type") != "downloading_list_ncmld":
        print(format_output(raw="Value Error!", type="Error"))
        return
    d = dict(d)
    print(
        format_output(
            raw="$title$ -> title, $artist$ -> artist, $album$ -> album, $id$ -> id, $$ -> $",
            type="Info",
        )
    )
    ff = input_func(notice="Input filename format")
    div = input_func(notice="Input path")
    if div[-1] != "/" and div[-1] != "\\":
        div += "/"
    download_track: list[Song] = []
    for j in d["track"]:
        i = j["info"]
        tmp = Song(id=i["id"])
        # tmp.album = i['album']
        # tmp.artist = i['artist']
        # tmp.id = i['id']
        # tmp.title = i['title']
        # tmp.url_info.update({'album_pic': i['pic_url']})
        tmp.filename_format = div + ff
        """tmp.filename_info.update({
            'song': tmp.get_formated_filename('mp3'),
            'pic': tmp.get_formated_filename('jpg'),
            'lyric': tmp.get_formated_filename('lrc'),
        })"""
        download_track.append(tmp)
    for i in range(0, len(d["track"])):
        dd = d["global_config"]
        download_track[i].multi_run(d=dd)
        print(format_output(raw=f"{download_track[i].title} Start.", type="Info"))
        while download_track[i].is_dl == False:
            time.sleep(1)
        print(format_output(raw=f"{download_track[i].title} Succeed.", type="Info"))
