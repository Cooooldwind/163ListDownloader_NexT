"""
ncmlistdownloader/common.py
Core.Ver.2.0.0.240731b1
Copyright @CooooldWind_
Following GNU_AGPLV3+ License
"""

import os


def url_split(url=str()) -> str:
    """
    把id从url里面提取出来
    ----------
    参数:
    1. `url`(必填): 需要转换的url
    """
    id_return = url.split("?id=")[-1].split("&")[0]
    return id_return


def artist_turn_str(info=[], split_word=", ") -> str:
    """
    把歌手列表转换为字符串。
    ----------
    参数:
    1. `info`(必填): 歌手列表
    2. `split_word`(默认 `, ` ): 分隔符
    """
    if not info:
        raise ValueError('"info" must be a list. See comment for detail infomation.')
    str_return = ""
    for i in info:
        str_return += i
        if i != info[-1]:
            str_return += split_word
    return str_return


def get_type(filename=str()) -> str:
    """
    获取文件的后缀名。
    ----------
    参数：
    1. `filename`: 文件名
    """
    return filename[filename.rfind(".") + 1 :]


def get_name(filename=str()) -> str:
    """
    获取文件的名称。
    ----------
    参数：
    1. `filename`: 文件名
    """
    return filename[: filename.rfind(".")]


def clean(filename=str()) -> str:
    """
    清空有悖于标准的字符的函数。
    ----------
    参数：
    1. `filename`: 文件名
    """
    filename_return = filename
    dirty = [":", "*", '"', "?", "|", "<", ">", "/", "\\"]
    for i in dirty:
        filename_return = filename_return.replace(i, "_")
    return filename_return


def auto_mkdir(path=str()):
    """
    创建路径
    ----------
    参数：
    1. `path`: 路径
    """
    now_path = os.getcwd().replace("\\", "/")
    path_re = path.replace("\\", "/")
    if path.find(":/") >= 0:
        path_list = path_re.split("/")
        finally_path_list = path_list
    else:
        now_path_list = now_path.split("/")
        path_list = path_re.split("/")
        while path_list[0] == "../":
            path_list = path_list[1:]
            now_path_list = now_path_list[:-1]
        finally_path_list = now_path_list + path_list
    finally_path = ""
    for i in finally_path_list:
        finally_path += i + "/"
        if not os.path.exists(finally_path):
            os.mkdir(path=finally_path)


def format(filename="", title="", artist="", album="", id="") -> str:
    filename_formated = filename
    filename_formated = filename_formated.replace("$title$", title)
    filename_formated = filename_formated.replace("$artist$", artist)
    filename_formated = filename_formated.replace("$album$", album)
    filename_formated = filename_formated.replace("$id$", id)
    filename_formated = filename_formated.replace("$$", "$")
    return filename_formated
