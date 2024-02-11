import requests
import pprint
'''
tmp = requests.post(
    url = "http://api.tunefree.fun/ncm/song/",
    data = {
        'id': '2043976339',
        'level': 'exhigh'
    }
).json()
'''
tmp = requests.get(
    url = "http://api.tunefree.fun/ncm/song/?id=2043976339&level=hires",
).json()
pprint.pprint(tmp)