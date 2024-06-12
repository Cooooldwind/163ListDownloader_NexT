"""
ncmlistdownloader/music/__init__.py
Core.Ver.2.0.0.240612a1
Copyright @CooooldWind_
Following GNU_AGPLV3+ License
"""

import requests
import ncmlistdownloader.encode as encode
import ncmlistdownloader.tool as tool
import ncmlistdownloader.global_args as global_args


class Music:
    """
    Music类
    ----------
    """

    def __init__(self, id: str, auto_info_get: bool = True):
        # 处理id
        self.id: str
        if id.find("163.com") != -1:
            self.id = tool.url_split(url=id)
        else:
            self.id = id
        # 解密数据
        self._encode_data = {
            "c": str([{"id": str(self.id)}]),
            "csrf_token": "",
        }
        self._lyric_encode_data = {
            "id": str(str(self.id)),
            "lv": -1,
            "tv": -1,
            "csrf_token": "",
        }
        self._enhanced_encode_data = {
            "ids": str([self.id]),
            "level": "",
            "encodeType": "mp3",
            "csrf_token": "",
        }
        # 返回值
        self.raw_info = None
        self.enhanced_raw_info = None
        # 基本信息
        self.title: str = None
        self.album: str = None
        self.artist: list[str] = None
        # 歌词
        self.lyric: str = None
        # URL
        self.music_url: str = None
        self.cover_url: str = None
        # 自动获取信息
        if auto_info_get:
            self.get_info()

    def get_info(self, MUSIC_U: str = "", level: int = 1):
        # 基本信息
        self.raw_info = encode.NeteaseParams(
            url=global_args.SONG_INFO_API, encode_data=self._encode_data
        ).get_resource()["songs"][0]
        self.title = self.raw_info["name"]
        self.artist: list[str] = [i["name"] for i in self.raw_info["ar"]]
        self.album = self.raw_info["al"]["name"]
        # 图片URL
        self.cover_url = self.raw_info["al"]["picUrl"]
        # 歌曲URL
        url = ""
        if MUSIC_U != "":
            # 使用cookies的
            cookies = {"MUSIC_U": MUSIC_U}
            self._enhanced_encode_data["level"] = global_args.LEVEL[level]
            if level == 4:
                self._enhanced_encode_data["encodeType"] = "aac"
            self.enhanced_raw_info = encode.NeteaseParams(
                url=global_args.SONG_FILE_API_ENHANCED,
                encode_data=self._enhanced_encode_data,
            ).get_resource(cookies=cookies)["data"][0]
            url = self.enhanced_raw_info["url"]
            url = url[: url.rfind("?")]
        else:
            url = global_args.SONG_FILE_API + self.id
            url = requests.head(url=url, allow_redirects=True).url
        self.music_url = url
        # 歌词
        lyric_raw_info = encode.NeteaseParams(
            url=global_args.LYRIC_API, encode_data=self._lyric_encode_data
        ).get_resource()
        self.lyric = str(lyric_raw_info["lrc"]["lyric"])
        result = {
            "title": self.title,
            "album": self.album,
            "artist": self.artist,
            "music_url": self.music_url,
            "cover_url": self.cover_url,
            "lyric": self.lyric,
        }
        return result
