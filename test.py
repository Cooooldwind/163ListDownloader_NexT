import ListDownloader
test_p = ListDownloader.Playlist("id") #把id删掉，填上歌单id
test_p.get_resource()
d = "dir" #把dir删掉填上存储目录，务必以正斜杠或反斜杠结尾
def run(waiting):
    fn = waiting.info['name'] + " - " + waiting.info['artist_str'] #两个互换就是“歌手-歌曲名”的形式
    waiting.song_download(3, d, fn) #歌曲下载。第一个参数是音质，1~8如下。
    '''
    1 standard 标准
    2 higher 较高
    3 exhigh 极高
    4 lossless 无损
    5 hires Hi-Res模式
    6 jyeffect 高清环绕声
    7 sky 沉浸环绕声
    8 jymaster 超清母带
    '''
    tp = waiting.info['song_type']
    waiting.lyric_download(d, fn) #歌词下载
    waiting.cover_download(d, fn) #封面下载
    waiting.attribute_write(d, fn, tp) #属性填写
    waiting.cover_write(d, fn, tp, d, fn) #封面注入到属性
    waiting.lyric_write(d, fn, tp, d, fn) #歌词注入到属性

for p in test_p.tracks:
    p.get_resource()
for p in test_p.tracks:
    run(p)
