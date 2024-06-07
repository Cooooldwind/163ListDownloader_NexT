import ncmlistdownloader.music as nld_music

m = nld_music.Music("https://music.163.com/song?id=1897685644&userid=1577080369")
print(
    m.music_download(
        level=4,
        MUSIC_U="",
    )
)
