import time
from ncmlistdownloader.common.global_args import *

def format_output(raw: str, type: str) -> str:
    time_now_formated = time.strftime('%H:%M:%S', time.localtime())
    return_str = f"[{type}][{time_now_formated}] {raw}"
    if type == "Input":
        return_str += ">> "
    return return_str

def input_func(notice: str):
    return input(format_output(raw = notice, type = "Input"))

def main():
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
    choice = int(input_func("Press the number of the function"))

        

if __name__ == "__main__":
    main()
    