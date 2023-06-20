# -*- coding:utf-8 -*-
import time
import json
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs
import requests as hx

from TYC.img_ import *
from TYC.product_args import *

"""
https://www.tianyancha.com/
https://napi-huawei.tianyancha.com/validate/init?_=1685167907425
https://api.geevisit.com/gettype.php?gt=f5c10f395211c77e386566112c6abf21&callback=geetest_1685167908064
https://api.geevisit.com/get.php?gt=f5c10f395211c77e386566112c6abf21&challenge=875203811307b07c87754cd3d239c074&product=popup&offline=false&api_server=api.geevisit.com&protocol=https://&type=slide&path=/static/js/geetest.6.0.9.js&callback=geetest_1685167910503
https://api.geetest.com/ajax.php?gt=f5c10f395211c77e386566112c6abf21&challenge=875203811307b07c87754cd3d239c07444&w=nHwjAutqqWQ7Y0myx8)XxD5CbRVAaSSPN6dmGHiIclgw1HivZCwbXjamBoIwqZVSIUEPV8v9IAfAwwqt4iuAccQbOT39SAI8MIMJmAXmsGy1F4Z0xLpKDUAdtXtQcSvU(x1ZIABaD(LM4YkRoQX6UwrEEJ4r1WOjwvuXPNz6DBQ4jsg1WgWMe71SIYRDqpl5jC41XZ)vKkZ)FxrKBu6loLip8uQzCcp2)C3YO5A4AtM6mwJiQzaos7TGvsBfaajaVkDo2ai)GzPvBRRnKDoJ9XvgqHvDDsPeYs2FXYrGIFssVtf1lUOfKleuQoUQE1pSkJ0ysL2fQXpbf6O(MATcHdgEGWqIRW)WpqrO2CMQ8QI.4dcd19e822d2f67c09e0737e716409c8fbe3ceceb5787633a3d571947c339c2217639eb18348ddc45f77d45ca85e4725cf2ea3a1074a8024f4cf70712ea9cdb21b3666cb212574837b2cd750a6490f6fd60ce635b81dfdcf0c2996df959743f0ee6687f1bb1b3b2ec04042c4c9530bfc335c07fdcb2a416850b3a5b77af73af8&callback=geetest_1685168139065
https://napi-huawei.tianyancha.com/next/web/cdloginV2?_=1685168131656&mobile=13112341377&cdpassword=8e310df5da170452d5fe1bca11f1e5cc&loginway=PL&challenge=875203811307b07c87754cd3d239c07444&validate=5ccad666482cc7a37913a0b0b4301b12&seccode=5ccad666482cc7a37913a0b0b4301b12%7Cjordan

https://www.tianyancha.com/search?key=%E7%99%BE%E5%BA%A6
"""


def request_1():
    url = "https://www.tianyancha.com/"
    headers = {
        "Host": "www.tianyancha.com",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    }
    res = hx.get(url, headers=headers)
    args = res.headers['Set-Cookie'].split("; path=/, ")
    retval = {}
    for item in args:
        tmp = item.split("=")
        if tmp[0] == "TYCID":
            retval[tmp[0]] = tmp[1].split(";")[0]
            continue
        retval[tmp[0]] = tmp[1]
    return retval


def request_2(pre_args):
    url = "https://napi-huawei.tianyancha.com/validate/init?_=" + str(time.time_ns())[:-6]
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Host": "napi-huawei.tianyancha.com",
        "Origin": "https://www.tianyancha.com",
        "Pragma": "no-cache",
        "Referer": "https://www.tianyancha.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "X-TYCID": pre_args["TYCID"],
        "version": "TYC-Web"
    }
    res = hx.get(url, headers=headers)
    args = res.headers['Set-Cookie'].split("; path=/, ")
    retval = {}
    for item in args:
        tmp = item.split("=")
        if tmp[0] == "csrfToken":
            retval[tmp[0]] = tmp[1].split(";")[0]
            continue
        retval[tmp[0]] = tmp[1]
    retval.update({
        "challenge": res.json()['data'].split('"challenge":"')[1].split('"')[0],
        "gt": res.json()['data'].split('"gt":"')[1].split('"')[0],
    })
    return retval


