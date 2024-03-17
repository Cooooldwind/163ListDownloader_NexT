'''
ncmlistdownloader/Common/__init__.py
存储常用函数。
Core.Ver.1.0.0.240317a2
Author: CooooldWind_
Updated_Content:
1. get_name(str = '')
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
    获取文件的后缀名。
    ----------
    参数：
    1. str: 文件名
    '''
    return str[str.find(".") + 1:]

def get_name(str = ''):
    '''
    获取文件的名称。
    ----------
    参数：
    1. str: 文件名
    '''
    return str[:str.rfind(".")]
    