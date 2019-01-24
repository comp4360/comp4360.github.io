#!/usr/bin/python
# -*- coding:utf-8 -*-
#Written by Şükrü Ozan

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('lena.png')
img.show()
#%matplotlib inline
plt.imshow(np.asarray(img))
plt.show()