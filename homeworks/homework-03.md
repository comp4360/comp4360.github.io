---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
title: Homework 03
permalink: /homeworks/homework-03/
---

### **Homework 03**

 _(Due Date: 28.03.2019 23:59:59)_

(Read the below text completely!)

## Prework

- Before starting your implementation make sure that you already read [Basic Python Tutorial](/tutorials/basic-python-tutorial/){:target='_blank'}. 
and [Homework Submission tutorial](/tutorials/homework-submission-tutorial/){:target='_blank'}. 

- Also it is important that you downloaded the most recent versions of the scripts  [comp4360.py (v1.3)](/homeworks/comp4360.py){:target='_blank'}  and [submit.py](/homeworks/submit.py).

- For this homework, you will send just your python script and you WONT send an output image. Hence you SHOULD leave the data['image_name'] field empty while performing your submission.

- Do not cooperate while writing your codes
- Read the homework text completely
- Fill in [submit.py](/homeworks/submit.py) with correct parameter values
- DO NOT modify any line in [comp4360.py](/homeworks/comp4360.py){:target='_blank'} 
- Current version is 1.3 make sure that you are using the correct up-to-date version of [comp4360.py](/homeworks/comp4360.py){:target='_blank'}


## Problem

You have already seen intensity transformation functions in the lectures and now you know how they work. In this homework you're going to write a python script which is capable of reading user inputs from the command line. The script is going to accept two input image file names which are the transformation function (itf) image  and the input image file name . You'll reconstruct the itf from the itf  image you're going to read and the output image will be the transformed version of the input image. For simplicity consider that the itf image is of size 255 by 255.

See the sample input image - itf image - output image triplets below:

## EXAMPLE 1

| [![Source Image](/homeworks/car.png)](/homeworks/car.png)  | [![ITF Image](/homeworks/itf2.png)](/homeworks/itf2.png)  | [![Output Image](/homeworks/out-car-itf2.png)](/homeworks/out-car-itf2.png)  |
|:---:|:---:|:---:|
| Source Image | ITF Image | Output Image |


## EXAMPLE 2

| [![Source Image](/homeworks/xray.jpg)](/homeworks/xray.jpg)  | [![ITF Image](/homeworks/itf3.png)](/homeworks/itf3.png)  | [![Output Image](/homeworks/out-xray-itf3.png)](/homeworks/out-xray-itf3.png)  |
|:---:|:---:|:---:|
| Source Image | ITF Image | Output Image |


## EXAMPLE 3

| [![Source Image](/homeworks/xray.jpg)](/homeworks/xray.jpg)  | [![ITF Image](/homeworks/itf4.png)](/homeworks/itf4.png)  | [![Output Image](/homeworks/out-xray-itf4.png)](/homeworks/out-xray-itf4.png)  |
|:---:|:---:|:---:|
| Source Image | ITF Image | Output Image |

## Important Notice

- For this homework you SHOULD name your python script as your student number. i.e. If your student number is '123456789' your python file should be named as '123456789.py'. Your output image name should also match with your student id. You run your code from terminal as follows:

```console
$ python 123456789.py itf2.png car.png
```

```python
#!/usr/bin/env python
# coding: utf-8

# USE ONLY THE FOLLOWING LIBRARIES DO NOT ADD ANYTHING TO THIS LINE
from comp4360 import Image, np, sys

# INSERT YOUR CODE HERE
```