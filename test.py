'''
test.py
Author: CooooldWind_
'''

'''
# 1.0.0.240317a1
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

'''
# 1.0.0.240320a2
from ncmlistdownloader.Downloader import *
import pprint
filename = "C:/Users/Administrator/Desktop/git.exe"
url = "https://mirrors.huaweicloud.com/git-for-windows/v2.43.0.windows.1/Git-2.43.0-64-bit.exe"
file_origin = OriginFile(url = url)
pprint.pprint(file_origin.headers)
'''

'''
返回的结果。
{
    'Server': 'CloudWAF',
    'Date': 'Wed, 20 Mar 2024 10:30:11 GMT',
    # 文件类型：应用，UTF-8编码。
    'Content-Type': 'application/octet-stream;charset=UTF-8',
    # 文件大小：60868040（位？）
    'Content-Length': '60868040',
    'Connection': 'keep-alive',
    'Set-Cookie': 'HWWAFSESID=49893bb79fce609919; path=/, HWWAFSESTIME=1710930604973; path=/',
    'lubanops-gtrace-id': 'v-648620-1710930611731-326844629',
    'lubanops-nenv-id': '269996',
    'Vary': 'Origin, Access-Control-Request-Method, Access-Control-Request-Headers',
    'X-Checksum-Md5': 'dfd5b1ee7c69a55a61da44e00473f56a',
    'X-Checksum-Sha1': 'c479dc90ebd3c71a8d24b19a9cdc0222dc4705a0',
    'X-Checksum-Sha256': 'a6058d7c4c16bfa5bcd6fde051a92de8c68535fd7ebade55fc0ab1c41be3c8d5',
    'X-Checksum-Sha512': '38155d550d3c29e4c0b9beecb766d8a0d09fb15cd3f72ca5a8ed0a454c23abd0758f8f32cc9d3c54359dd128242d6506ed811c00965f3616017c0ccd3b681ede',
    'Last-Modified': 'Mon, 20 Nov 2023 11:00:15 GMT',
    'ETag': 'c479dc90ebd3c71a8d24b19a9cdc0222dc4705a0',
    'Content-Disposition': 'attachment; filename="Git-2.43.0-64-bit.exe"; filename*=UTF-8\'\'%47%69%74%2D%32%2E%34%33%2E%30%2D%36%34%2D%62%69%74%2E%65%78%65',
    'Expires': 'Thu, 04 Apr 2024 10:30:11 GMT',
    'Cache-Control': 'max-age=1296000',
    'pass-uri': 'git-for-windows-local/v2.43.0.windows.1/Git-2.43.0-64-bit.exe',
    'Accept-Ranges': 'bytes'
}
'''

'''

URL: https://www.runoob.com/http/http-content-type.html

常见的媒体格式类型如下：

    text/html ： HTML格式
    text/plain ：纯文本格式
    text/xml ： XML格式
    image/gif ：gif图片格式
    image/jpeg ：jpg图片格式
    image/png：png图片格式

以application开头的媒体格式类型：

    application/xhtml+xml ：XHTML格式
    application/xml： XML数据格式
    application/atom+xml ：Atom XML聚合格式
    application/json： JSON数据格式
    application/pdf：pdf格式
    application/msword ： Word文档格式
    application/octet-stream ： 二进制流数据（如常见的文件下载）
    application/x-www-form-urlencoded ： <form encType=””>中默认的encType，form表单数据被编码为key/value格式发送到服务器（表单默认的提交数据的格式）

另外一种常见的媒体格式是上传文件之时使用的：

    multipart/form-data ： 需要在表单中进行文件上传时，就需要使用该格式

