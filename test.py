import ncmlistdownloader.encode

d = ncmlistdownloader.encode.NeteaseParams(
    url="https://music.163.com/weapi/v3/song/detail",
    encode_data={
        "c": str([{"id": str(407007703)}]),
        "csrf_token": "",
    },
)
import pprint

pprint.pprint(d.get_resource())
