import ListDownloader
import pprint

test_p = ListDownloader.Playlist("2391850012")
test_p.get_resource()
'''
for i in test_p.tracks:
    i.get_resource()
    pprint.pprint(i.response)
'''

test_p.tracks[0].get_resource()
pprint.pprint(test_p.tracks[0].response)
pprint.pprint(test_p.tracks[0].info)
'''test_p.tracks[0].song_download(5, "C:\\Users\\Administrator\\Downloads\\", "test")'''
'''test_p.tracks[0].cover_download("C:\\Users\\Administrator\\Downloads\\", "test2", size = 128)'''
test_p.tracks[0].attribute_write("C:\\Users\\Administrator\\Downloads\\", "test", "flac")