'''

'''
# 1.0.0.240321a1
from ncmlistdownloader.Downloader import *
import pprint
filename = "C:/Users/Administrator/Desktop/git.exe"
url = "https://mirrors.huaweicloud.com/git-for-windows/v2.43.0.windows.1/Git-2.43.0-64-bit.exe"
file_origin = OriginFile(url = url)
pprint.pprint(file_origin.headers)
file_origin.start(filename = "C:\\Users\\Administrator\\Downloads\\git.exe")
'''

'''
# 1.0.0.240323a1
from ncmlistdownloader.Common import auto_mkdir
filename = "C:\\Users\\Administrator\\Desktop\\new_folder\\new\\folder.txt"
path = ""
for i in filename.split("\\")[:-1]:
    path += i + "\\"
auto_mkdir(path = path)
'''

'''
# 1.0.0.230325a1 获取歌单
from ncmlistdownloader.common.encode_sec_key import *
from ncmlistdownloader.common.global_args import *
from ncmlistdownloader.song import *
import pprint
data = {
    'csrf_token': "",
    'id': "9362578229",
    'n': "0"
}
res = NeteaseParams(encode_data = data, url = PLAYLIST_API).get_resource()
k = res['playlist']['trackIds']
pprint.pprint(k)
kk = [str(i['id']) for i in k]
pprint.pprint(kk)
kkk = [Song(id = j) for j in kk]
kkk[8].get_info()
pprint.pprint(kkk[8].raw_info)
pprint.pprint(kkk[8].url_info)
pprint.pprint(kkk[8].processed_info)
for j in kkk:
    j.get_info()
for j in kkk:
    pprint.pprint(j.processed_info)
'''

'''
# 1.0.0.240330a1
from ncmlistdownloader.playlist import *
import pprint
c = Playlist("2391850012")
k = open("result.txt", "w+", encoding="utf-8")
k.write(str(c.get_info()))
k.close()
'''

'''
# 1.0.0.240401a3
from ncmlistdownloader.playlist import *
from ncmlistdownloader.downloader import *
import pprint
c = Playlist('9091949976')
c.get_info()
c.track[0].get_info()
orf = OriginFile(c.track[0].url_info['song_file'])
pprint.pprint(orf.headers)
pprint.pprint(orf.chunks)
print(orf.url[orf.url.rfind("/") + 1:])
orf.auto_start()
'''

'''
orf = OriginFile(c.track[0].url_info['album_pic'])
pprint.pprint(orf.headers)
pprint.pprint(orf.chunks)
print(orf.url[orf.url.rfind("/") + 1:])
'''

'''
连续请求了三次，重定向的Location:
http://m701.music.126.net/20240401230050/e5a72ac2987914839b46c11906e5a43f/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/8367965002/5755/9777/e9a2/7b692217610db9b03d683dcb9de285fa.mp3
http://m801.music.126.net/20240401230148/4077d3b1586ad41d0e1c63adce972e5a/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/8367965002/5755/9777/e9a2/7b692217610db9b03d683dcb9de285fa.mp3
http://m701.music.126.net/20240401230234/9300c80a3e289616d2cc0100a369d656/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/8367965002/5755/9777/e9a2/7b692217610db9b03d683dcb9de285fa.mp3
从jdymusic开始就一模一样了，music.126.net后面俩应该是与cookie有关的。
'''

'''
# 1.0.0.240402a1
from ncmlistdownloader.playlist import *
import pprint
playlist = Playlist("2391850012")
playlist.get_info()
playlist.get_detail_info()
pprint.pprint(playlist.track[66].raw_info)
'''

'''
# 1.0.0.240404a2
from ncmlistdownloader.common.thread_test import *
k = 0
for i in range(10):
    j = best_thread()
    print(j)
    k += j
