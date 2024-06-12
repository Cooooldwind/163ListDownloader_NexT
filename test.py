import ncmlistdownloader.music as nld_music
from pprint import pprint

"""m = nld_music.Music("https://music.163.com/song?id=2146779694&userid=1577080369")
result = m.get_info(
    MUSIC_U="",
    level=4,
)
with open("C:\\Users\\Administrator\\Desktop\\11.txt", "w+") as f:
    f.write(m.lyric)"""
m = nld_music.Music("https://music.163.com/song?id=2146779694&userid=1577080369")
r = m.get_info()
pprint(r)
