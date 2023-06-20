# -*- coding:utf-8 -*-

import re

import requests
import json

# execjs 乱码问题
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs

url = "http://www.nmpa.gov.cn/"

headers = {
    "Host": "www.nmpa.gov.cn",
    "Pragma": "no-cache",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

res = requests.get(url,headers=headers)
if res.status_code == 202:
    print(res.headers['set-cookie'])
    parms = {k.split('=')[0]: k.split('=')[1] for k in [i.replace("Max-Age=1800, ", "").replace(",", "").strip() for i in
                                                        [item for item in res.headers['set-cookie'].split(';') if
                                                         item.find("neCYtZEjo8GmO") != -1 or item.find(
                                                             "acw_tc") != -1]]}
    # print(parms)

    with open("./datas/index.html", "w", encoding="utf-8") as fs:
        fs.write(res.text)
    content = re.findall('<meta content=(".*?")>', res.text, re.I)[0]
    src = re.findall('charset="iso-8859-1" src="(.*?)"', res.text, re.I)[0]
    func = re.findall('r="m">(.*?)</script>', res.text, re.I)[0]
    headers2={
        "Cookie": "acw_tc="+parms['acw_tc']+ "; "+"neCYtZEjo8GmO="+parms['neCYtZEjo8GmO'],
        "Accept": "*/*",
        "Host": "www.nmpa.gov.cn",
        "Pragma": "no-cache",
        "Referer": "https://www.nmpa.gov.cn/"
    }
    print("src ->",src)
    # print(headers2)
    res2 = requests.get('https://www.nmpa.gov.cn' + src,headers=headers2)
    with open('./env.js', 'r', encoding='utf-8') as fs:
        env = fs.read()
    if res2.status_code == 200:
        with open("./datas/test.js", "w", encoding="utf-8") as fs:
            # fs.write("var cookie_1=" + repr(res.headers['set-cookie']))
            fs.write("var cookie_1=" + repr("acw_tc="+parms['acw_tc']+ "; "+"neCYtZEjo8GmO="+parms['neCYtZEjo8GmO']))
            fs.write(';;;')
            fs.write("var content_1=" + content)
            fs.write(';;;')
            fs.write(env)
            fs.write(';;;')
            fs.write(res2.text)
            fs.write(';;;')
            fs.write(func)
            fs.write(';;;')
            fs.write("""
                function encrypt_() { 
                        return window.eval_1;
                }
            """)
            fs.write(';;;')
    with open('./datas/test.js', 'r', encoding='utf-8') as fs:
        cookiejs = execjs.compile(fs.read()).call('encrypt_')

    with open("./datas/test.js", "a+", encoding="utf-8") as fs:
        fs.write("window.$_ts = window.navigator.$_ts;")
        fs.write(";;;")
        fs.write("/*cookiejs-start*/")
        fs.write(cookiejs)
        fs.write(';;;')
        fs.write("""
                var localStorage_2= {};
                for(var kkk in window.localStorage){
                    if (kkk =="getItem" || kkk=="setItem"||kkk=="removeItem") continue;
                    localStorage_2[kkk]=window.localStorage[kkk];
                }
            """)
        fs.write(';;;')
        fs.write("""
                function encrypt_2() { 
                        return {"cookie":window.document.cookie,"localStorage_2":localStorage_2};
                }
            """)
        fs.write(';;;')
    with open('./datas/test.js', 'r', encoding='utf-8') as fs:
        cookiejs_2 = execjs.compile(fs.read()).call('encrypt_2')
    # print(cookiejs_2)
    headers3={
        "Cookie": "acw_tc="+parms['acw_tc']+ "; "+"neCYtZEjo8GmO="+parms['neCYtZEjo8GmO']+"; "+cookiejs_2['cookie'].split(";")[0],
        "Accept": "*/*",
        "Host": "www.nmpa.gov.cn",
        "Pragma": "no-cache",
        "Referer": "https://www.nmpa.gov.cn/"
    }
    print(headers3)
    res3=requests.get("https://www.nmpa.gov.cn/",headers=headers3)
    print(res3.status_code)
    print(res3.headers)
    # print(res3.headers)
    if res3.status_code==202:
        with open("./datas/index_2.html", "w", encoding="utf-8") as fs:
            fs.write(res3.text)
        content_2 = re.findall('<meta content=(".*?")>', res3.text, re.I)[0]
        src_2 = re.findall('charset="iso-8859-1" src="(.*?)"', res3.text, re.I)[0]
        func_2 = re.findall('r="m">(.*?)</script>', res3.text, re.I)[0]
        print("src2->",src_2)

        res4 = requests.get('https://www.nmpa.gov.cn' + src_2,headers={
            "Cookie": "acw_tc="+parms['acw_tc']+ "; "+"neCYtZEjo8GmO="+parms['neCYtZEjo8GmO']+"; "+cookiejs_2['cookie'].split(";")[0],
            "Accept": "*/*",
            "Host": "www.nmpa.gov.cn",
            "Pragma": "no-cache",
            "Referer": "https://www.nmpa.gov.cn/"
    })
        with open('./env2.js', 'r', encoding='utf-8') as fs:
            env2 = fs.read()
        if res4.status_code == 200:
            with open("./datas/test_2.js", "w", encoding="utf-8") as fs:
                fs.write("var cookie_1=" + repr(res3.request.headers['Cookie']))
                fs.write(';;;')
                fs.write("var content_1=" + content_2)
                fs.write(';;;')
                fs.write(env2)
                fs.write(';;;')
                fs.write(res4.text)
                fs.write(';;;')
                fs.write(func_2)
                fs.write(';;;')
                fs.write("""
                    function encrypt_() { 
                            return window.eval_1;
                    }
                """)
                fs.write(';;;')
        with open('./datas/test_2.js', 'r', encoding='utf-8') as fs:
            cookiejs_3 = execjs.compile(fs.read()).call('encrypt_')

        with open("./datas/test_2.js", "a+", encoding="utf-8") as fs:
            fs.write(f'window.$_ts = window.navigator.$_ts;var localStorage_3={cookiejs_2["localStorage_2"]};')
            fs.write("for(var k_2 in localStorage_3){window.localStorage[k_2]=localStorage_3[k_2];}")     
            fs.write(";;;")
            fs.write("/*cookiejs-start*/")
            fs.write(cookiejs)
            fs.write(';;;')
            fs.write("""
                    var localStorage_2= {};
                    for(var kkk in window.localStorage){
                        if (kkk =="getItem" || kkk=="setItem"||kkk=="removeItem") continue;
                        localStorage_2[kkk]=window.localStorage[kkk];
                    }
                """)
            fs.write(';;;')
            fs.write("""
                    function encrypt_2() { 
                            return {"cookie":window.document.cookie,"localStorage_2":localStorage_2};
                    }
                """)
            fs.write(';;;')
        with open('./datas/test.js', 'r', encoding='utf-8') as fs:
            cookiejs_4 = execjs.compile(fs.read()).call('encrypt_2')
        # print(cookiejs_2)
        headers4={
            "Cookie": "acw_tc="+parms['acw_tc']+ "; "+"neCYtZEjo8GmO="+parms['neCYtZEjo8GmO']+"; "+cookiejs_4['cookie'].split(";")[0],
            "Accept": "*/*",
            "Host": "www.nmpa.gov.cn",
            "Pragma": "no-cache",
            "Referer": "https://www.nmpa.gov.cn/"
        }
        print(headers4)
        res5=requests.get("https://www.nmpa.gov.cn/",headers=headers4)
        print(res5.status_code)

        with open("./datas/index_3.html", "w", encoding="utf-8") as fs:
            fs.write(res5.text)
else:
    print(res.status_code)
    print(res.text)
