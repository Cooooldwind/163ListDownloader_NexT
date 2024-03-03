from setuptools import setup, find_packages
from version import VERSION as V
setup(
    classifiers = [
        # 发展时期
        'Development Status :: 3 - Alpha',
        # 开发的目标用户
        'Intended Audience :: Customer Service',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        # 属于什么类型
        'Topic :: Communications :: File Sharing',
        'Topic :: Internet',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: CD Audio',
        'Topic :: Multimedia :: Sound/Audio :: Editors',
        # 许可证信息
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        # 目标 Python 版本
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
		'Programming Language :: Python :: 3.11',
		'Programming Language :: Python :: 3.12',
		'Programming Language :: Python :: 3.13',
    ],
    name = 'ncmlistdownloader',
    version = str(V[0]) + '.' + str(V[1]) + '.' + str(V[2]) + '.' + str(V[3]) + str(V[4]) + str(V[5]),
    description = '获取网易云音乐歌单数据，下载音乐，主动添加元信息。',
    author = 'CooooldWind_',
    url = 'https://github.com/Cooooldwind/163ListDownloader_NexT',
    packages = find_packages(),
    install_requires = ['pycryptodome','pillow','mutagen','requests',],
    entry_points = {'console_scripts': ['163ListDownloader = ncmlistdownloader.cmd_script:main']},
)