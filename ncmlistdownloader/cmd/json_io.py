'''
ncmlistdownloader/cmd/json_io.py
Core.Ver.1.0.1.240422a1
Author: CooooldWind_
'''

from ncmlistdownloader.song import *
from ncmlistdownloader.playlist import *
from ncmlistdownloader.cmd.common import *

def json_save_list(pl: Playlist):
    path = str(input_func(notice = "Input the file's page"))
    d = {
        'type': 'downloading_list',
        'global_config': GLOBAL_CONFIG_MODEL,
        'track': [],
    }
    t = []
    for i in pl.track:
        t.append({
            'type': 'song',
            'info': {
                'title': i.title,
                'artist': i.artist,
                'album': i.album,
                'id': i.id,
            },
            'global': True,
            'downloading_config': GLOBAL_CONFIG_MODEL,
        })
    d['track'] = t
    with open(path, 'w+', encoding = 'utf-8') as file:
        json.dump(d, file, ensure_ascii = False, sort_keys = True)
    print(format_output("Saved!", type = "Info"))