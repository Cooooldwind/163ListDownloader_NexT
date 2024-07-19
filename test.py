"""
这是一个基于新的downloader的下载器的测试
他会下载最新版的ncmlistdownloader_cmd并放在C盘根目录下
同时会显示下载百分比，已花费的时间，速度和剩余时间
"""

from ncmlistdownloader.downloader import OriginFile
import time
from pprint import pprint

def start(of: OriginFile):
    start_time = int(round(time.time() * 1000))
    of.start()
    last_time = int(round(time.time() * 1000))
    now_time = int(round(time.time() * 1000))
    last_size = 0
    now_size = 0
    tot_size = of.tot_size
    while of.now_size != of.tot_size:
        time.sleep(0.5)
        last_time = now_time
        last_size = now_size
        now_size = of.now_size
        now_time = int(round(time.time() * 1000))
        percentage = now_size / tot_size // 0.0001 / 100
        speed = (now_size - last_size) / (now_time - last_time) # Bytes/ms
        speed_mbps = speed * 1000 / 1048576 // 0.01 / 100
        est_time = (tot_size - now_size) / speed / 1000 // 0.01 / 100
        costed_time = (now_time - start_time) / 1000 // 0.01 / 100
        print(f"{percentage}%\nCosted:{costed_time}s\n{speed_mbps}MB/s\nEst.{est_time}s\n")

of = OriginFile(url = "https://gitee.com/CooooldWind/163ListDownloader_NexT/releases/download/Ver.1.3.2.240707/ncmlistdownloader_cmd_1.3.2.240707.exe")
start(of)
print("Writing...")
with open("C:/ncmlistdownloader_cmd_1.3.2.240707.exe", "wb") as f:
    f.write(of.data)
print("Succeed!")
