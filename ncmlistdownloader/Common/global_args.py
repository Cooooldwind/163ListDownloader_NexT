'''
list_downloader/global_args.py
Core.Ver.1.0.0.240326a1
Author: CooooldWind_, 是青旨啊
Update_Content:
1. 把信息转移到了一个.json文件里面
'''
import json
import os
import ncmlistdownloader.common
module_path = os.path.abspath(ncmlistdownloader.common.__file__)
with open(module_path[:module_path.rfind("\\")] + "global_args.json", encoding = "utf-8") as f:
    json_file = json.load(f)
USER_AGENTS = json_file['USER_AGENTS']
FUNC_F = json_file['FUNC_F']
SEC_KEY = json_file['SEC_KEY']
PLAYLIST_API = json_file['PLAYLIST_API']
SONG_INFO_API = json_file['SONG_INFO_API']
SONG_FILE_API = json_file['SONG_FILE_API']
SONG_FILE_API_2 = json_file['SONG_FILE_API_2']
LYRIC_API = json_file['LYRIC_API']
