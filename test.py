import ncmlistdownloader.music as nld_music
m = nld_music.Music("https://music.163.com/song?id=1897685644&userid=1577080369", auto_info_get=False)
import pprint
pprint.pprint(m.raw_info)
m.get_info()
pprint.pprint(m.raw_info)
