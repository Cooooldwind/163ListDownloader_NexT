"""
ncmlistdownloader/cmd/common.py
Core.Ver.1.0.5.240429
Author: CooooldWind_
"""

import time

GLOBAL_CONFIG_MODEL = {
    "song_download": True,
    "cover_download": True,
    "lyric_download": True,
    "attribute_write": True,
    "cover_write": True,
    "lyric_write": True,
}


def format_output(raw: str, type="Info") -> str:
    time_now_formated = time.strftime("%H:%M:%S", time.localtime())
    return_str = f"[{type}][{time_now_formated}] {raw}"
    if type == "Input":
        return_str += ">> "
    return return_str


def input_func(notice: str):
    return input(format_output(raw=notice, type="Input"))
