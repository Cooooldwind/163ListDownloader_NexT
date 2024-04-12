'''
ncmlistdownloader/cmd/__init__.py
Core.Ver.1.0.0.240412a2
Author: CooooldWind_
P.S.: 实现几个页面，可以来回切换，对应运行函数。
'''

from ncmlistdownloader.cmd.module import *
from ncmlistdownloader.playlist import *
import multiprocessing
import time

def pl_run(pl: Playlist):
    pl.get_detail_info()

def main():
    def exit_c():
        return
    
    #get_detail
    def get_detail():

        #get_detail_waiting
        
        
        def get_detail_waiting(id_input):
            multiprocessing.freeze_support()
            pl = Playlist(id_input)
            p = Page()
            p.script = []
            p.title = "163ListDownloader CMD Ver - Playlist-get is runnning"
            p.width = 80
            info = [
                f"Getting the detail infomation from id: {id_input} ...",
                ""
            ]
            for i in info:
                p.script.append(Script(info = i, justify = "center"))
            p.renderer()
            pl.get_info()
            mp = multiprocessing.Process(target = pl_run, args = (pl,))
            print(mp.is_alive())
            mp.start()
            print(mp.is_alive())
            time.sleep(1)
            print(mp.is_alive())
            time.sleep(1)
            while mp.is_alive() == True and pl.done_sum() != pl.track_count:
                info = [
                    f"Getting the detail infomation from id: {id_input} ...",
                    f"Done: {pl.done_sum()} / {pl.track_count}",
                    "",
                ]
                p.script = []
                for i in info:
                    p.script.append(Script(info = i, justify = "center"))
                p.renderer()
                d = pl.done_sum()
            get_detail_succeed(pl)
            
        # get_detail_succeed
        def get_detail_succeed(pl: Playlist):
            p = Page()
            p.script = []
            p.title = "163ListDownloader CMD Ver - Playlist-get Succeed"
            p.width = 80
            info = [
                f"\"{pl.title}\" got, here's detail:",
                f"creator: {pl.creator} (id: {pl.creator_id})",
                f"total: {pl.track_count}",
                "",
            ]
            t_num = 0
            for i in pl.track:
                t_num += 1
                info.append(f"#{t_num}: {i.title} - {i.artist_str}")
            info.append("")
            for i in info:
                p.script.append(Script(info = i, justify = "left"))
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
        
        p_gd = Page()
        p_gd.script = []
        p_gd.title = "163ListDownloader CMD Ver - Get Start"
        p_gd.width = 80
        info = [
            "Press your playlist's id/url below.",
            "",
        ]
        for i in info:
            p_gd.script.append(Script(info = i, justify = "left"))
        p_gd.renderer()
        id_input = str(input(">> "))
        get_detail_waiting(id_input)
    
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
        "",
    ]
    for i in info:
        p.script.append(Script(info = i, justify = "center"))
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
