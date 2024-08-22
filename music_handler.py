import mutagen
import magic
from mutagen.id3 import ID3, APIC
from mutagen.flac import Picture
import imghdr
from PIL import Image  # 用于处理图片

# 定义不同格式的常见标签键
ID3V1_TAG_KEYS = ['title', 'artist', 'album', 'year', 'comment', 'track', 'genre']
ID3V2_TAG_KEYS = ['TIT2', 'TPE1', 'TALB', 'TYER', 'COMM', 'TRCK', 'TCON']
FLAC_TAG_KEYS = ['TITLE', 'ARTIST', 'ALBUM', 'DATE', 'COMMENT', 'TRACKNUMBER', 'GENRE']
OGG_TAG_KEYS = ['TITLE', 'ARTIST', 'ALBUM', 'DATE', 'COMMENT', 'TRACKNUMBER', 'GENRE']
M4A_TAG_KEYS = ['title', 'artist', 'album', 'year', 'comment', 'trackNumber', 'genre']

class MusicFileHandler:
    """
    一个用于处理多种音乐文件格式（MP3、FLAC、OGG、M4A）的标签读写操作的类
    """

    def __init__(self, file_path):
        """
        初始化类，根据文件路径加载音乐文件

        参数：
        file_path (str): 音乐文件的路径
        """
        self.file_path = file_path
        self.mime_type = magic.Magic(mime=True).from_file(file_path)
        self.file_type = self.detect_file_type()
        self.music_file = mutagen.File(file_path)

    def detect_file_type(self):
        """
        根据文件扩展名和 magic 库检测的 MIME 类型来确定文件类型

        返回：
        str: 文件类型（'mp3', 'flac', 'ogg','m4a' 等）
        """
        file_extension = self.file_path.split('.')[-1].lower()
        if file_extension =='mp3' and self.mime_type.startswith('audio/mpeg'):
            return'mp3'
        elif file_extension == 'flac' and self.mime_type == 'audio/x-flac':
            return 'flac'
        elif file_extension == 'ogg' and self.mime_type.startswith('audio/ogg'):
            return 'ogg'
        elif file_extension =='m4a' and self.mime_type.startswith('audio/mp4'):
            return'm4a'
        else:
            raise ValueError(f"不支持的音乐文件格式或文件后缀与实际格式不匹配。magic 认为可能的格式是: {self.mime_type}")

        def process_cover(self, cover_data, new_size=(32, 32)):
        """
        处理封面图片
        参数：
        cover_data (bytes): 封面图片数据
        new_size (tuple): 新的尺寸，默认为 (32, 32)
        """
        image_type = imghdr.what(None, h=cover_data)
        if image_type == 'gif':
            raise ValueError("不支持 GIF 格式的封面，封面应为 JPEG 格式")
        elif image_type == 'png':
            # 将 PNG 转换为 JPEG
            image = Image.open(io.BytesIO(cover_data))
            new_image = image.convert('RGB')
            output = io.BytesIO()
            new_image.save(output, format='JPEG')
            cover_data = output.getvalue()
        # 调整封面图片大小
        image = Image.open(io.BytesIO(cover_data))
        resized_image = image.resize(new_size)
        output = io.BytesIO()
        resized_image.save(output, format='JPEG')
        cover_data = output.getvalue()

    def add_cover(self, cover_data):
        """
        添加封面到音乐文件
        参数：
        cover_data (bytes): 封面图片数据
        """
        self.process_cover(cover_data)
        if self.file_type =='mp3':
            self.music_file.tags.add(APIC(encoding=3, mime='image/jpeg', type=1, desc='Cover', data=cover_data))
            self.music_file.save()
        elif self.file_type == 'flac':
            picture = Picture()
            picture.type = 1
            picture.mime = 'image/jpeg'
            picture.data = cover_data
            self.music_file['pictures'] = [picture]
            self.music_file.save()
