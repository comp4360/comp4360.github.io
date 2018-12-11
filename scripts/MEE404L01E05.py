#!/usr/bin/python
# -*- coding:utf-8 -*-
#Written by Şükrü Ozan

'''
This Program calculates file size of a given raw (uncompressed) image by using given input values
'''
import numpy as np

channel = input('Enter the number of the color channels (E.g. 1, 3 etc):')
width = input('Enter the pixel width of the image:')
height = input('Enter the pixel height of the image:')
bit = input('Enter the bit length:')

int_level = np.power(2,bit)
bit_size = channel*width*height*bit
byte_size = bit_size/8.0
kb_size = byte_size/1024.0
mb_size = kb_size/1024.0

print("The image you have is "+str(mb_size)+" MBs. "+" The image you have "+str(int_level)+" diffent intensity levels.")
print("The image you have is {0:.2f}".format(mb_size)+" MBs.")