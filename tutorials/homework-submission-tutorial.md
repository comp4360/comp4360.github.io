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
data['lecture'] = 'COMP4360' # DO NOT CHANGE THIS
data['homework_number'] = '1' # WRITE THE CORRECT HOMEWORK NUMBER HERE
data['student_number'] = '123456789' # WRITE YOUR STUDENT NUMBER CORRECTLY!
data['student_name_surname'] = 'Ali Veli' # IT IS IMPORTANT THAT YOU WRITE YOUR NAME AND SURNAME CORRACTLY IN THIS FIELD
data['script_name'] = 'my_script.py' # THE NAME OF THE SCRIPT YOU'RE GOING TO SUBMIT
data['image_name'] = 'my_image.png' # THE NAME OF THE OUTPUT IMAGE YOU'RE GOING TO SUBMIT
# DO NOT CHANGE THE FOLLOWING CONSENT SENTENCE, SUBMISSIONS WITHOUT THIS EXACT CONSENT SENTENCE WILL NOT BE GRADED
data['consent'] = 'I pledge on my honor that: \n \
I have completed all steps of the attached homework on my own, \n \
I have not used any unauthorized materials while completing this homework, and \n \
I have not given anyone else access to my homework. \n'
data['cc']  = '' # IF YOU WANT YOU CAN SUBMIT A COPY OF YOUR SUBMISSION TO YOUR PERSONAL EMAIL ADDRESS 

print(submit(data))
```

- All the allowed libraries will be in comp4360.pyc file. You can call functions from this library by using the above scheme using "from,import" structure, or you would prefer to import the whole comp4360 library and call functions as a library instance e.g.:

```python
import comp4360
.
.
print(comp4360.submit(data))
```


- You should NOT change the prefined fields showing the course code _(i.e. data['lecture'])_ and consent sentence _(i.e. data['consent'] = '...')_ . Consent sequence is your statement that you do NOT cheat while preparing and submiting a homework. Submissions WITHOUT this exact consent sentence WILL NOT BE graded. 

- The other fields  should be filled correctly. All the files, i.e. your script, comp4360.pyc, submit.py and the output image should be in the same directory for your submission to work. You should write the name of your script and output image file correctly in the corresponding data field.

- If you followed every step correctly by simply running submit.py from terminal you should be able to submit your homework. If you want you can add your mail address to the data field _(i.e. data['cc'])_ and see how your submission actually looks like. The run should return 'email sent' message to you from within the terminal. 

```sh
(venv-imageprocessinglecture)$ python submit.py
email sent
```

- Make your submissions till the declared due date for each homework. 