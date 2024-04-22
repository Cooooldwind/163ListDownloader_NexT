'''
ncmlistdownloader/cmd/find_from_id.py
Core.Ver.1.0.1.240422a1
Author: CooooldWind_
'''

from ncmlistdownloader.song import *
from ncmlistdownloader.playlist import *
from ncmlistdownloader.common.global_args import *
from ncmlistdownloader.cmd.common import *
from ncmlistdownloader.cmd.json_io import *
from ncmlistdownloader.cmd import *

def find_from_id(cookies):
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
        print(format_output(f"Song: {now.title} - {now.artist_str}", type = "Info"))
    elif choice == 2:
        now = Playlist(id)
        if now.get_info(cookies = cookies) == -1:
            print(format_output("You don't have the currect cookies to get the info of this Playlist.", type = "Error"))
        now.multiprocessing_get_detail()
        wait_time = 0
        while now.done_sum() != now.track_count:
            count = now.done_sum()
            wait_time += 1
            least = -1
            if count != 0:
                least = int(wait_time / count * (now.track_count - count))
            print(format_output(f"Done: {count}/{now.track_count}, still need: {least} seconds", type = "Info"))
            time.sleep(1)
        for i in range(0, len(now.track)):
            j = now.track[i]
            print(format_output(f"Song #{i + 1}: {j.title} - {j.artist_str}", type = "Info"))
    while True:
        FUNC_CHOICE = [
            "Save to a json file",
            "Search something else",
            "Exit to the main page",
        ]
        for i in range(0, len(FUNC_CHOICE)):
            print(format_output(f"[{i + 1}] -> {FUNC_CHOICE[i]}", type = "Info"))
        while True:    
            choice = int(input_func("Press the number of the function "))
            if choice >= 1 and choice <= len(FUNC_CHOICE):
                break
        if choice == 1:
            json_save_list(pl = now)
        if choice == 2:
            find_from_id()
        if choice == 3:
            break