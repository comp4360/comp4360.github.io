---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
title: Homework Submission Tutorial
permalink: /tutorials/homework-submission-tutorial/
---

### **Homework Submission Tutorial**

- Make sure that you read [Basic Python Tutorial](/tutorials/basic-python-tutorial/){:target='_blank'}. It is important that you've configured your virtual environments and install all the requirements accordingly. 

- Once you installed the requirements and activated your virtual environment, you can start writing your homeworks. It is important that you also download [comp4360.pyc](/homeworks/comp4360.pyc){:target='_blank'} file to the same directory with your script.

- Assuming that you finished writing your script you can submit it properly by using [submit.py](/homeworks/submit.py){:target='_blank'}. In the submit file you have to enter the correct information to make a proper submission.

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

- You should NOT change the prefined fields showing the course code _(i.e. data['lecture'])_ and consent sentence _(i.e. data['consent'] = '...')_ . Consent sequence is your statement that you do NOT cheat while preparing and submiting a homework. I hope you will behave accordingly. 

- The other fields  should be filled correctly. All the files, i.e. your script, comp4360.pyc, submit.py and the output image should be in the same directory for your submission to work. You should write the name of your script and output image file correctly in the corresponding data field.

- If you followed every step correctly by simply running submit.py from terminal you should be able to submit your homework. If you want you can add your mail address to the data field _(i.e. data['cc'])_ and see how your submission actually looks like. The run should return 'email sent' message to you from within the terminal. 

'''sh
(venv-imageprocessinglecture)$ python submit.py
'''

- Make your submissions till the declared due date for each homework. 


