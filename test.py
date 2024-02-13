import time
import pprint
import threading
import list_downloader
test_p = list_downloader.Playlist("9293890250") #把id删掉，填上歌单id
test_p.get_resource()
d = "C:\\Users\\Administrator\\Downloads\\dik\\" #把dir删掉填上存储目录，务必以正斜杠或反斜杠结尾
tc = threading.Semaphore(4)
for p in test_p.tracks:
    p.get_resource()
    p.initialize(d, tc)
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
    time.sleep(1)
