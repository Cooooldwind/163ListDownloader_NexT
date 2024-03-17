'''
ncmlistdownloader/Editer/__init__.py
Core.Ver.1.0.0.240317a2
Author: CooooldWind_
Updated_Content:
1. Bug fixed
'''
from PIL import Image
from mutagen.flac import FLAC, Picture
from mutagen.mp3 import EasyMP3
from mutagen.id3 import ID3, APIC, USLT, Encoding
from ncmlistdownloader.Common import get_type, artist_turn_str

expection_word_front = "Opening files with the suffix \"."
lyric_expection_word_front = "Opening cover files with the suffix \"."
cover_expection_word_front = "Opening cover files with the suffix \"."
expection_word_end = "\" is not supported."

def attribute_write(filename = str(), info = dict()):
    '''
    属性写入
    ----------
    参数：
    1. filename: 文件名，字符串，仅mp3/flac格式
    2. info: 信息，里面需要"album"，"artist"，"title"
    '''
    type = get_type(filename)
    if type == "mp3":
        file = EasyMP3(filename)
    elif type == "flac":
        file = FLAC(filename)
    else: 
        raise Exception(expection_word_front + type + expection_word_end)
    file['title'] = info['title']
    file['album'] = info['album']
    file['artist'] = artist_turn_str(
        info = info['artist'],
        split_word = '; ')
    file.save()
    return 0

def cover_write(filename = str(), cover_filename = str()):
    '''
    专辑封面写入
    ----------
    参数：
    1. filename: 文件名，字符串，仅mp3/flac格式
    2. cover_filename: 封面的文件名，字符串，仅jpg格式
    '''
    type = get_type(filename)
    if type == "mp3":
        file = ID3(filename)
    elif type == "flac":
        file = FLAC(filename)
    else: 
        raise Exception(expection_word_front + type + expection_word_end)
    cover_type = get_type(cover_filename)
    if cover_type != "jpg" and cover_type != "jpeg":
        raise Exception(cover_expection_word_front + cover_type + expection_word_end)
    with open(cover_filename, 'rb+') as cover_file:
        if type == "mp3":
            file.add(APIC(
                encoding = 3,
                mime = "image/jpeg",
                type = 3,
                desc = u"Cover",
                data = cover_file.read()
            ))
        elif type == "flac":
            file.clear_pictures()
            cover = Picture()
            cover.data = cover_file.read()
            cover.mime = "image/jpeg"
            file.add_picture(cover)
    file.save()
    return 0

def lyric_write(filename = str(), lyric_filename = str()):
    '''
    专辑封面写入
    ----------
    参数：
    1. filename: 文件名，字符串，仅mp3/flac格式
    2. lyric_filename: 封面的文件名，字符串，仅lrc格式
    '''
    type = get_type(filename)
    if type == "mp3":
        file = ID3(filename)
    elif type == "flac":
        file = FLAC(filename)
    else: 
        raise Exception(expection_word_front + type + expection_word_end)
    lyric_type = get_type(lyric_filename)
    if lyric_type != "lrc":
        raise Exception(lyric_expection_word_front + lyric_type + expection_word_end)
    with open(lyric_filename, 'rb+') as lyric_file:
        lyric = lyric_file.read()
        if type == "mp3":
            file.setall("USLT",[USLT(
                encoding = Encoding.UTF8,
                format = 2,
                type = 1,
                text = lyric
            )])
        elif type == "flac":
            file['lyrics'] = lyric
    file.save()
    return 0
