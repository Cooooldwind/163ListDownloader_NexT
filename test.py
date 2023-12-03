'''
version: 1.0.0.231202a
docstring: 测试文件
author: CooooldWind_
'''
import encode_sec_key
import pprint

pprint.pprint(
    encode_sec_key.NeteaseParams(
        url = "https://music.163.com/weapi/song/lyric?csrf_token=",
        encode_data = {
            'csrf_token': "",
            'id': "1398764652",
            'lv': '-1',
            'tv': '-1'
            }
        ).get_resource()
    )