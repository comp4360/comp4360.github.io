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


Make sure that you read [Homework Submission tutorial](/tutorials/homework-submission-tutorial/){:target='_blank'}. 

Once you installed the requirements and activated your virtual environment, you can start writing your homeworks. It is important that you also download [comp4360.pyc](/homeworks/comp4360.pyc){:target='_blank'} file to the same directory with your script.

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
