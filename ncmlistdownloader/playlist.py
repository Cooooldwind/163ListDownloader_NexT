"""
ncmlistdownloader/playlist.py
Core.Ver.2.0.0.240731b1
Copyright @CooooldWind_
Following GNU_AGPLV3+ License
"""

from class163 import Playlist as PlaylistFatherClass
import threading

class Playlist(PlaylistFatherClass):
    def __init__(self, id: int | str):
        PlaylistFatherClass.__init__(self, id)
    def multi_get(self, thread_sum: int = 8) -> dict:
        self.get(detail=False, session=self.encode_session)
        thread_list: list[threading.Thread] = []
        for tmp in self.track:
            thread_list.append(threading.Thread(target=tmp.get, kwargs={mode='d'}))
        for tmp in thread_list:
            with threading.Semaphore(thread_sum):
                tmp.start()