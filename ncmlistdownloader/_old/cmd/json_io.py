"""
ncmlistdownloader/cmd/json_io.py
Core.Ver.1.0.5.240429
Author: CooooldWind_
"""

from ncmlistdownloader.song import *
from ncmlistdownloader.playlist import *
from ncmlistdownloader.cmd.common import *
from ncmlistdownloader.cmd.download import *

def json_save_list(pl: Playlist):
    path = str(input_func(notice = "Input the file's save location"))
    d = {
        "type": "downloading_list_ncmld",
        "global_config": GLOBAL_CONFIG_MODEL,
        "track": [],
    }
    t = []
    for i in pl.track:
        t.append({
            "type": "song",
            "info": {
                "title": i.title,
                "artist": i.artist,
                "album": i.album,
                "id": i.id,
                "pic_url": i.url_info["album_pic"]
            },
            "global": True,
            "downloading_config": GLOBAL_CONFIG_MODEL,
        })
    d["track"] = t
    if path[-5:] != ".json":
        path += "ncmld_saved.json"
    with open(path, "w+", encoding = "utf-8") as file:
        json.dump(d, file, ensure_ascii = False, sort_keys = True)
    print(format_output("Saved!", type = "Info"))

def json_load(path: str):
    with open(path, "r+", encoding = "utf-8") as file:
        d = json.load(file)
    for i in range(len(d["track"])):
        now = d["track"][i]
        print(format_output(type = "Info", raw = f"Song #{i}:"))
        print(format_output(type = "Info", raw = f"Title: {now["info"]["title"]}"))
        print(format_output(type = "Info", raw = f"Artists: {now["info"]["artist"]}"))
        # print(format_output(type = "Info", raw = f""))
    download(d)
