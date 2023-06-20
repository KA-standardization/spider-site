# -*- coding:utf-8 -*-
import time
import copy
import random


def time_str():
    t = str(time.time()).split('.')
    return t[0] + t[1][:3]


def my_args(gt, ch, ua):
    html_len = "7436"
    text_len = "6148"
    div = "12"
    inputs = "2"
    labels = "3"
    scripts = "5"
    hardwareConcurrency = "12"
    canvas = "3515ba42d4414f09872d5667a81df514"
    font = "Arial,ArialBlack,ArialNarrow,BookAntiqua,BookmanOldStyle,Calibri,Cambria,CambriaMath,Century,CenturyGothic,CenturySchoolbook,ComicSansMS,Consolas,Courier,CourierNew,Garamond,Georgia,Helvetica,Impact,LucidaBright,LucidaCalligraphy,LucidaConsole,LucidaFax,LucidaHandwriting,LucidaSans,LucidaSansTypewriter,LucidaSansUnicode,MicrosoftSansSerif,MonotypeCorsiva,MSGothic,MSPGothic,MSReferenceSansSerif,MSSansSerif,MSSerif,PalatinoLinotype,SegoePrint,SegoeScript,SegoeUI,SegoeUILight,SegoeUISemibold,SegoeUISymbol,Tahoma,Times,TimesNewRoman,TrebuchetMS,Verdana,Wingdings,Wingdings2,Wingdings3"
    plugins = "internal-pdf-viewer,internal-pdf-viewer,internal-pdf-viewer,internal-pdf-viewer,internal-pdf-viewer"

    info_browser = text_len + \
                   '!!' + \
                   html_len + \
                   '!!CSS1Compat!!1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!' + \
                   inputs + \
                   '!!' + \
                   labels + \
                   '!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!1!!-1!!-1!!-1!!0!!0!!0!!0!!1536!!730!!1536!!832!!zh-CN!!zh-CN!!-1!!1.25!!24!!' + \
                   ua + \
                   '!!1!!1!!1536!!864!!1536!!832!!1!!1!!1!!-1!!Win32!!0!!-8!!' + \
                   canvas + \
                   '!!0!!' + \
                   plugins + \
                   '!!0!!-1!!0!!' + \
                   div + \
                   '!!' + \
                   font + \
                   '!!' + \
                   time_str() + \
                   '!!-1!!-1!!-1!!' + \
                   hardwareConcurrency + \
                   '!!-1!!-1!!-1!!' + \
                   scripts + \
                   '!!-1!!-1"'

    data = '{"gt":"' + \
           gt + \
           '","challenge":"' + \
           ch + \
           '","offline":false,"new_captcha":true,"product":"float","width":"300px","https":true,"api_server":"' + \
           'apiv6.geetest.com' + \
           '","protocol":"https://","type":"fullpage","static_servers":["' + \
           'static.geetest.com/' + \
           '","' + \
           'dn-staticdown.qbox.me/' + \
           '"],"beeline":"' + \
           '/static/js/beeline.1.0.1.js' + \
           '","voice":"' + \
           '/static/js/voice.1.2.2.js' + \
           '","click":"' + \
           '/static/js/click.3.0.7.js' + \
           '","fullpage":"' + \
           '/static/js/fullpage.9.1.3.js' + \
           '","slide":"' + \
           '/static/js/slide.7.8.9.js' + \
           '","geetest":"' + \
           '/static/js/geetest.6.0.9.js' + \
           '","aspect_radio":{"slide":103,"click":128,"voice":128,"beeline":50' + \
           '},"cc":12,"ww":true,"i":"' + \
           info_browser + \
           '}'
    return (info_browser, data)


