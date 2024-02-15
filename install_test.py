import ncmlistdownloader
p = ncmlistdownloader.Playlist(9293890250)
p.get_resource()
for i in p.tracks:
    i.get_resource()
    i.initialize(tc_sum = 2)
for i in p.tracks:
    i.start()