import list_downloader
test_p = list_downloader.Playlist("9293890250") #把id删掉，填上歌单id
test_p.get_resource()
d = "C:\\Users\\Administrator\\Downloads\\dik\\" #把dir删掉填上存储目录，务必以正斜杠或反斜杠结尾
p = test_p.tracks[1]
p.get_resource()
p.song_download(3, d, "test")
p.lyric_download(d, "test")
p.cover_download(d, "test", 320)
p.attribute_write(d, "test", p.info['song_type'])
p.cover_write(d, "test", p.info['song_type'], d, "test")
p.lyric_write(d, "test", p.info['song_type'], d, "test")