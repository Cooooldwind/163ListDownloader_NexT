"""
这是一个基于新的downloader的下载器的测试
他会下载最新版的ncmlistdownloader_cmd并放在C盘根目录下
同时会显示下载百分比，已花费的时间，速度和剩余时间
"""

from ncmlistdownloader.downloader import OriginFile
import time
from tqdm import tqdm

def start(of: OriginFile):
    of.start()
    last_size = 0
    now_size = 0
    tot_size = of.tot_size
    with tqdm(total = tot_size, unit= "B", unit_scale=True) as pbar:
        while of.now_size < of.tot_size:
            last_size = now_size
            now_size = of.now_size
            pbar.update(now_size - last_size)

of = OriginFile(url = "https://gitee.com/CooooldWind/163ListDownloader_NexT/releases/download/Ver.1.3.2.240707/ncmlistdownloader_cmd_1.3.2.240707.exe")
print("Start downloading.")
start(of)
print("Writing...")
with open("C:/ncmlistdownloader_cmd_1.3.2.240707.exe", "wb") as f:
    f.write(of.data)
print("Succeed!")
