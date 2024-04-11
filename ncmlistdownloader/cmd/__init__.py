'''
ncmlistdownloader/cmd/__init__.py
Core.Ver.1.0.0.240411a1
Author: CooooldWind_
P.S.: 实现几个页面，可以来回切换，对应运行函数。
'''

from ncmlistdownloader.cmd.module import *
from ncmlistdownloader.playlist import *

def main():
    def exit_c():
        return
    def get_detail_succeed(pl: Playlist):
        p = Page()
        p.script = []
        p.title = "163ListDownloader CMD Ver - Playlist-get Succeed"
        p.width = 80
        info = [
            f"\"{pl.title} (by:{pl.creator})\" got.",
        ]
        for i in info:
            p.script.append(Script(info = i, justify = "center"))
        p.script.append(Script(info = ''))
        command: list[Command] = []
        command.append(Command(func = exit_c, key = 0, info = 'Exit'))
        command.append(Command(func = main, key = 1, info = 'Back to Main.'))
        for i in command:
            p.script.append(Script(info = i.str_back(), justify = "left"))
        p.renderer()
        command_input = int(input(">> "))
        for i in command:
            if i.key == command_input:
                i.func()
    def get_detail():
        p_gd = Page()
        p_gd.script = []
        p_gd.title = "163ListDownloader CMD Ver - Get Start"
        p_gd.width = 80
        info = [
            "Press your playlist's id/url below.",
        ]
        for i in info:
            p_gd.script.append(Script(info = i, justify = "left"))
        p_gd.script.append(Script(info = ''))
        p_gd.renderer()
        id_input = str(input(">> "))
        pl = Playlist(id_input)
        pl.auto_get_info()
        get_detail_succeed(pl)
    p = Page()
    p.script = []
    p.title = "163ListDownloader CMD Ver - Main Page"
    p.width = 80
    info = [
        "163ListDownloader CMD Ver.",
        "Made by CooooldWind_",
        "Warning: It's an Alpha Version. It may has a lot of bugs.",
        "If you met them, click the links below:",
        "Gitee: https://gitee.com/CooooldWind/163ListDownloader_NexT/issues",
        "GitHub: https://github.com/CooooldWind/163ListDownloader_NexT/issues",
    ]
    for i in info:
        p.script.append(Script(info = i, justify = "center"))
    p.script.append(Script(info = ''))
    command: list[Command] = []
    command.append(Command(func = exit_c, key = 0, info = 'Exit'))
    command.append(Command(func = get_detail, key = 1, info = 'Get Start!'))
    for i in command:
        p.script.append(Script(info = i.str_back(), justify = "left"))
    p.renderer()
    command_input = int(input(">> "))
    for i in command:
        if i.key == command_input:
            i.func()
