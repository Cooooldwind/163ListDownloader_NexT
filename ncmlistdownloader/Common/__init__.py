'''
ncmlistdownloader/Common/__init__.py
存储常用函数。
Core.Ver.1.0.0.240327a1
Author: CooooldWind_
Update_Content:
1. 改了参数名字
'''

import os

def url_split(url = str()):
    '''
    把id从url里面提取出来
    ----------
    参数:
    1. `url`(必填): 需要转换的url
    '''
    id = url.split("song?id=")[-1].split("&")[0]
    return id

def artist_turn_str(info = [],split_word = ', '):
    '''
    把歌手列表转换为字符串。
    ----------
    参数:
    1. `info`(必填): 歌手列表
    2. `split_word`(默认 `, ` ): 分隔符
    '''
    str = ""
    for i in info:
        str += i
        if i != info[-1]:
            str += split_word
    return str

def get_type(filename = str()):
    '''
    获取文件的后缀名。
    ----------
    参数：
    1. `filename`: 文件名
    '''
    return filename[filename.find(".") + 1:]

def get_name(filename = str()):
    '''
    获取文件的名称。
    ----------
    参数：
    1. `filename`: 文件名
    '''
    return filename[:filename.rfind(".")]

def clean(filename = str()):
    '''
    清空有悖于标准的字符的函数。
    ----------
    参数：
    1. `filename`: 文件名
    '''
    dirty = [":","*","\"","?","|","<",">","/","\\"]
    for i in dirty:
        filename = filename.replace(i,"")
    return filename

def auto_mkdir(path = str()):
    '''
    创建路径
    ----------
    参数：
    1. `path`: 路径
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
