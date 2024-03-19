'''
test.py
Core.Ver.1.0.0.240319a4
Author: CooooldWind_
'''

# 1.0.0.240317a1
'''
from ncmlistdownloader.Song import *
import pprint

s = Song("2040876720")
pprint.pprint(s.get_info())
s.attribute_write("test.mp3")
'''

'''
# 1.0.0.240318a1
from ncmlistdownloader.Downloader.common import *
filename = "C:/Users/Administrator/Desktop/git.exe"
url = "https://mirrors.huaweicloud.com/git-for-windows/v2.43.0.windows.1/Git-2.43.0-64-bit.exe"
download(url = url, filename = filename)
'''

'''
# 1.0.0.240319a3
# 这个运行不了，貌似是要cookies。
from ncmlistdownloader.Downloader.common import *
from ncmlistdownloader.Common.encode_sec_key import *
import pprint
url = "https://music.163.com/weapi/cloudsearch/get/web?csrf_token="
key = "Better to lie"
data = {
    "s": key,
    "csrf_token": "",
    # "limit": "30",
    # "total": "true",
    # "offset": "0",
    # "#/discover": "",
    "type": "1",
}
pprint.pprint(response_get(url = url, data = data))
'''