def my_args_slide(gt, ch, ua):
    my_args_ = my_args(gt, ch, ua)
    trajectory_base_1 = [
        ["move", 346, 363, 1678941407365, "pointermove"], ["move", 349, 362, 1678941407372, "pointermove"],
        ["move", 351, 360, 1678941407379, "pointermove"], ["move", 353, 359, 1678941407387, "pointermove"],
        ["move", 354, 358, 1678941407394, "pointermove"], ["move", 356, 357, 1678941407401, "pointermove"],
        ["move", 359, 355, 1678941407409, "pointermove"], ["move", 363, 353, 1678941407416, "pointermove"],
        ["move", 372, 348, 1678941407424, "pointermove"], ["move", 385, 345, 1678941407432, "pointermove"],
        ["move", 413, 336, 1678941407439, "pointermove"], ["move", 412, 336, 1678941407440, "pointermove"],
        ["move", 449, 328, 1678941407446, "pointermove"], ["move", 448, 328, 1678941407447, "pointermove"],
        ["move", 476, 323, 1678941407454, "pointermove"], ["move", 508, 316, 1678941407461, "pointermove"],
        ["move", 537, 311, 1678941407470, "pointermove"], ["move", 564, 306, 1678941407476, "pointermove"],
        ["move", 592, 299, 1678941407485, "pointermove"], ["move", 600, 298, 1678941407491, "pointermove"],
        ["move", 600, 297, 1678941407492, "pointermove"], ["move", 610, 295, 1678941407501, "pointermove"],
        ["move", 614, 294, 1678941407507, "pointermove"], ["move", 616, 294, 1678941407514, "pointermove"],
        ["move", 615, 294, 1678941407559, "pointermove"], ["move", 613, 294, 1678941407566, "pointermove"],
        ["move", 611, 294, 1678941407574, "pointermove"], ["move", 609, 294, 1678941407581, "pointermove"],
        ["move", 608, 293, 1678941407582, "pointermove"], ["move", 606, 294, 1678941407596, "pointermove"],
        ["move", 606, 293, 1678941407597, "pointermove"], ["move", 605, 295, 1678941407605, "pointermove"],
        ["move", 604, 295, 1678941407611, "pointermove"], ["move", 602, 297, 1678941407620, "pointermove"],
        ["move", 601, 299, 1678941407635, "pointermove"], ["move", 600, 301, 1678941407642, "pointermove"],
        ["move", 599, 303, 1678941407649, "pointermove"], ["move", 598, 306, 1678941407656, "pointermove"],
        ["move", 598, 307, 1678941407665, "pointermove"], ["move", 598, 310, 1678941407671, "pointermove"],
        ["move", 597, 313, 1678941407680, "pointermove"], ["move", 596, 318, 1678941407686, "pointermove"],
        ["move", 594, 321, 1678941407694, "pointermove"], ["move", 593, 326, 1678941407701, "pointermove"],
        ["move", 589, 331, 1678941407709, "pointermove"], ["move", 586, 335, 1678941407717, "pointermove"],
        ["move", 582, 340, 1678941407725, "pointermove"], ["move", 578, 347, 1678941407731, "pointermove"],
        ["move", 575, 354, 1678941407740, "pointermove"], ["move", 574, 360, 1678941407746, "pointermove"],
        ["move", 574, 366, 1678941407754, "pointermove"], ["move", 574, 375, 1678941407762, "pointermove"],
        ["move", 574, 378, 1678941407770, "pointermove"], ["move", 574, 384, 1678941407777, "pointermove"],
        ["move", 576, 390, 1678941407785, "pointermove"], ["move", 576, 392, 1678941407791, "pointermove"],
        ["move", 578, 397, 1678941407800, "pointermove"], ["move", 578, 399, 1678941407808, "pointermove"],
        ["move", 579, 403, 1678941407815, "pointermove"], ["move", 581, 406, 1678941407821, "pointermove"],
        ["move", 583, 409, 1678941407829, "pointermove"], ["move", 586, 413, 1678941407836, "pointermove"],
        ["move", 590, 418, 1678941407845, "pointermove"], ["move", 594, 423, 1678941407851, "pointermove"],
        ["move", 599, 427, 1678941407859, "pointermove"], ["move", 606, 432, 1678941407867, "pointermove"],
        ["move", 613, 438, 1678941407874, "pointermove"], ["move", 612, 437, 1678941407875, "pointermove"],
        ["move", 620, 441, 1678941407882, "pointermove"], ["move", 627, 445, 1678941407890, "pointermove"],
        ["move", 634, 447, 1678941407896, "pointermove"], ["move", 640, 449, 1678941407905, "pointermove"],
        ["move", 646, 450, 1678941407912, "pointermove"], ["move", 647, 451, 1678941407919, "pointermove"],
        ["move", 654, 452, 1678941407927, "pointermove"], ["move", 663, 454, 1678941407936, "pointermove"],
        ["move", 667, 454, 1678941407941, "pointermove"], ["move", 667, 453, 1678941407942, "pointermove"],
        ["move", 680, 455, 1678941407950, "pointermove"], ["move", 694, 457, 1678941407956, "pointermove"],
        ["move", 699, 457, 1678941407964, "pointermove"], ["move", 714, 457, 1678941407971, "pointermove"],
        ["move", 718, 457, 1678941407979, "pointermove"], ["move", 728, 457, 1678941407987, "pointermove"],
        ["move", 739, 456, 1678941407994, "pointermove"], ["move", 739, 456, 1678941407995, "pointermove"],
        ["move", 742, 456, 1678941408002, "pointermove"], ["move", 754, 456, 1678941408009, "pointermove"],
        ["move", 760, 456, 1678941408016, "pointermove"], ["move", 777, 459, 1678941408024, "pointermove"],
        ["move", 791, 460, 1678941408031, "pointermove"], ["move", 791, 460, 1678941408032, "pointermove"],
        ["move", 804, 461, 1678941408040, "pointermove"], ["move", 815, 462, 1678941408047, "pointermove"],
        ["move", 823, 462, 1678941408055, "pointermove"], ["move", 829, 462, 1678941408061, "pointermove"],
        ["move", 834, 461, 1678941408070, "pointermove"], ["move", 836, 460, 1678941408076, "pointermove"],
        ["move", 837, 459, 1678941408092, "pointermove"], ["move", 838, 459, 1678941408099, "pointermove"],
        ["move", 838, 459, 1678941408121, "pointermove"], ["move", 839, 459, 1678941408137, "pointermove"],
        ["move", 841, 459, 1678941408145, "pointermove"], ["move", 842, 458, 1678941408151, "pointermove"],
        ["move", 844, 458, 1678941408159, "pointermove"], ["move", 847, 455, 1678941408166, "pointermove"],
        ["move", 849, 454, 1678941408175, "pointermove"], ["move", 850, 452, 1678941408182, "pointermove"],
        ["move", 852, 451, 1678941408190, "pointermove"], ["move", 854, 447, 1678941408197, "pointermove"],
        ["move", 856, 445, 1678941408204, "pointermove"], ["move", 859, 442, 1678941408211, "pointermove"],
        ["move", 862, 439, 1678941408220, "pointermove"], ["move", 863, 436, 1678941408226, "pointermove"],
        ["move", 867, 431, 1678941408235, "pointermove"], ["move", 870, 427, 1678941408242, "pointermove"],
        ["move", 873, 423, 1678941408250, "pointermove"], ["move", 878, 415, 1678941408257, "pointermove"],
        ["move", 880, 410, 1678941408266, "pointermove"], ["move", 882, 404, 1678941408271, "pointermove"],
        ["move", 882, 404, 1678941408272, "pointermove"], ["move", 884, 399, 1678941408279, "pointermove"],
        ["move", 886, 391, 1678941408287, "pointermove"], ["move", 886, 385, 1678941408294, "pointermove"],
        ["move", 886, 381, 1678941408302, "pointermove"], ["move", 886, 376, 1678941408310, "pointermove"],
        ["move", 886, 372, 1678941408316, "pointermove"], ["move", 883, 367, 1678941408324, "pointermove"],
        ["move", 880, 363, 1678941408331, "pointermove"], ["move", 874, 358, 1678941408340, "pointermove"],
        ["move", 868, 353, 1678941408346, "pointermove"], ["move", 862, 349, 1678941408355, "pointermove"],
        ["move", 854, 344, 1678941408362, "pointermove"], ["move", 849, 342, 1678941408370, "pointermove"],
        ["move", 843, 340, 1678941408376, "pointermove"], ["move", 838, 339, 1678941408385, "pointermove"],
        ["move", 832, 337, 1678941408391, "pointermove"], ["move", 828, 337, 1678941408400, "pointermove"],
        ["move", 825, 336, 1678941408407, "pointermove"], ["move", 822, 336, 1678941408415, "pointermove"],
        ["move", 821, 336, 1678941408423, "pointermove"], ["move", 819, 335, 1678941408430, "pointermove"],
        ["move", 818, 335, 1678941408438, "pointermove"], ["move", 818, 335, 1678941408452, "pointermove"],
        ["move", 817, 335, 1678941408459, "pointermove"], ["move", 815, 335, 1678941408482, "pointermove"],
        ["move", 814, 334, 1678941408490, "pointermove"], ["move", 812, 333, 1678941408496, "pointermove"],
        ["move", 808, 331, 1678941408505, "pointermove"], ["move", 803, 329, 1678941408511, "pointermove"],
        ["move", 796, 326, 1678941408519, "pointermove"], ["move", 793, 323, 1678941408527, "pointermove"],
        ["move", 789, 323, 1678941408534, "pointermove"], ["move", 786, 322, 1678941408542, "pointermove"],
        ["move", 783, 321, 1678941408549, "pointermove"], ["move", 783, 321, 1678941408550, "pointermove"],
        ["move", 782, 321, 1678941408556, "pointermove"], ["move", 781, 321, 1678941408564, "pointermove"],
        ["move", 781, 320, 1678941408571, "pointermove"], ["move", 779, 320, 1678941408646, "pointermove"],
        ["move", 778, 320, 1678941408662, "pointermove"], ["move", 778, 321, 1678941408692, "pointermove"],
        ["move", 778, 321, 1678941408706, "pointermove"],
        ["down", 778, 321, 1678941409001, "pointerdown"],
        ["focus", 1678941409001],
        ["up", 778, 321, 1678941409074, "pointerup"]
    ]
    total = len(trajectory_base_1)
    time_interval = [random.randint(2, 25) for _ in range(total - 1)]
    time_interval.insert(0, 0)
    t1 = int(time_str())
    t2 = t1 + sum(time_interval)
    trajectory_1 = []
    for i in range(total):
        if i == 0:
            trajectory_1.append(
                [trajectory_base_1[i][0], [trajectory_base_1[i][1], trajectory_base_1[i][2]], time_interval[i]])
        elif i == (total - 2):
            trajectory_1.append([trajectory_base_1[i][0], time_interval[i]])
        elif i == (total - 1):
            trajectory_1.append([trajectory_base_1[i][0], [trajectory_base_1[i][1] - trajectory_base_1[i - 2][1],
                                                           trajectory_base_1[i][2] - trajectory_base_1[i - 2][2]],
                                 time_interval[i]])
        else:
            trajectory_1.append([trajectory_base_1[i][0], [trajectory_base_1[i][1] - trajectory_base_1[i - 1][1],
                                                           trajectory_base_1[i][2] - trajectory_base_1[i - 1][2]],
                                 time_interval[i]])

    t3 = t1 - 15650 - sum(time_interval)
    t4 = [t3 + random.randint(15, 200) for _ in range(26)]

    trajectory_1_1 = '"fp":["move",346,363,' + str(t1) + ',"pointermove"],"lp":["up",778,321,' + \
                     str(t2) + ',"pointerup"],"em":{"ph":0,"cp":0,"ek":"11","wd":1,"nt":0,"si":0,"sc":0},"tm":{' + \
                     f'"a":{t3},"b":0,"c":0,"d":0,"e":0,"f":{t4[1]},"g":{t4[2]},"h":{t4[3]},"i":{t4[4]},"j":{t4[5]},"k":{t4[6]},"l":{t4[7]},"m":{t4[8]},"n":{t4[9]},"o":{t4[10]},"p":{t4[11]},"q":{t4[12]},"r":{t4[13]},"s":{t4[14]},"t":{t4[15]},"u":{t4[16]}' + \
                     '}'

    pass_time = random.randint(800, 2600)
    gt_ch_pt = gt + ch + str(pass_time)
    info_browser_1 = my_args_[0].replace("!!", "magic data")
    info_graphics_card = '{"v":"9.1.2","de":false,"te":false,"$_BBS":true,"ven":"Google Inc. (NVIDIA)","ren":"ANGLE (NVIDIA, NVIDIA Quadro P2000 Direct3D11 vs_5_0 ps_5_0, D3D11)",' + \
                         trajectory_1_1 + ',"dnf":"dnf","by":0}'
    return (gt, ch, my_args_[1], trajectory_1, my_args_[0], info_browser_1, info_graphics_card, gt_ch_pt, pass_time)