num_threads = [1, 2, 4, 8, 16, 32, 64]
k /= 10
for i in num_threads:
    if i > k:
        print(i // 2)
        break
'''

'''
# 1.0.0.240404a2
# https://music.163.com/#/song?id=2083182016
from ncmlistdownloader.song import Song
m = Song("https://music.163.com/#/song?id=2083182016")
m.get_info()
m.song_download()
'''

'''
# 1.0.0.240407b1
from ncmlistdownloader import main
main()

# https://music.163.com/playlist?id=9319926180&userid=1577080369
# D:\ncmlistdownloader_test
'''

'''
#1.0.0.240409a1
from pprint import pprint
from ncmlistdownloader.playlist import *
from ncmlistdownloader.song import *

# p = Playlist('https://music.163.com/playlist?id=9319926180&userid=1577080369')
# p.auto_get_info()
p = Song('https://music.163.com/song?id=446732031&userid=1577080369')
p.get_info()
pprint(p.song_download_enhanced(level = 'lossless'))
'''

'''
#1.0.0.240410a1
from pprint import pprint
from ncmlistdownloader.common.encode_sec_key import *
from ncmlistdownloader.common.global_args import SEARCH_API
d = {
    # "hlpretag": "<span class=\"s-fc7\">",
    # "hlposttag": "</span>",
    # "#/discover": "",
    "s": '陈奕迅',
    "type": "1",
    # "offset": str(0),
    # "total": "true",
    "limit": "20",
    "csrf_token": ""
}
r = NeteaseParams(url = SEARCH_API, encode_data = d)
c = {
    'MUSIC_U': ""
}
c['MUSIC_U'] = str(input('your cookies\' MUSIC_U:'))
rd = r.get_resource(cookies = c)
with open('result_1.json', 'w+', encoding = 'UTF-8') as f:
    json.dump(rd, f, ensure_ascii = False, indent = 2)

from ncmlistdownloader.song import *
s = Song(id = str(input('an url/id of a song(must VIP-only):')))
s.get_info()
input('if you have VIP, press Enter.')
ee = s.song_download_enhanced(level = 'lossless', cookies = c)
with open('result_2.json', 'w+', encoding = 'UTF-8') as f:
    f.write(str(ee))
'''

'''
from ncmlistdownloader.cmd import *
d = Page()
d.renderer()


from ncmlistdownloader.cmd import *


from ncmlistdownloader.playlist import *
from pprint import pprint
p = Playlist('9091949976')
p.auto_get_info()
pprint(p.raw_info)
'''

'''
# 免费VIP下载测试，看起来不行喔TAT，羊毛薅不到了；但是私密歌单倒可以。
from ncmlistdownloader.song import *
from pathlib import Path
s = Song(id = "https://music.163.com/song?id=1305364097&userid=1577080369")
s.get_info()
d = str(Path.home()) + '/Downloads/ncmld_downloads/'
s.filename_format = d + "$title$ - $artist$"
c = {'MUSIC_U':"0You Can't GET My Cookies!!!E"}
k = s.song_download_enhanced(level = 'lossless', cookies = c)
print(k)

from pprint import pprint
from ncmlistdownloader.playlist import *
c = {'MUSIC_U':"0You Can't GET My Cookies!!!E"}
p = Playlist("https://music.163.com/playlist?id=9269203337")
p.get_info(cookies=c)
pprint(p.raw_info)
'''

import pprint
from ncmlistdownloader.common.encode_sec_key import *
from ncmlistdownloader.common.global_args import *
u = 'http://interface.music.163.com/eapi/batch/api/cloudsearch/pc'
d = {
    # "hlpretag": "<span class=\"s-fc7\">",
    # "hlposttag": "</span>",
    # "#/discover": "",
    "s": '陈奕迅',
    "type": "1000",
    # "offset": str(0),
    # "total": "true",
    "limit": "20",
    "csrf_token": ""
}
p = NeteaseParams(url = u, encode_data = d)
pprint.pprint(p.get_resource())

'''
'http://interface.music.163.com/eapi/batch'
'/api/cloudsearch/pc'
1: 单曲, 10: 专辑, 100: 歌手, 1000: 歌单, 1002: 用户, 1004: MV, 1006: 歌词, 1009: 电台, 1014: 视频
'''

'''
from ncmlistdownloader.cmd import *
main()
'''