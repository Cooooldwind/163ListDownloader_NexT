"""
ncmlistdownloader/Editer/__init__.py
Core.Ver.1.0.8.240501
Author: CooooldWind_
"""

from PIL import Image
from mutagen.flac import FLAC, Picture
from mutagen.id3 import ID3, APIC, USLT, Encoding
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from ncmlistdownloader.common import get_type, artist_turn_str

expection_word_front = 'Opening files with the suffix ".'
lyric_expection_word_front = 'Opening cover files with the suffix ".'
cover_expection_word_front = 'Opening cover files with the suffix ".'
expection_word_end = '" is not supported.'


def attribute_write(filename=str(), info=None):
    """
    属性写入
    ----------
    参数：
    1. `filename`: 文件名, 字符串, 仅mp3/flac格式
    2. `info`: 信息, 里面需要 `'album'` , `'artist'`, `'title'`
    """
    type = get_type(filename)
    if type == "mp3":
        file = EasyID3(filename)
    elif type == "flac":
        try: file = FLAC(filename)
        except: return -1
    else:
        raise Exception(expection_word_front + type + expection_word_end)
    if not info:
        raise ValueError(
            '"info" must be a dict(). See the comment for detail infomatiom.'
        )
    file["title"] = info["title"]
    file["album"] = info["album"]
    file["artist"] = artist_turn_str(info=info["artist"], split_word="; ")
    file.save()
    return 0


def cover_write(filename=str(), cover_filename=str()):
    """
    专辑封面写入
    ----------
    参数：
    1. `filename`: 文件名, 字符串, 仅mp3/flac格式
    2. `cover_filename`: 封面的文件名, 字符串, 仅jpg格式
    """
    type = get_type(filename)
    if type == "mp3":
        file = ID3(filename)
    elif type == "flac":
        try: file = FLAC(filename)
        except: return -1
    else:
        raise Exception(expection_word_front + type + expection_word_end)
    cover_type = get_type(cover_filename)
    if cover_type != "jpg" and cover_type != "jpeg":
        raise Exception(cover_expection_word_front + cover_type + expection_word_end)
    with open(cover_filename, "rb") as cover_file:
        if type == "mp3":
            file["APIC"] = APIC(
                encoding=3,
                mime="image/jpeg",
                type=3,
                desc="Cover",
                data=cover_file.read(),
            )
            file.save(v2_version=3, v1=2)
        elif type == "flac":
            file.clear_pictures()
            cover = Picture()
            cover.data = cover_file.read()
            cover.mime = "image/jpeg"
            file.add_picture(cover)
            file.save()
    return 0


def lyric_write(filename=str(), lyric_filename=str()):
    """
    专辑歌词写入
    ----------
    参数：
    1. `filename`: 文件名, 字符串, 仅mp3/flac格式
    2. `lyric_filename`: 歌词的文件名, 字符串, 仅lrc格式
    """
    type = get_type(filename)
    if type == "mp3":
        file = ID3(filename)
    elif type == "flac":
        try: file = FLAC(filename)
        except: return -1
    else:
        raise Exception(expection_word_front + type + expection_word_end)
    lyric_type = get_type(lyric_filename)
    if lyric_type != "lrc":
        raise Exception(lyric_expection_word_front + lyric_type + expection_word_end)
    with open(lyric_filename, "rb+") as lyric_file:
        lyric = lyric_file.read()
        if type == "mp3":
            file.setall(
                "USLT", [USLT(encoding=Encoding.UTF8, format=2, type=1, text=lyric)]
            )
        elif type == "flac":
            file["lyrics"] = lyric
    file.save()
    return 0


def cover_compress(edge_len=800, filename=str()):
    cover_file = Image.open(filename)
    cover_file = cover_file.convert("RGB")
    cover_file_type = cover_file.format
    cover_file_out = cover_file.resize((edge_len, edge_len), Image.NEAREST)
    cover_file_out.save(filename, cover_file_type)
