"""
list_downloader/global_args.py
Core.Ver.1.3.1.240707
Author: CooooldWind_, 是青旨啊
"""
from ncmlistdownloader.common.version import *
FUNC_F_PART = [
    "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7",
    "b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280",
    "104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932",
    "575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b",
    "3ece0462db0a22b8e7",
]
SEC_KEY_PART = [
    "6ea19f618d09893013feb207e6953ab0d04831ccf86095147970745a825a",
    "0f3288ad0bfdb802ffd5876394599d179b65785e679b23ae38035d476872",
    "f5270c26f7e15f0e2de0da92ac7fdd1de6a965642a67707d3b204d48a3a3",
    "c66fe536c9e2056d2032c884d764cf419e8ce7bd245f56bde140deccbaed",
    "83995285ee66ccda",
]
json_file = {
    "FUNC_F": "".join(FUNC_F_PART),
    "LYRIC_API": "https://music.163.com/weapi/song/lyric?csrf_token=",
    "PLAYLIST_API": "https://music.163.com/weapi/v6/playlist/detail?",
    "SEC_KEY": "".join(SEC_KEY_PART),
    "SONG_FILE_API": "https://music.163.com/song/media/outer/url?id=",
    "SONG_FILE_API_2": "https://music.163.com/weapi/song/enhance/player/url/v1?",
    "SONG_INFO_API": "https://music.163.com/weapi/v3/song/detail",
}
FUNC_F = json_file["FUNC_F"]
SEC_KEY = json_file["SEC_KEY"]
PLAYLIST_API = json_file["PLAYLIST_API"]
SONG_INFO_API = json_file["SONG_INFO_API"]
SONG_FILE_API = json_file["SONG_FILE_API"]
SONG_FILE_API_2 = json_file["SONG_FILE_API_2"]
SEARCH_API = "https://music.163.com/weapi/cloudsearch/get/web?csrf_token="
LYRIC_API = json_file["LYRIC_API"]
CMD_START_WORDS = [
    f"163ListDownloader CMD Ver - {CMD_VERSION}",
    "Made by CooooldWind_",
    "Here's the Gitee/GitHub Page, click a star if you like it~",
    "Gitee: https://gitee.com/CooooldWind/163ListDownloader_NexT/issues",
    "GitHub: https://github.com/CooooldWind/163ListDownloader_NexT/issues",
]
