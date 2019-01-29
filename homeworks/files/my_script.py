#!/usr/bin/env python
# coding: utf-8

from comp4360 import Image,ImageDraw,ImageFont

img = Image.open("my_image.png")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("algerya-sans.otf", 40)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((0, 0),"Türkçe karakteler: Ü Ö Ş Ğ Ü Ç İ ı ç ü ğ ş ö ü",(255,255,255),font=font)
img.save('sample-out.png')