'''
ncmlistdownloader/cmd/module.py
Core.Ver.1.0.0.240411a1
Author: CooooldWind_
P.S.: 实现几个页面，可以来回切换，对应运行函数。
'''

import os

class Script():
    def __init__(self, justify: str = "left", info: str = 'An Script class in Page class.'):
        self.justify = justify
        self.info = info
    def __str__(self) -> str:
        return self.info

class Command():
    def __init__(self, func, key: int, info = 'A Command'):
        self.func = func
        self.key = key
        self.info = info
    def str_back(self) -> str:
        return f'[{self.key}] -> {self.info}'

class Page():
    def __init__(self):
        self.title: str = 'Page'
        self.script: list[Script]
        self.width = 40
    def renderer(self):
        os.system("cls")
        print(self.title.ljust(self.width))
        for i in range(self.width):
            print('-', end = '')
        print()
        for i in self.script:
            if i.justify == "right": print(i.info.rjust(self.width))
            elif i.justify == "center": print(i.info.center(self.width))
            else: print(i.info.ljust(self.width))