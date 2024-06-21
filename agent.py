# -*- coding: UTF-8 -*-
import random
import random
import execjs
agent = [
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
]

# 获取浏览器认证头
def get_user_agents():
    return random.choice(agent)
# 读取js
def djs(js):
    f = open(js, 'r', encoding='utf-8')
    jst = ''
    while True:
        readline = f.readline()
        if readline:
            jst += readline
        else:
            break
    return jst
def getjs():
    return djs('jsdm.js')

# 获取ptqrtoken
def ptqrtoken(qrsign):
    # 加载js
    execjs_execjs = execjs.compile(getjs())
    return execjs_execjs.call('hash33', qrsign)
# 获取UI
def guid():
    # 加载js
    execjs_execjs = execjs.compile(getjs())
    return execjs_execjs.call('guid')
# 获取g_tk
def get_g_tk(p_skey):
    # 加载js
    execjs_execjs = execjs.compile(getjs())
    return execjs_execjs.call('getToken', p_skey)
# 获取i
def S():
    # 加载js
    execjs_execjs = execjs.compile(getjs())
    return execjs_execjs.call('S')
# 获取key
def a():
    # 加载js
    execjs_execjs = execjs.compile(getjs())
    return execjs_execjs.call('a', 16)
