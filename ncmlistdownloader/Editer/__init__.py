from PIL import Image
from mutagen.flac import FLAC, Picture
from mutagen.mp3 import EasyMP3
from mutagen.id3 import ID3, APIC, USLT, Encoding
from Common import get_type, artist_turn_str

def attribute_write(filename = str(), info = dict()):
    '''
    属性写入
    ----------
    参数：
    1. filename: 文件名，字符串
    2. info: 信息，里面需要"album"，"artist"，"title"
    '''
    expection_word_front = "Opening files with the suffix \"."
    expection_word_end = "\" is not supported."
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

    