def request_3(pre_args):
    t = str(time.time_ns())[:-6]
    url = f"https://api.geevisit.com/get.php?gt={pre_args['gt']}&challenge={pre_args['challenge']}&product=popup&offline=false&api_server=api.geevisit.com&protocol=https://&type=slide&path=/static/js/geetest.6.0.9.js&callback=geetest_" + t
    headers = {
        "Accept": "*/*",
        # "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Host": "api.geevisit.com",
        "Pragma": "no-cache",
        "Referer": "https://www.tianyancha.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    }
    res = hx.get(url, headers=headers)
    tmp = json.loads(res.text[res.text.find('(') + 1:-1])
    print(tmp)
    url_fullbg = tmp['fullbg']
    url_bg = tmp['bg']
    path_fullbg = './fullbg.png'
    path_bg = "./bg.png"
    require_3_1(url_fullbg, path_fullbg)
    require_3_1(url_bg, path_bg)
    path_new_fullbg = './new_fullbg.png'
    path_new_bg = './new_bg.png'
    img_restore(path_fullbg, path_new_fullbg)
    img_restore(path_bg, path_new_bg)
    point_x = img_ocr(path_new_bg, path_new_fullbg)['target'][0]
    move_data = my_args_slide_2(point_x)
    print(point_x, move_data)
    with open('./tyc.js', 'r', encoding='utf-8') as fs:
        my_move = execjs.compile(fs.read()).call('main', move_data)
    print(my_move)
    with open('./geetest_6_0_9.js', 'r', encoding='utf-8') as fs2:
        my_w = execjs.compile(fs2.read()).call('main', my_move, pre_args['gt'], pre_args['challenge'], 778, point_x,
                                               tmp['c'], tmp['s'])
    print(my_w)
    require_4(pre_args['gt'], pre_args['challenge'], my_w)


def require_3_1(url, path_img):
    url = "https://static.geetest.com/" + url
    headers = {
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Origin": "https://www.tianyancha.com",
        "pragma": "no-cache",
        "Referer": "https://www.tianyancha.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    }
    res = hx.get(url=url, headers=headers)
    with open(path_img, "wb") as f:
        f.write(res.content)


def require_4(gt, ch, w):
    url = f"https://api.geetest.com/ajax.php?gt={gt}&challenge={ch}&w={w}&callback=geetest_" + str(time.time_ns())[:-6]
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Host": "api.geevisit.com",
        "Pragma": "no-cache",
        "Referer": "https://www.tianyancha.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    }
    res = hx.get(url, headers=headers)
    print(res.text)


if __name__ == '__main__':
    # a = request_1()
    # print(a)
    # b = request_2(a)
    # print(b)
    # request_3(b)
    gt = "f5c10f395211c77e386566112c6abf21"
    ch = "6187d3549bc64a5d4d7625e61e2734d7fl"
    point_x = 141
    c = [12, 58, 98, 36, 43, 95, 62, 15, 12]
    s = "4f527570"

    # move_data = my_args_slide_2(point_x)
    # print(point_x, move_data)
    move_data=[[-22,-17,0],[0,0,0],[1,0,95],[2,0,102],[2,0,117],[3,0,125],[5,0,132],[6,0,148],[6,0,156],[7,0,170],[8,0,178],[9,0,223],[10,0,260],[10,0,343],[11,0,358],[12,0,364],[13,-1,372],[14,-1,380],[15,-1,388],[16,-1,395],[18,-1,403],[19,-1,411],[26,-1,418],[28,-2,425],[38,-2,431],[42,-2,441],[51,-2,446],[58,-3,455],[63,-3,462],[72,-3,470],[75,-3,478],[78,-3,486],[81,-3,493],[82,-3,500],[83,-2,508],[84,-2,522],[85,-2,621],[86,-2,636],[88,-2,642],[89,-2,650],[91,-2,657],[93,-2,665],[96,-2,673],[97,-2,681],[100,-2,688],[102,-2,695],[102,-2,702],[105,-2,711],[106,-2,718],[107,-2,725],[110,-2,732],[110,-2,740],[111,-2,747],[114,-2,756],[115,-2,762],[117,-2,771],[119,-2,777],[120,-2,786],[121,-2,792],[122,-2,800],[122,-2,807],[123,-2,822],[124,-2,836],[125,-2,846],[126,-2,861],[126,-2,876],[127,-2,883],[128,-2,912],[129,-2,920],[130,-2,936],[133,-3,942],[134,-3,950],[134,-3,957],[136,-3,965],[137,-4,973],[138,-4,980],[140,-4,987],[141,-4,995],[142,-4,1002],[142,-4,1016],[143,-4,1025],[144,-4,1048],[145,-4,1055],[146,-4,1070],[146,-4,1085],[146,-4,1332],[145,-4,1386],[144,-4,1498],[143,-4,1536],[142,-4,1641],[142,-4,1724],[141,-4,1737],[141,-4,2742]]
    with open('./tyc.js', 'r', encoding='utf-8') as fs:
        my_move = execjs.compile(fs.read()).call('main', move_data)
    print(my_move)
    with open('./geetest_6_0_9.js', 'r', encoding='utf-8') as fs2:
        my_w = execjs.compile(fs2.read()).call('main', my_move, gt, ch, 778, point_x,
                                               c, s)
    print(my_w)
    require_4(gt, ch, my_w)
