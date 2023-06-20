# -*- coding:utf-8 -*-
import re
import base64
import httpx


def P(m, t):
    p = 0
    for i in m[0]:
        p += ord(i)
    p = p * int(t[0])
    p += 111111
    return p


# -0x1 * 0x2317d + -0x1 * 0x1a622 + 0x589a6 * 0x1
# -0x1*0x2317d+-0x1*0x1a622+0x589a6*0x1

def r0():
    url = "http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125440/3876551/4858442/index.html"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    res = httpx.get(url=url, headers=headers)
    url_suffix = re.findall(".*var Q='(.*?)',.*", res.text, re.I)
    M = re.findall(".*M='(.*?)',.*", res.text, re.I)
    t = re.findall(".*t='(.*?)',.*", res.text, re.I)
    pp = P(M, t)
    b64_str = "WZWS_CONFIRM_PREFIX_LABEL" + str(pp)
    wzws_sessionid = re.findall(".*wzws_sessionid=(.*?);.*", res.headers['set-cookie'], re.I)
    wzws_cid = re.findall(".*wzws_cid=(.*?);.*", res.headers['set-cookie'], re.I)


    url_2 = "http://www.pbc.gov.cn" + url_suffix[0] + "?wzwschallenge=" + base64.b64encode(
        b64_str.encode("UTF-8")).decode("UTF-8")
    headers_2 = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Cookie": "wzws_sessionid=" + wzws_sessionid[0] + "; wzws_cid=" + wzws_cid[0],
        "Referer": "http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125440/3876551/4858442/index.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    res2 = httpx.get(url=url_2, headers=headers_2)
    wzws_cid_2 = re.findall(".*wzws_cid=(.*?);.*", res2.headers['set-cookie'], re.I)
    
    
    headers_3 = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Cookie": "wzws_sessionid=" + wzws_sessionid[0] + "; wzws_cid=" + wzws_cid_2[0],
        "Referer": "http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125440/3876551/4858442/index.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    res3 = httpx.get(url=url, headers=headers_3)
    print(res3.text)


if __name__ == '__main__':
    r0()

