import requests
from lxml import etree
from fontTools.ttLib import TTFont
import json


# source /Users/wangyu/Jagder/envs/env_python3.9/bin/activate
font = requests.get(
    "https://www.shixiseng.com/interns/iconfonts/file?rand=0.39654030623663883")
with open('my.tff', 'wb') as f:
    f.write(font.content)

font = TTFont('./my.tff')
font.saveXML('./my.xml')
tmp_dict = dict()

for k, v in font['cmap'].getBestCmap().items():
    # tmp_dict["$#"+hex(k)[1:]]=v.replace('uni',R'\u')
    if v == 'x':
        tmp_dict[hex(k)[2:]] = R'\u78'
    else:
        tmp_dict[hex(k)[2:]] = v.replace('uni', R'\u')


print(tmp_dict)

res = requests.get(
    url="https://www.shixiseng.com/interns",
    params={
        "keyword": "c",
        "city": "全国",
        "type": "intern"
    },
    headers={
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
)
html = etree.HTML(res.text)
a = html.xpath('//div[@style="display:;"]//a//text()')
# print(a)


def code_(s):
    str_ = ""
    for ch in s:
        ch_in = ch.encode('unicode_escape')
        key = ""
        for byte_ in ch_in[2:]:
            key += chr(byte_)
        val = tmp_dict.get(key, None)
        if val != None:
            val2 = val.encode('unicode_escape')[3:]
            val2_l = len(val2)
            if val2_l != 4:
                tmp_val = "\\u"
                for _ in range(4-val2_l):
                    tmp_val += "0"
                for val3 in val2:
                    tmp_val += chr(val3)
                str_ += tmp_val.encode().decode('unicode_escape')
            else:
                str_ += val.encode().decode('unicode_escape')
        else:
            str_ += ch
    print(str_)


for item in a:
    if item.strip():
        code_(item)
