---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
title: Homework 05
permalink: /homeworks/homework-05/
---

### **Homework 05**

 _(Due Date: 09.05.2019 23:59:59)_

(Read the below text completely!)

## Prework

- It is important that you downloaded the most recent versions of the scripts  [comp4360.py (v1.4)](/homeworks/comp4360.py){:target='_blank'}  and [submit.py](/homeworks/submit.py).
- Before starting your implementation make sure that you already read [Basic Python Tutorial](/tutorials/basic-python-tutorial/){:target='_blank'}.  and [Homework Submission tutorial](/tutorials/homework-submission-tutorial/){:target='_blank'}. 
- For this homework, you will send just your python script and you WONT send an output image. Hence you SHOULD leave the data['image_name'] field empty while performing your submission.
- Do not cooperate while writing your codes
- Read the homework text completely
- Fill in [submit.py](/homeworks/submit.py) with correct parameter values
- DO NOT modify any line in [comp4360.py](/homeworks/comp4360.py){:target='_blank'} 
- Current version is 1.4 make sure that you are using the correct up-to-date version of [comp4360.py](/homeworks/comp4360.py){:target='_blank'}


## Problem

Since you're familiar with fourier transform, now you can perform frequency domain filtering. In this homework you're going to write a python script which is capable of  performing filtering in fourier domain. The program should show the frequency domain image of an input image. The user should be able to select multiple areas in the frequency domain image and filter them out. 

By this way it can be possible to remove a noise ,e.g. a periodic noise, effectively. Watch the following video to understand how your script should work exactly:


{::nomarkdown}

<!-- HTML CODE-->
<iframe width="560" height="315" src="https://www.youtube.com/embed/wZMMWjlZZ5Q" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

{:/}


You can use the following image to test your algırithm:


| [![Source Image](/homeworks/periodic_noise.jpg)](/homeworks/periodic_noise.jpg)  | 
|:---:|
| Image with Periodic Noise |


## Important Notice

- For this homework you SHOULD name your python script as your student number. i.e. If your student number is '123456789' your python file should be named as '123456789.py'. Your output image name should also match with your student id. You run your code from terminal as follows, the output file name should also be read from the commandline input:

```console
$ python 123456789.py sample.jpg result.png
```

- You can You can use the following code as a hint. It can 

```python
#!/usr/bin/env python
# coding: utf-8

# USE ONLY THE FOLLOWING LIBRARIES DO NOT ADD ANYTHING TO THIS LINE
from comp4360 import Image, np, plt, RectangleSelector, sys
.
.
.

def line_select_callback(eclick, erelease):
    global selection
    global fimg,fftimg
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    selection.append([x1,y1,x2,y2])
    fimg[int(y1):int(y2)+1,int(x1):int(x2)+1] = 0
    fftimg[int(y1):int(y2)+1,int(x1):int(x2)+1] = 0

def toggle_selector(event):
    print(' Key pressed.')
    if event.key in ['Q', 'q'] and toggle_selector.RS.active:
        print(' RectangleSelector deactivated.')
        toggle_selector.RS.set_active(False)
        showImage()
        reconstructImage()

    if event.key in ['A', 'a'] and not toggle_selector.RS.active:
        print(' RectangleSelector activated.')
        toggle_selector.RS.set_active(True)


# INSERT YOUR CODE HERE




```