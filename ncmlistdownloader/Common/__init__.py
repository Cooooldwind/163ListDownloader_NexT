'''
ncmlistdownloader/Common/__init__.py
存储常用函数。
Core.Ver.1.0.0.240310a1
Author: CooooldWind_
'''

def url_split(str = ""):
    '''
    把id从url里面提取出来
    ----------
    参数:
    1. str(必填): 需要转换的url
    '''
    str = str.split("song?id=")[-1]
    str = str.split("&")[0]
    return str

def artist_turn_str(info = [],split_word = ', '):
    '''
    把歌手列表转换为字符串。
    ----------
    参数:
    1. info(必填): 歌手列表
    2. split_word(默认", "): 分隔符
    '''
    str = ""
    for i in info:
        str += i
        if i != info[-1]:
            str += split_word
    return str

def get_type(str = ''):
    '''
    分析文件的后缀名。
    ----------
    参数：
    1. str: 文件名
    '''
    pos = str.rfind(".")
    return str[pos + 1:]
    