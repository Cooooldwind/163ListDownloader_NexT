"""
ncmlistdownloader/login.py
Ver.1.3.0.240707
Author: CooooldWind_
"""

import pyqrcode
import tkinter
import time
from ncmlistdownloader.common.encode_sec_key import NeteaseParams

def login():
    unikey_url = "https://music.163.com/weapi/login/qrcode/unikey?csrf_token="
    np = NeteaseParams(url = unikey_url, encode_data = {"type": "1"})
    unikey = np.get_resource()['unikey']
    qrcode_url =f"https://music.163.com/login?codekey={unikey}&refer=scan"

    code=pyqrcode.create(qrcode_url)#需要显示中文encoding='UTF-8'即可
    cXbm=code.xbm(scale=5)#scale生成的二维码图片比例大小

    win=tkinter.Tk()
    tkBap=tkinter.BitmapImage(data=cXbm)
    tkBap.config(foreground="black")
    tkBap.config(background="white")
    tLable=tkinter.Label(image=tkBap)
    tLable.pack()
    win.title("163ListDownloader - QRCode")

    check_login_url = "https://music.163.com/weapi/login/qrcode/client/login"
    np_2 = NeteaseParams(url = check_login_url, encode_data = {"key": unikey, "type": "1"})

    scan = False
    notice = False
    fail = False

    while True:
        r = np_2.get_resource()
        if r['code'] == 800:
            print("Login Failed.")
            fail = True
            break
        elif r['code'] == 802 and scan == False:
            scan = True
            print(f"{r['nickname']} Login...")
        elif r['code'] == 801 and notice == False:
            notice = True
            print("Please login.")
        elif r['code'] == 803:
            print("succeed.")
            break
        win.update()
        time.sleep(1)

    if not fail:
        c = np_2.session.cookies.items()
        print(c)
        for i in c:
            if i[0] == 'MUSIC_U': return i[1]
