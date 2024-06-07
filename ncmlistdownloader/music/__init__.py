"""
ncmlistdownloader/music/__init__.py
Core.Ver.2.0.0.240607a1
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

    def __init__(self, id: str, MUSIC_U: str = "", auto_info_get: bool = True):
        # 处理cookies
        self.cookies = {"MUSIC_U": MUSIC_U}
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
        # 自动获取信息
        if auto_info_get:
            self.get_info()

    def get_info(self):
        self.raw_info = encode.NeteaseParams(
            url=global_args.SONG_INFO_API, encode_data=self._encode_data
        ).get_resource()["songs"][0]
        self.title = self.raw_info["name"]
        self.artist: list[str] = [i["name"] for i in self.raw_info["ar"]]
        self.album = self.raw_info["al"]["name"]
        return self.raw_info

    def music_download(self, MUSIC_U: str = "", level: int = 1):
        if MUSIC_U != "":
            cookies = {"MUSIC_U": MUSIC_U}
        else:
            cookies = self.cookies
        # 获取链接
        self._enhanced_encode_data["level"] = global_args.LEVEL[level]
        if level == 4:
            self._enhanced_encode_data["encodeType"] = "aac"
        self.enhanced_raw_info = encode.NeteaseParams(
            url = global_args.SONG_FILE_API_ENHANCED, encode_data=self._enhanced_encode_data
        ).get_resource(cookies=cookies)["data"][0]
        url = self.enhanced_raw_info["url"]
        url = url[:url.rfind("?")]
        return url