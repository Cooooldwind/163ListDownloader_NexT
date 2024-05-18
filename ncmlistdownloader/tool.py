"""
ncmlistdownloader/tool.py
Core.Ver.2.0.0.240518a1
Copyright @CooooldWind_
Following GNU_AGPLV3+ License
"""

import os


def url_split(url=str()) -> str:
    """
    把id从url里面提取出来
    ----------
    参数:
    1. `url`: 需要转换的url
    """
    id_return = url.split("?id=")[-1].split("&")[0]
    return id_return
