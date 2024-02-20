'''
cmd_script.py
Core.Ver.1.0.0.240220a10
Author: CooooldWind_
'''
import time
import pprint
import os
import multiprocessing
import ncmlistdownloader

def func(id, d, fnf, lv, t_sum):
    print("Progress is running at", os.getpid())
    test_p = ncmlistdownloader.Playlist(str(id))
    test_p.get_resource()
    print("Info-reading succeed.")
    for p in test_p.tracks:
        p.get_resource()
        p.initialize(t_sum, fnf, lv, d)
        p.start()
    while True:
        back = True
        for p in test_p.tracks:
            if p.finish == False:
                pprint.pprint(p.downloading_info)
                back = False
        if back:
            break
        time.sleep(0.5)
    print("Download succeed.")

def main():
    print("163ListDownloader CMD Ver.")
    print("Core.Ver.1.0.0.240220a10 / Made by CooooldWind_")
    print("Warning: It's an Alpha Version.")
    multiprocessing.freeze_support()
    d = str(input("Dir: "))
    id = str(input("ID/Url: "))
    if id.find("music.163.com") != -1:
        id = id.split("id=")[1].split("&user")[0]
    fnf = str(input("Filename format: "))
    lv = int(input("Level: "))
    t_sum = int(input("Thread sum: "))
    p = multiprocessing.Process(target = func, args = (id, d, fnf, lv, t_sum))
    p.start()
    print("Start! The program will shutdown after downloading, please DO NOT TOUCH THE PROGRAM before it.")

if __name__ == "__main__":
    main()
    
        