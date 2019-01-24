#!/usr/bin/python
# -*- coding:utf-8 -*-
#Written by Şükrü Ozan

import numpy as np
from PIL import Image

im = Image.open('rose1024.jpg')

for i in [512,256,128,64,32,16,8]:
	print i
	filename = 'rose'+str(i)+'.jpg'
	im.resize((i,i)).save(filename,format='JPEG')