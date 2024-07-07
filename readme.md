# 163ListDownloader_NexT

**目前最新版本是: `Core.Ver.1.3.2.240707`**

## 简介

这堆东西源于我想下下我网易云上的歌单，然后就断断续续写了两年，最后发展成这个个人认为蛮有意义的小程序。

现在能扫码登录，下载无损音质（前提是你有VIP啦），选择是否下载歌词，添加封面啥的。

使用的API在网上公开，所以（可能）不会造成什么法律上的风险。

## 163ListDownloader_NexT 建库声明

这将会是新的开始：一个更好的库，和一个更好的UI（虽然目前来看可能还是基于Win32的Tkinter）！

所以可以紧跟我们的脚步，看看究竟会发生什么。

## 安装与使用

### 可执行文件 (.exe)

在 [“发行版”](https://gitee.com/CooooldWind/163ListDownloader_NexT/releases) 界面下载最新 release 版本的可执行文件 (.exe)，然后双击运行。

### 安装库

目前已经将库部署至 Pypi，使用 ```pip install ncmlistdownloader``` 下载。

镜像库会有延迟，一般在 5~10 分钟。

### 使用库

本文会向您展示使用这个库的方法。

#### 命令行

如果是普通用户，更加推荐使用命令行，除非有特殊需求。

在命令行安装完库以后，可以在命令行输入 ```ncmlistdownloader``` 命令直接下载。这是目前最方便快捷的方式。

#### 手写代码并运行

以下是一个能正常运行并实现部分功能的最简代码。

```python
from ncmlistdownloader.playlist import *
p = Playlist('一个id或者url')
p.auto_get_info()
for i in p.track:
   i.song_download()
```

可以打开每个文件都看看注释。

其他更加深入的自定义功能请自行探索。

### 其他

关于之前的 _old 版本，欢迎 [点击链接](https://github.com/Cooooldwind/163ListDownloader_old) 。

## 冷知识

### 1 - 虽然是 240404b4 但是是 24/04/05 发的

第一个Beta版本 ```1.0.0.240404b4``` 实际上到第二天 (2024/04/05) 才调试好并发布。但是那个版本其实还是有bug（笑

### 2 - 这貌似比较实用...？

如果直接 ```import ncmlistdownloader``` 然后 ```p = ncmlistdownloader.Playlist(id="")``` 貌似也是可以的喔（喜

### 3 - 求Star，但是跳转到issues界面

[![pkW3eQe.png](https://s21.ax1x.com/2024/07/07/pkW3eQe.png)](https://imgse.com/i/pkW3eQe)

下个版本一定改（罢？）

### 4 - 不存在的（至少目前是

都说了没有了你看个锤子喔！

------

[CooooldWind_](https://cooooldwind.netlify.app) 制作，该 Repo 以及 Pypi 上的 ncmlistdownloader 库都在 AGPL-3.0 协议保护之下。

特别鸣谢：[是青旨啊](https://sayqz.com)，[bilibili@半岛的孤城](https://space.bilibili.com/32187583)

文本编辑于 Core.Ver.1.3.2.240707

2024.02.20 CooooldWind_

latest_update: 2024.07.07 CooooldWind_
