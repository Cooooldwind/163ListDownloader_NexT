'''
cmd.py
Core.Ver.1.0.0.240220a2
Author: CooooldWind_
'''
import time
import pprint
import os
import sys
import multiprocessing
import threading
import __init__

def func(id, d, fnf, lv, t_sum):
    print("Progress is running at", os.getpid())
    test_p = __init__.Playlist(str(id))
    test_p.get_resource()
    print("Info-reading succeed.")
    tc = threading.Semaphore(t_sum)
    for p in test_p.tracks:
        p.get_resource()
        p.initialize(tc, fnf, lv, d)
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
    print("Warning: It's an Alpha Version.")
    multiprocessing.freeze_support()
    d = str(input("dir: "))
    id = str(input("id/url: "))
    if id.find("music.163.com") != -1:
        id = id.split("id=")[1].split("&user")[0]
    fnf = str(input("filename format: "))
    lv = int(input("level: "))
    t_sum = int(input("thread sum: "))
    p = multiprocessing.Process(target = func, args = (id, d, fnf, lv, t_sum))
    p.start()
    print("Start!")

if __name__ == "__main__":
    main()
    
        