
from comp4360 import submit


data = {}
data['lecture'] = 'COMP4360'
data['homework_number'] = '1'
data['student_number'] = '1124130'
data['student_name_surname'] = 'Şükrü Ozan'
data['script_name'] = 'my_script.py'
data['image_name'] = 'my_image.png'
data['consent'] = 'I pledge on my honor that: \n \
I have completed all steps of the attached homework on my own, \n \
I have not used any unauthorized materials while completing this homework, and \n \
I have not given anyone else access to my homework. \n'
data['cc']  = ''

print(submit(data))
