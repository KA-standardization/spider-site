# -*- coding:utf-8 -*-
import time
import json
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs
import requests as hx

from myDemo.demo.img_ import img_restore, img_ocr
from myDemo.demo.product_args import my_args_slide, my_args_slide_2, my_args_slide_3


def time_str():
    t = str(time.time()).split('.')
    return t[0] + t[1][:3]


def request_1(ua):
    url = "https://www.geetest.com/demo/gt/register-slide"
    params = {
        "t": time_str()
    }
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": "https://www.geetest.com/demo/slide-float.html",
        "user-agent": ua,
        "x-requested-with": "XMLHttpRequest"
    }
    r1 = hx.get(url=url, params=params, headers=headers).json()
    return r1


def request_2(ua, gt):
    url = "https://apiv6.geetest.com/gettype.php"
    params = {
        "gt": gt,
        "callback": "geetest_" + time_str()
    }
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Host": "apiv6.geetest.com",
        "Pragma": "no-cache",
        "Referer": "https://www.geetest.com/",
        "user-agent": ua
    }
    r2 = hx.get(url=url, params=params, headers=headers)
    return (r2.text[22:-1], r2.headers['set-cookie'].split(';')[0])


def require_3(ua, gt, challenge, w, cookie):
    url = "https://apiv6.geetest.com/get.php"
    params = {
        "gt": gt,
        "challenge": challenge,
        "lang": "zh-cn",
        "pt": 0,
        "client_type": "web",
        "w": w,
        "callback": "geetest_" + time_str()
    }
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": cookie,
        "Host": "apiv6.geetest.com",
        "Pragma": "no-cache",
        "Referer": "https://www.geetest.com/",
        "user-agent": ua
    }
    r3 = hx.get(url=url, params=params, headers=headers)
    return json.loads(r3.text[22:-1].replace("true", '"true"').replace("false", '"false"'))


def require_4(ua, gt, challenge, w, cookie):
    url = "https://api.geetest.com/ajax.php"
    params = {
        "gt": gt,
        "challenge": challenge,
        "lang": "zh-cn",
        "pt": 0,
        "client_type": "web",
        "w": w,
        "callback": "geetest_" + time_str()
    }
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": cookie,
        "Host": "api.geetest.com",
        "Pragma": "no-cache",
        "Referer": "https://www.geetest.com/",
        "User-Agent": ua
    }
    r4 = hx.get(url=url, params=params, headers=headers)
    res = r4.text[22:-1].replace("true", '"true"').replace("false", '"false"')
    return r4.headers['set-cookie'].split(';')[0]


def require_5(ua, gt, challenge, cookie):
    url = "https://api.geetest.com/get.php"
    params = {
        'is_next': "true",
        'type': 'slide3',
        "gt": gt,
        "challenge": challenge,
        "lang": "zh-cn",
        'https': "true",
        'protocol': 'https: //',
        'offline': "false",
        'product': 'embed',
        'api_server': 'api.geetest.com',
        'isPC': "true",
        'autoReset': "true",
        'width': '100 %',
        "callback": "geetest_" + time_str()
    }
    headers = {
        "Accept": "*/*",
        # "Accept-Encoding": "gzip, deflate, br",
        # "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": cookie,
        "Host": "api.geetest.com",
        "Pragma": "no-cache",
        "Referer": "https://www.geetest.com/",
        "User-Agent": ua
    }
    r5 = hx.get(url=url, params=params, headers=headers)
    return json.loads(r5.text[22:-1].replace("true", '"true"').replace("false", '"false"'))


def require_6(ua, url, path_img):
    url = "https://static.geetest.com/" + url
    headers = {
        "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "origin": "https://www.geetest.com",
        "pragma": "no-cache",
        "referer": "https://www.geetest.com/",
        "user-agent": ua
    }
    r6 = hx.get(url=url, headers=headers)
    with open(path_img, "wb") as f3:
        f3.write(r6.content)


if __name__ == '__main__':
    user_a = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    res_1 = request_1(user_a)
    myArg = my_args_slide(res_1['gt'], res_1['challenge'], user_a)
    res_2 = request_2(user_a, myArg[0])
    with open('./jsLocal/jy9_1_3_.js', 'r', encoding='utf-8') as fs:
        my_ww = execjs.compile(fs.read()).call('main', myArg[2])
        my_w = my_ww.split("!!!!")
    res_3 = require_3(user_a, myArg[0], myArg[1], my_w[0], res_2[1])
    with open('./jsLocal/jy9_1_3_.js', 'r', encoding='utf-8') as fs_2:
        my_w_2 = execjs.compile(fs_2.read()).call('main2', myArg[3], res_3["data"]['c'], res_3["data"]['s'], myArg[4],
                                                  myArg[5], myArg[6], myArg[7], myArg[8], my_w[1])
    res_4 = require_4(user_a, myArg[0], myArg[1], my_w_2, res_2[1])
    res_5 = require_5(user_a, myArg[0], myArg[1], res_2[1] + "; " + res_4)
    print(res_5)
    img_path_bg = "./a.png"
    path_bg = './a_.png'
    require_6(user_a, res_5['bg'].replace(".jpg", ".webp"), img_path_bg)
    require_6(user_a, "pictures/gt/7bfaaa72b/bg/b0c61989d.webp".replace(".jpg", ".webp"), img_path_bg)
    img_restore(img_path_bg, path_bg)
    img_path_fullbg = "./b.png"
    path_fullbg = './b_.png'
    require_6(user_a, res_5['fullbg'].replace(".jpg", ".webp"), img_path_fullbg)
    require_6(user_a, "pictures/gt/7bfaaa72b/7bfaaa72b.webp".replace(".jpg", ".webp"), img_path_fullbg)
    img_restore(img_path_fullbg, path_fullbg)

    point_x = img_ocr(path_bg, path_fullbg)['target'][0]

    move_data = my_args_slide_2(point_x)
    print(point_x, move_data)
    # move_data = my_args_slide_3(point_x)
    # print(point_x, move_data)
    # c = res_5['c']
    # s = res_5['s']
