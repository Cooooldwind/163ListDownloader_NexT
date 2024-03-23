'''
ncmlistdownloader/Common/__init__.py
存储常用函数。
Core.Ver.1.0.0.240323a1
Author: CooooldWind_
Updated_Content:
1. auto_mkdir(path)
'''

import os

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

def clean(str = ''):
    '''
    清空有悖于标准的字符的函数。
    ----------
    参数：
    1. str: 文件名
    '''
    dirty = [":","*","\"","?","|","<",">"]
    for i in dirty:
        str = str.replace(i,"")
    return str
    
def auto_mkdir(path = ''):
    '''
    创建路径
    ----------
    参数：
    1. path: 路径
    '''
    now_path = os.getcwd().replace("\\","/")
    path = path.replace("\\","/")
    if path.find(":/") >= 0:
        path_list = path.split("/")
        finally_path_list = path_list
    else:
        now_path_list = now_path.split("/")
        path_list = path.split("/")
        while path_list[0] == "../":
            path_list = path_list[1:]
            now_path_list = now_path_list[:-1]
        finally_path_list = now_path_list + path_list
    finally_path = ""
    for i in finally_path_list:
        finally_path += i + "/"
        if not os.path.exists(finally_path):
            os.mkdir(path = finally_path)

