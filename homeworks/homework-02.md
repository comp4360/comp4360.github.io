---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
title: Homework 02
permalink: /homeworks/homework-02/
---

## **Homework 02**

 _(Due Date: 28.02.2019 23:59:59)_

(Read the below text completely!)

### Prework

- Before starting your implementation make sure that you already read [Basic Python Tutorial](/tutorials/basic-python-tutorial/){:target='_blank'}. 
and [Homework Submission tutorial](/tutorials/homework-submission-tutorial/){:target='_blank'}. 

- Also it is important that you downloaded the most recent versions of the scripts  [comp4360.py (v1.2)](/homeworks/comp4360.py){:target='_blank'}  and [submit.py](/homeworks/submit.py).

- For this homework, you will send just your python script and you WONT send an output image. Hence you SHOULD leave the data['image_name'] field empty while performing your submission.


## Problem

In machine learning, if your aim is to perform a computer vision task, you most of the time prefer to reduce the dimension of an input image. This is due to the architecture of the conventional ML systems. We may  have either  a 1 channel grayscale image or a 3 channel RGB image and  our aim is to reduce it to a 1D array. Some images may even have a fourth channel for alpha which refers to transparency.

In this homework your aim is to perform the complement of this operation. i.e. You will be given arrays of numbers from which you will reconstruct an image and save it. First 3 integers in the array represent nC ( #channels) nW (width of the image) and nH (height of the image) respectively. By using this information you can reshape the 1D array to the desired image size. See below a brief representation of such an array.

INPUT ARRAY [ nC  nW nH . . . . . . .<image data>. . . . . . . .]

Your script should read the input file name command line. Input files are  numpy array files (i.e. .npy file). You can use the following files to test your script. You can see the code samples where the user input is taken as a commandline argument in the presentations.

- [img1.npy](/homeworks/img1.npy)
- [img2.npy](/homeworks/img2.npy)

In the script you may need to use the following functions, refer to the document pages of these functions and figure out how you can use them in your code:

- np.load(...)
- reshape() function from numpy library
- Image.fromarray(...)


## Important Notice



- For this homework you SHOULD name your python script as your student number. i.e. If your student number is '123456789' your python file should be named as '123456789.py'. Your output image name should also match with your student id (see the plt.savefig() function below). You run your code from terminal as follows:

```console
$ python 123456789.py img1.npy
```

```python
#!/usr/bin/env python
# coding: utf-8

# USE ONLY THE FOLLOWING LIBRARIES DO NOT ADD ANYTHING TO THIS LINE
from comp4360 import Image, np, sys, os, plt


# INSERT YOUR CODE HERE


# YOU CAN USE THW FOLLOWING SEGMENT TO SAVE THE PLOT AS IMAGE
fig = plt.figure(figsize=(5, 5))
ax1 = fig.add_subplot(111)
ax1.imshow(img)
ax1.set_title('Number of channel(s) = ...)
plt.savefig('123456789.png')
```

When you run your script for [img2.npy](/homeworks/img2.npy), the output figure should look exactly the same as the following figure:

 <div class='fig figcenter'>
  <img src='/homeworks/123456789.png'>
</div>