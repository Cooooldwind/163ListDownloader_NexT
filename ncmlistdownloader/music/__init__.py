"""
ncmlistdownloader/music/__init__.py
Core.Ver.2.0.0.240518a1
Copyright @CooooldWind_
Following GNU_AGPLV3+ License
"""

import ncmlistdownloader.encode as encode
import ncmlistdownloader.tool as tool
import ncmlistdownloader.global_args as global_args


class Music:
    """
    Music类
    ----------
    """

    def __init__(self, id: str, cookies: str = "", auto_info_get: bool = True):
        self.cookies = {"MUSIC_U": cookies}
        self.id: str
        if id.find("163.com") != -1:
            self.id = tool.url_split(url=id)
        else:
            self.id = id
        self.encode_data = {
            "c": str([{"id": str(self.id)}]),
            "csrf_token": "",
        }
        self.lyric_encode_data = {
            "csrf_token": "",
            "id": str(str(self.id)),
            "lv": -1,
            "tv": -1,
        }
        self.raw_info = None
        self.title: str = None
        self.album: str = None
        self.artist: list[str] = None
        if auto_info_get: self.get_info()

    def get_info(self, cookies = None):
        cookies_ready = cookies
        if self.cookies["MUSIC_U"] != "":
            cookies_ready = self.cookies
        self.raw_info = encode.NeteaseParams(
            url=global_args.SONG_INFO_API, encode_data=self.encode_data
        ).get_resource(cookies=cookies_ready)["songs"][0]
        self.title = self.raw_info["name"]
        self.artist: list[str] = [i["name"] for i in self.raw_info["ar"]]
        self.album = self.raw_info["al"]["name"]