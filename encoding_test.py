'''
解参数测试文件
Version: 1.0.0.231203a
Author: CooooldWind_
'''
import encode_sec_key
import pprint

get_list = encode_sec_key.NeteaseParams(
    url = "https://music.163.com/weapi/v6/playlist/detail?",
    encode_data = {'csrf_token': "", 'id': "2547050034", 'n': "0"}
).get_resource()
user_id = get_list['playlist']['userId']
get_list = get_list['playlist']['trackIds']


get_list = encode_sec_key.NeteaseParams(
    url = "https://music.163.com/weapi/v3/song/detail",
    encode_data = {'c': str(get_list), 'csrf_token': '', 'userId':user_id }
).get_resource()['songs']

pprint.pprint(get_list)