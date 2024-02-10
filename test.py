import ListDownloader
import pprint

test_p = ListDownloader.Playlist("2391850012")
test_p.get_resource()
for i in test_p.tracks:
    i.get_resource()
    pprint.pprint(i.info)
