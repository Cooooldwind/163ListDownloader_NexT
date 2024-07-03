# -*- coding: utf-8 -*-
import base64
import codecs
import pickle
from Crypto.Cipher import AES     
#解决方法:安装crypto后，将\venv\Lib\site-packages\crypto的crypto文件夹名首字母c改成大写C就可以了
import qrcode
import agent
from threading import Thread
import time
import requests
from io import BytesIO
from PIL import Image
import os
from pprint import pprint
requests.packages.urllib3.disable_warnings()
headers = {'User-Agent': agent.get_user_agents(),'Referer':'https://music.163.com/'}


from ncmlistdownloader.encode import NeteaseParams

class showpng(Thread):
    def __init__(self, data):
        Thread.__init__(self)
        self.data = data

    def run(self):
        img = Image.open(BytesIO(self.data))
        img.show()

#解密params和encSecKey值
def keys(key):
    while len(key) % 16 != 0:
        key += '\0'
    return str.encode(key)

def AES_aes(t, key, iv):
    p = lambda s: s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)
    encrypt = str(base64.encodebytes(AES.new(keys(key), AES.MODE_CBC,keys(iv)).encrypt(str.encode(p(t)))), encoding='utf-8')
    return encrypt

def RSA_rsa(i, e, f):
    return format(int(codecs.encode(i[::-1].encode('utf-8'), 'hex_codec'), 16) ** int(e, 16) % int(f, 16), 'x').zfill(256)

#获取的参数
key = agent.S() # i6c的值

d = str({'key': key, 'type': "1", 'csrf_token': ""})
e = "010001"# (["流泪", "强"])的值
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud" # (["爱心", "女孩", "惊恐", "大笑"])的值

iv = "0102030405060708"  # 偏移量
i = agent.a()  # 随机生成长度为16的字符串

def params():
    return AES_aes(AES_aes(d, g, iv), i, iv)   #g 和 i 都是key代替

def encSecKey():
    return RSA_rsa(i, e, f)

#判断cookie是否有效
def islogin(session):
    try:
        session.cookies.load(ignore_discard=True)
    except Exception:
        pass
    csrf_token = session.cookies.get('__csrf')
    c = str({'csrf_token': csrf_token})
    try:
        loginurl = session.post('https://music.163.com/weapi/w/nuser/account/get?csrf_token={}'.format(csrf_token), data={'params': AES_aes(AES_aes(c, g, iv), i, iv), 'encSecKey': encSecKey()}, headers=headers).json()
        if '200' in str(loginurl['code']):
            print('Cookies值有效：',loginurl['profile']['nickname'],'，已登录！')
            return session, True
        else:
            print('Cookies值已经失效，请重新扫码登录！')
            return session, False
    except:
        print('Cookies值已经失效，请重新扫码登录！')
        return session, False

#登录扫码保存cookie
def wyylogin():
    # 写入
    session = requests.session()
    if not os.path.exists('wyycookies.cookie'):
        with open('wyycookies.cookie', 'wb') as f:
            pickle.dump(session.cookies, f)
    # 读取
    session.cookies = pickle.load(open('wyycookies.cookie', 'rb'))
    session, status = islogin(session)
    if not status:
        getlogin = session.post('https://music.163.com/weapi/login/qrcode/unikey?csrf_token=', data={'params': params(), 'encSecKey': encSecKey()}, headers=headers).json()
        pprint(getlogin)
        pngurl = 'https://music.163.com/login?codekey=' + getlogin['unikey'] + '&refer=scan'
        print(pngurl)
        qr = qrcode.QRCode()
        qr.add_data(pngurl)
        img = qr.make_image()
        # 缓存的好处就是不需要保存本地
        a = BytesIO()
        img.save(a, 'png')
        png = a.getvalue()
        a.close()
        # 打开二维码进行扫码操作
        t = showpng(png)
        t.start()
        tokenurl = 'https://music.163.com/weapi/login/qrcode/client/login?csrf_token='
        while 1:
            u = str({'key': getlogin['unikey'], 'type': "1", 'csrf_token': ""})
            qrcodedata = session.post(tokenurl, data={'params': AES_aes(AES_aes(u, g, iv), i, iv), 'encSecKey': encSecKey()}, headers=headers).json()
            if '801' in str(qrcodedata['code']):
                print('二维码未失效，请扫码！')
            elif '802' in str(qrcodedata['code']):
                print('已扫码，请确认！')
            elif '803' in str(qrcodedata['code']):
                print('已确认，登入成功！')
                break
            else:
                print('其他：', qrcodedata)
            time.sleep(2)
        with open('wyycookies.cookie', 'wb') as f:
            pickle.dump(session.cookies, f)
    return session
    
if __name__ == '__main__':
    wyylogin()


