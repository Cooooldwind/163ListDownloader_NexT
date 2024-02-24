'''
ncmlistdownloader/cmd_script.py
Core.Ver.1.0.0.240224a2
Author: CooooldWind_
'''
import time
import pprint
import multiprocessing
import ncmlistdownloader as nld

'''
def func(id, d, fnf, lv, t_sum):
    print("Progress is running at", os.getpid())
    test_p = ncmlistdownloader.Playlist(str(id))
    test_p.get_resource()
    print("Info-reading succeed.")
    for ap in test_p.tracks:
        ap.get_resource()
        ap.initialize(t_sum, fnf, lv, d)
    print("Initialized.")
    for ap in test_p.tracks:
        ap.start()
    print("Pushed.")
    while True:
        back = True
        for ap in test_p.tracks:
            if ap.finish == False:
                pprint.pprint(ap.downloading_info)
                back = False
        if back:
            break
        time.sleep(0.5)
    print("Download succeed.")

def main():
    print("163ListDownloader CMD Ver.")
    print("Core.Ver.1.0.0.240220a11 / Made by CooooldWind_")
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
    p.join()
    print("Start! The program will shutdown after downloading, please DO NOT TOUCH THE PROGRAM before it.")

if __name__ == "__main__":
    main()
'''  

def monitor(i):
    while i.finish == False:
        pprint.pprint(i.downloading_info)
        time.sleep(0.5)

if __name__ == "__main__":
    print("163ListDownloader CMD Ver.")
    print("Core.Ver.1.0.0.240224a1 / Made by CooooldWind_")
    print("Warning: It's an Alpha Version.")
    multiprocessing.freeze_support()
    p = nld.Playlist()
    id = str(input("ID/Url: "))
    d = str(input("Dir: "))
    fnf = str(input("Filename format: "))
    lv = int(input("Level: "))
    p.get_resource(id)
    print("Playlist info-reading succeed.")
    for i in p.tracks:
        print("Downloading:" + str(i.id['id']))
        i.get_resource()
        print("Music info-reading succeed.")
        i.initialize(0, fnf, lv, d)
        print("Initialized.")
        ap = multiprocessing.Process(target = i.start_single())
        ap.start()
        print("Succeed.")