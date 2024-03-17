# 163ListDownloader_NexT

这将会是新的开始：一个更好的库，和一个更好的UI（虽然还是基于Win32的Tkinter）！

所以可以紧跟我们的脚步，看看究竟会发生什么。

## 这里是Settled分支

我正在整理那坨400多行的shit，他会看起来好一点罢（确信

## 2024年3月10日 - 关于TuneFree终止服务的通知

在二月，我们基于TuneFree的API进行了项目制作。很遗憾的是，由于不可控因素，该API在3月1日被迫关停。我们在近日更新了接口，目前暂不支持VIP歌曲下载。特此通知。

## 安装与使用

### 安装库

目前已经将库部署至 Pypi，使用```pip install ncmlistdownloader```下载。

### 使用库

本文会向您展示使用这个库的方法。

#### 手写代码并运行

以下是一个能正常运行并实现部分功能的最简代码。

```python
import ncmlistdownloader as NLD
p = NLD.Playlist("歌单id")
p.get_resource()
for i in p.tracks:
 i.get_resource()
 i.initialize(fnf = "$name$ - $artist$", lv=3, tc_sum = 4)
 i.start()
```

```initialize```的参数：

1. ```tc_sum```：多线程的线程数：默认 8 ；

2. ```fnf```: 文件名的格式，以下是文件名格式的规范:

   > 1. 用 ```"$xxx$"``` 表示一些内容:
   > 2. ```"$id$"``` 是歌曲id；```"$name$"``` 是歌曲名称；
   > 3. ```"$artist$"``` 是歌手；```"$album$"``` 是专辑；
   > 4. 输入 ```"$"``` 用 ```"$$"``` ；

3. ```lv```: 品质（由低到高1~8）默认1；

4. ```d```: 存储路径（结尾必须是 “/” 或 “\” ）默认创建子文件夹 “download/” 。

如果想添加查看进度的功能，把以下代码放在上方代码块的底部。

```python
import pprint
while True:
 for i in p.tracks:
 pprint.pprint(i.downloading_info)
```

其他更加深入的自定义功能请自行探索，我们为大家准备了（应该是）广阔的发挥空间。

#### 命令行

在命令行利用```pip install ncmlistdownloader```安装完库以后，可以在命令行输入```163ListDownloader```命令直接下载。这是目前最方便快捷的方式。

### 其他

关于之前的 _old 版本，欢迎[点击链接](https://github.com/Cooooldwind/163ListDownloader_old)。

------

[CooooldWind_](https://cooooldwind.netlify.app) 制作，该 Repo 以及 Pypi 上的 ncmlistdownloader 库都在 AGPL-3.0 协议保护之下。

特别鸣谢：[是青旨啊](https://sayqz.com)，[bilibili@半岛的孤城](https://space.bilibili.com/32187583)

文本编辑于 Core.Ver.1.0.0.240303a2

2024.02.20 CooooldWind_

2024.03.02 CooooldWind_(紧急更新)
