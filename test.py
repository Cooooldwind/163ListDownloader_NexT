'''
test.py
Core.Ver.1.0.0.240325a1
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
#1.0.0.240320a2
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
#1.0.0.240321a1
from ncmlistdownloader.Downloader import *
import pprint
filename = "C:/Users/Administrator/Desktop/git.exe"
url = "https://mirrors.huaweicloud.com/git-for-windows/v2.43.0.windows.1/Git-2.43.0-64-bit.exe"
file_origin = OriginFile(url = url)
pprint.pprint(file_origin.headers)
file_origin.start(filename = "C:\\Users\\Administrator\\Downloads\\git.exe")
'''

'''
#1.0.0.240323a1
from ncmlistdownloader.Common import auto_mkdir
filename = "C:\\Users\\Administrator\\Desktop\\new_folder\\new\\folder.txt"
path = ""
for i in filename.split("\\")[:-1]:
    path += i + "\\"
auto_mkdir(path = path)
'''

#1.0.0.230325a1 获取歌单
from ncmlistdownloader.Common.encode_sec_key import *
from ncmlistdownloader.Common.global_args import *
from ncmlistdownloader.Song import *
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
'''
for j in kkk:
    j.get_info()
for j in kkk:
    pprint.pprint(j.processed_info)
'''