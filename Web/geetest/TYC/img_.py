# -*- coding:utf-8 -*-
from PIL import Image

import cv2
import ddddocr


def img_restore(img_path, img_new_path):
    img_ = Image.open(img_path)
    img_new = Image.new('RGB', (260, 160))
    ge_ = [
        39, 38, 48, 49, 41, 40, 46, 47, 35, 34, 50, 51, 33, 32, 28, 29, 27, 26, 36, 37, 31, 30, 44, 45, 43,
        42, 12, 13, 23, 22, 14, 15, 21, 20, 8, 9, 25, 24, 6, 7, 3, 2, 0, 1, 11, 10, 4, 5, 19, 18, 16, 17
    ]
    w_ = 10
    h_ = 80

    for i in range(len(ge_)):
        x = ge_[i] % 26 * 12 + 1
        y = h_ if ge_[i] > 25 else 0
        img_cut = img_.crop((x, y, x + w_, y + h_))
        new_x = i % 26 * 10
        new_y = h_ if i > 25 else 0
        img_new.paste(img_cut, (new_x, new_y))

    img_new.save(img_new_path)


def img_ocr(bg_path, pre_path):
    slide = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)

    with open(bg_path, 'rb') as f:
        target_bytes = f.read()

    with open(pre_path, 'rb') as f:
        background_bytes = f.read()

    img = cv2.imread(bg_path)

    res = slide.slide_comparison(target_bytes, background_bytes)

    return res