def my_args_slide_2(point_x):
    trajectory = []
    flag_ = point_x // 3 - 5
    for i in range(flag_):
        # slow
        if i < int(flag_ * 0.2):
            if i == 0:
                trajectory.append([1, 1, 89])
            else:
                trajectory.append(
                    [
                        trajectory[i - 1][0] + random.randint(3, 5),
                        trajectory[i - 1][1] + random.randint(1, 2),
                        trajectory[i - 1][2] + random.randint(8, 10)
                    ])
        elif i < int(flag_ * 0.5):
            trajectory.append(
                [
                    trajectory[i - 1][0] + random.randint(3, 5),
                    trajectory[i - 1][1] + random.randint(-1, 1),
                    trajectory[i - 1][2] + random.randint(20, 39)
                ])
        elif i < int(flag_ * 0.8):
            trajectory.append(
                [
                    trajectory[i - 1][0] + random.randint(2, 4),
                    trajectory[i - 1][1] + random.randint(-1, 1),
                    trajectory[i - 1][2] + random.randint(40, 100)
                ])
        else:
            trajectory.append(
                [
                    trajectory[i - 1][0] + random.randint(1, 2),
                    trajectory[i - 1][1] + random.randint(-1, 1),
                    trajectory[i - 1][2] + random.randint(100, 400)
                ])

    flag_point = copy.deepcopy(point_x)
    flag_i = 1
    for j in trajectory[::-1]:
        if j[0] >= point_x:
            trajectory[flag_ - flag_i][0] = flag_point
            flag_point -= 1
        flag_i += 1
    if trajectory[-1][0] < point_x:
        trajectory[-1][0] = point_x
    trajectory = [[-39, -30, 0], [0, 0, 0]] + trajectory
    return trajectory


def __ease_out_expo(x):
    if x == 1:
        return 1
    else:
        return 1 - pow(2, -10 * x)


def __ease_out_quart(x):
    return 1 - pow(1 - x, 4)


def my_args_slide_3(distance):
    if not isinstance(distance, int) or distance < 0:
        raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
    # 初始化轨迹列表
    slide_track = [
        [random.randint(20, 60), random.randint(10, 40), 0]
    ]
    # 共记录count次滑块位置信息
    count = 30 + int(distance / 2)
    # 初始化滑动时间
    t = random.randint(50, 100)
    # 记录上一次滑动的距离
    _x = 0
    _y = 0
    for i in range(count):
        # 已滑动的横向距离
        x = round(__ease_out_expo(i / count) * distance)
        # 滑动过程消耗的时间
        t = random.randint(10, 20)
        if x == _x:
            continue
        slide_track.append([x - _x, _y, t])
        _x = x
    slide_track.append([0, 0, random.randint(200, 300)])
    return slide_track
