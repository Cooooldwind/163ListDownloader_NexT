'''
ncmlistdownloader/cmd/__init__.py
Core.Ver.1.0.1.240422a1
Author: CooooldWind_
'''
from ncmlistdownloader.song import *
from ncmlistdownloader.playlist import *
from ncmlistdownloader.common.global_args import *
from ncmlistdownloader.cmd.common import *
from ncmlistdownloader.cmd.json_io import *
from ncmlistdownloader.cmd.find_from_id import *

cookies = None

def main():
    global cookies
    for i in CMD_START_WORDS:
        print(format_output(raw = i, type = "Info"))
    cookies = {'MUSIC_U': input_func("Please input your cookies (ONLY MUSIC_U) (if you don't have, just press enter) ")}
    if cookies["MUSIC_U"] == '':
        cookies = None
    while True:
        FUNC_CHOICE = [
            "Find Playlist/Song by ID/Url",
            "Load from json file",
            "Search",
            "Exit",
        ]
        for i in range(0, len(FUNC_CHOICE)):
            if not(i == 2 and cookies == None): print(format_output(f"[{i + 1}] -> {FUNC_CHOICE[i]}", type = "Info"))
            else: print(format_output(f"[X] -> {FUNC_CHOICE[i]}", type = "Info"))
        choice = None
        while True:    
            choice = int(input_func("Press the number of the function "))
            if choice >= 1 and choice <= len(FUNC_CHOICE):
                break
            else:
                print(format_output("Value Error!", type = "Error"))
        if choice == 1:
            find_from_id(cookies = cookies)
        if choice == 4:
            print(format_output(raw = "Byebye~", type = "Info"))
            break

if __name__ == "__main__":
    main()
    