---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
title: Homework 01
permalink: /homeworks/homework-01/
---

### **Homework 01**

 _(Due Date: 15.02.2019 23:59:59)_

This homework aims, first of all, to make you install python3.6 on your system and install necessary libraries required for this course. 

Make sure that you read and performed both:
- [Basic Python Tutorial](/tutorials/basic-python-tutorial/){:target='_blank'}. 
- [Homework Submission tutorial](/tutorials/homework-submission-tutorial/){:target='_blank'}. 

Once you installed the requirements and activated your virtual environment, you can start writing your homeworks. It is important that you also download [comp4360.pyc](/homeworks/comp4360.pyc){:target='_blank'} file to the same directory with your script.

In this homework you are going to simply run the following script. You can download the script from [here](/homeworks/files/my_script.py){:target='_blank'}.

```python
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
```

You should be able to run this script if you followed the previous steps correctly. Thsi script needs an input image which you can download from [here](/homeworks/files/my_image.png){:target='_blank'}. It creates an output image whichs is a copy of the input image where some text is inserted on it. The script also seeks for a proper font file which supports Turkish letters. You can download the font file from [here](/homeworks/files/algerya-sans.otf){:target='_blank'}.

Assuming that you finished writing your script you can submit it properly by using [submit.py](/homeworks/submit.py){:target='_blank'}. In the submit file you have to enter the correct information to make a proper submission.

```python
from comp4360 import submit

data = {}
data['lecture'] = 'COMP4360'
data['homework_number'] = ''
data['student_number'] = ''
data['student_name_surname'] = ''
data['script_name'] = ''
data['image_name'] = ''
data['consent'] = 'I pledge on my honor that: \n \
I have completed all steps of the attached homework on my own, \n \
I have not used any unauthorized materials while completing this homework, and \n \
I have not given anyone else access to my homework. \n'
data['cc']  = ''

print(submit(data))
```



```python
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
```