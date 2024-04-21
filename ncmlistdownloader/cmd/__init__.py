'''
ncmlistdownloader/cmd/__init__.py
Core.Ver.1.0.1.240421a1
Author: CooooldWind_
'''
import time
from ncmlistdownloader.song import *
from ncmlistdownloader.playlist import *
from ncmlistdownloader.common.global_args import *

cookies = None

GLOBAL_CONFIG_MODEL = {
    'song_download': True,
    'cover_download': True,
    'lyric_download': True,
    'attribute_write': True,
    'cover_write': True,
    'lyric_write': True,
}

def format_output(raw: str, type: str) -> str:
    time_now_formated = time.strftime('%H:%M:%S', time.localtime())
    return_str = f"[{type}][{time_now_formated}] {raw}"
    if type == "Input":
        return_str += ">> "
    return return_str

def input_func(notice: str):
    return input(format_output(raw = notice, type = "Input"))

def json_save_list(pl: Playlist):
    path = str(input_func(notice = "Input the file's page"))
    d = {
        'type': 'downloading_list',
        'global_config': GLOBAL_CONFIG_MODEL,
        'track': [],
    }
    t = []
    for i in pl.track:
        t.append({
            'type': 'song',
            'info': {
                'title': i.title,
                'artist': i.artist,
                'album': i.album,
                'id': i.id,
            },
            'global': True,
            'downloading_config': GLOBAL_CONFIG_MODEL,
        })
    d['track'] = t
    with open(path, 'w+', encoding = 'utf-8') as file:
        json.dump(d, file, ensure_ascii = False, sort_keys = True)
    print(format_output("Saved!", type = "Info"))

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
            find_from_id()
        if choice == 4:
            print(format_output(raw = "Byebye~", type = "Info"))
            break

if __name__ == "__main__":
    main()
    