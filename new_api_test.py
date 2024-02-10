import ListDownloader
import pprint

kurl = ListDownloader.global_args.SONG_FILE_URL

result = ListDownloader.encode_sec_key.NeteaseParams(
    encode_data = {
        'csrf_token': '',
        'ids': ["1382576173"],
        'level':"standard",
        'encodeType':'aac',
    },
    url = kurl).get_resource()
pprint.pprint(result)
