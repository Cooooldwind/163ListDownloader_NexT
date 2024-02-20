import ncmlistdownloader as NLD
import pprint
import time
p = NLD.Playlist("9319926180")
p.get_resource()
for i in p.tracks:
	while True:
		flag = False
		try:i.get_resource()
		except:flag = True
		if flag == False: break
	i.initialize(fnf = "$name$ - $artist$", lv = 4, tc_sum = 4, d="C:\\Users\\Administrator\\Desktop\\test\\")
for i in p.tracks:
	i.start()
while True:
	for i in p.tracks:
		flag = True
		if i.finish == False:
			flag = False
		pprint.pprint(i.downloading_info)
	time.sleep(0.25)
	if flag: break