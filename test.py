import time
import pprint
import multiprocessing
import threading
import list_downloader

def func(id, d, fnf, lv, t_sum):
    test_p = list_downloader.Playlist(str(id))
    test_p.get_resource()
    tc = threading.Semaphore(t_sum)
    for p in test_p.tracks:
        p.get_resource()
        p.initialize(d, tc, fnf, lv)
    for p in test_p.tracks:
        p.start()
        time.sleep(0)
    while True:
        back = True
        for p in test_p.tracks:
            if p.finish == False:
                pprint.pprint(p.downloading_info)
                back = False
        if back:
            break
        time.sleep(0.2)

if __name__ == "__main__":
    d = str(input("dir: "))
    id = str(input("id/url: "))
    if id.find("music.163.com") != -1:
        id = id.split("id=")[1].split("&user")[0]
    fnf = str(input("filename format: "))
    lv = int(input("level: "))
    t_sum = int(input("thread sum: "))
    p = multiprocessing.Process(target = func, args = (id, d, fnf, lv, t_sum))
    p.start()
    p.join()
        