---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
title: Homework 04
permalink: /homeworks/homework-04/
---

### **Homework 04**

 _(Due Date: 18.04.2019 23:59:59)_

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

In this homework you're goint to write a python script which is capable of  performing local histogram equalization for a given input image. The operation can be performed in 3 by 3 windows. 

See the sample input image -  output image pairs below:

## EXAMPLE 1

| [![Source Image](/homeworks/local-kc.png)](/homeworks/local-kc.png)  | [![Output Image](/homeworks/local-hist-kc.png)](/homeworks/local-hist-kc.png)  |
|:---:|:---:|
| Source Image | Output Image |


## EXAMPLE 2

| [![Source Image](/homeworks/local-yu.png)](/homeworks/local-yu.png)  | [![Output Image](/homeworks/local-hist-yu.png)](/homeworks/local-hist-yu.png)  |
|:---:|:---:|
| Source Image | Output Image |



## Important Notice

- For this homework you SHOULD name your python script as your student number. i.e. If your student number is '123456789' your python file should be named as '123456789.py'. Your output image name should also match with your student id. You run your code from terminal as follows:

```console
$ python 123456789.py local-kc.png local-hist-kc.png 
```