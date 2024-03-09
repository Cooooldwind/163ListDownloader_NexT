import ncmlistdownloader as NLD
import pprint
import time
p = NLD.Playlist()
p.get_resource("2391850012")
'''
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
'''
k = p.tracks[0]
k.get_resource()
k.initialize(lv = 3)
k.start_single()
