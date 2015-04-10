#!/usr/bin/env python
# coding=utf-8
from PIL import Image, ImageDraw, ImageFont


def add_num(pic_path, num, size=None, place=None):
    pic = Image.open(pic_path)

    width, height = pic.size
    font_size = size if size else int(height / 5)
    place = place if place else (width - font_size, 0)

    drawer = ImageDraw.Draw(pic)
    number_font = ImageFont.truetype('microsoft_yahei.TTF', font_size)
    drawer.text(place, str(num), fill=(255, 0, 0), font=number_font)

    pic.save('with_num.png')


if __name__ == '__main__':
    add_num('SLUG.png', 4)
