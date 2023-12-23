import ListDownloader
import pprint

test_p = ListDownloader.Playlist("2998665333")
test_p.get_resource()
for i in test_p.tracks:
    i.get_resource()
    pprint.pprint(i.info)
