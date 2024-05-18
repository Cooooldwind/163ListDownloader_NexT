"""
ncmlistdownloader/global_args.py
Core.Ver.2.0.0.240516a1
Copyright @CooooldWind_
Following GNU_AGPLV3+ License
"""

_CORE_VERSION_TUPLE = (
    "2",
    "0",
    "0",
    "240518",
    "3",
    "1",
)

# Don't touch codes below if unnecessary!
FUNC_F = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
LYRIC_API = "https://music.163.com/weapi/song/lyric?csrf_token="
PLAYLIST_API = "https://music.163.com/weapi/v6/playlist/detail?"
SEC_KEY = "6ea19f618d09893013feb207e6953ab0d04831ccf86095147970745a825a0f3288ad0bfdb802ffd5876394599d179b65785e679b23ae38035d476872f5270c26f7e15f0e2de0da92ac7fdd1de6a965642a67707d3b204d48a3a3c66fe536c9e2056d2032c884d764cf419e8ce7bd245f56bde140deccbaed83995285ee66ccda"
SONG_FILE_API = "https://music.163.com/song/media/outer/url?id="
SONG_FILE_API_ENHANCED = "https://music.163.com/weapi/song/enhance/player/url/v1?"
SONG_INFO_API = "https://music.163.com/weapi/v3/song/detail"
SEARCH_API = "https://music.163.com/weapi/cloudsearch/get/web?csrf_token="
USER_AGENTS = [
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
]
"""
Major,
Minor,
Fix,
Date,
Level(3 = ALpha, 4 = Beta, 5 = Stable),
Index Number,
"""
_LEVEL = ("a", "b")
CORE_VERSION = ""
if _CORE_VERSION_TUPLE[4] == 5:
    CORE_VERSION = ".".join(_CORE_VERSION_TUPLE[0:4])
else:
    _LEVEL_NOW = _LEVEL[int(_CORE_VERSION_TUPLE[4]) - 3]
    CORE_VERSION = (
        ".".join(_CORE_VERSION_TUPLE[0:4]) + _LEVEL_NOW + _CORE_VERSION_TUPLE[5]
    )
