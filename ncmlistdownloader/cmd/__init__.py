'''
ncmlistdownloader/cmd/__init__.py
Core.Ver.1.0.0.240416a1
Author: CooooldWind_
'''
import time
from ncmlistdownloader.song import *
from ncmlistdownloader.playlist import *
from ncmlistdownloader.common.global_args import *

cookies = None

def format_output(raw: str, type: str) -> str:
    time_now_formated = time.strftime('%H:%M:%S', time.localtime())
    return_str = f"[{type}][{time_now_formated}] {raw}"
    if type == "Input":
        return_str += ">> "
    return return_str

def input_func(notice: str):
    return input(format_output(raw = notice, type = "Input"))

def find_from_id():
    global cookies
    FUNC_CHOICE = [
        "song",
        "playlist"
    ]
    for i in range(0, len(FUNC_CHOICE)):
        print(format_output(f"[{i + 1}] -> {FUNC_CHOICE[i]}", type = "Info"))
    choice = None
    while True:
        choice = int(input_func("Press the number of the function "))
        if choice != 1 and choice != 2:
            print(format_output("Value Error!", type = "Error"))
        else: break
    now = None
    id = str(input_func("Press the id/Url "))
    if choice == 1:
        now = Song(id)
        now.get_info()
    elif choice == 2:
        now = Playlist(id)
        if now.auto_get_info(cookies = cookies) == -1:
            print(format_output("You don't have the currect cookies to get the info of this Playlist.", type = "Error"))
        


def main():
    global cookies
    for i in CMD_START_WORDS:
        print(format_output(raw = i, type = "Info"))
    cookies = {'MUSIC_U': input_func("Please input your cookies (ONLY MUSIC_U) (if you don't have, just press enter) ")}
    if cookies["MUSIC_U"] == '':
        cookies = None
    FUNC_CHOICE = [
        "Find Playlist/Song by ID/Url",
        "Load from json file",
        "Search",
    ]
    for i in range(0, len(FUNC_CHOICE)):
        if not(i == 2 and cookies == None): print(format_output(f"[{i + 1}] -> {FUNC_CHOICE[i]}", type = "Info"))
        else: print(format_output(f"[X] -> {FUNC_CHOICE[i]}", type = "Info"))
    choice = None
    while True:    
        choice = int(input_func("Press the number of the function "))
        if choice >= 1 and choice <= len(FUNC_CHOICE):
            break
    if choice == 1:
        find_from_id()

if __name__ == "__main__":
    main()
    