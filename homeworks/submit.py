from comp4360 import submit

data = {}
data['lecture'] = 'COMP4360' # DO NOT CHANGE THIS
data['homework_number'] = '...' # WRITE THE CORRECT HOMEWORK NUMBER HERE
data['student_number'] = '...' # WRITE YOUR STUDENT NUMBER CORRECTLY!
data['student_name_surname'] = '...' # IT IS IMPORTANT THAT YOU WRITE YOUR NAME AND SURNAME CORRECTLY IN THIS FIELD
data['script_name'] = '...' # THE NAME OF THE SCRIPT YOU'RE GOING TO SUBMIT
data['image_name'] = '...' # THE NAME OF THE OUTPUT IMAGE YOU'RE GOING TO SUBMIT
# DO NOT CHANGE THE FOLLOWING CONSENT SENTENCE, SUBMISSIONS WITHOUT THIS EXACT CONSENT SENTENCE WILL NOT BE GRADED
data['consent'] = 'I pledge on my honor that: \n \
I have completed all steps of the attached homework on my own, \n \
I have not used any unauthorized materials while completing this homework, and \n \
I have not given anyone else access to my homework. \n'
data['cc']  = '...' # IF YOU WANT YOU CAN SUBMIT A COPY OF YOUR SUBMISSION TO YOUR PERSONAL EMAIL ADDRESS 
data['user']  = '...@gmail.com' # THIS IS THE GMAIL ADDRESS YOU CREATED FOR SUBMISSION
data['password'] = '...' # THIS IS THE PASSWORD FOR THE GMAIL ADDRESS YOU ENTERED ABOVE

print(submit(data))