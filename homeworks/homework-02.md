---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
title: Homework 02
permalink: /homeworks/homework-02/
---

### **Homework 02**

 _(Due Date: 22.02.2019 23:59:59)_

(Read the below text completely!)

In machine learning, if your aim is to perform a computer vision task, you most of the time prefer to reduce the dimension of an input image. This is due to the architecture of the conventional ML systems. We may  have either  a 1 channel grayscale image or a 3 channel RGB image and  our aim is to reduce it to a 1D array. Some images may even have a fourth channel for alpha which refers to transparency.

In this homework your aiw is to perform the complement of this operation. i.e. You will be given arrays of numbers from which you will reconstruct an image and save it. First 3 integers in the array represent nC ( #channels) nW (width of the image) and nH (height of the image) respectively. By using this information you can reshape the 1D array to the desired image size. See below a brief representation of such an array.

INPUT ARRAY [ nC  nW nH . . . . . . .<image data>. . . . . . . .]

Your script should read the array file name from command line. The array files are numpy array files (i.e. NPY file). You can use the following files to test your script.

- [img1.npy](/homeworks/img1.npy)
- [img2.npy](/homeworks/img2.npy)

You are going to use [comp4360.pyc](/homeworks/comp4360.pyc) in your scripts and use [submit.py](/homeworks/submit.py) to submit your homeworks before the deadline and according to the [homework submission guideline](/tutorials/homework-submission-tutorial/){:target="blank"}. Use the following script template and complete it with your solution. You can enclose any ONE of the images you obtained from the above array files.


```python
#!/usr/bin/env python
# coding: utf-8

from comp4360 import Image
from comp4360 import np #this is the numpy library

```