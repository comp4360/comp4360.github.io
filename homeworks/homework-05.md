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

Since you're familiar with fourier transform, now you can perform frequency domain filtering. In this homework you're going to write a python script which is capable of  performing filtering in fourier domain. The program should show the frequency domain image of an input image. The user should be able to select multiple areas in the frequency domain image and filter them out. 

By this way it can be possible to remove a noise ,e.g. a periodic noise, effectively. Watch the following video to understand how your script should work exactly:


{::nomarkdown}

<!-- HTML CODE-->
<iframe width="560" height="315" src="https://www.youtube.com/embed/wZMMWjlZZ5Q" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

{:/}


See the sample input image -  output image pairs below:

## EXAMPLE 1

| [![Source Image](/homeworks/local-kc.png)](/homeworks/local-kc.png)  | [![Output Image](/homeworks/local-hist-kc.png)](/homeworks/local-hist-kc.png)  |
|:---:|:---:|
| Source Image | Output Image |


## Important Notice

- For this homework you SHOULD name your python script as your student number. i.e. If your student number is '123456789' your python file should be named as '123456789.py'. Your output image name should also match with your student id. You run your code from terminal as follows:

```console
$ python 123456789.py local-kc.png local-hist-kc.png 
```