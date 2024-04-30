"""
ncmlistdownloader/Downloader/__init__.py
Core.Ver.1.1.0.240430a1
Author: CooooldWind_
"""

import json
from ncmlistdownloader.song import *

"""
d = {
    "type": "downloading_list_ncmld",
    "global_config": GLOBAL_CONFIG_MODEL,
    "track": [{
        "type": "song",
        "info": {
            "title": i.title,
            "artist": i.artist,
            "album": i.album,
            "id": i.id,
            "pic_url": i.url_info["album_pic"]
        },
        "global": True,
        "downloading_config": GLOBAL_CONFIG_MODEL,
    },...]
}
"""


class DownloadList:

    def __init__(self) -> None:
        self.track: list[Song] = []

    def import_json(self, json_file: str) -> int:
        with open(json_file, "r+", encoding="utf-8") as json_file:
            raw_dict = json.load(json_file)
            if raw_dict["type"] != "downloading_list_ncmld":
                return -1
            for i in raw_dict['track']:
                self.track.append(Song(id=i['info']['id']))
            for i in self.track:
                i.multi_get_info()
