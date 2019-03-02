
# 02.03.2019

import email
import smtplib
import socket
import platform
import sys
import os
import time
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageFilter,ImageDraw,ImageFont
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from pif import get_public_ip

version = "1.3"

# smtplib module send mail
def submit(data):
    TO = "sukruozan@gmail.com"
    SUBJECT = data['lecture'] + ' HW ' + data['homework_number'] + ' ' + data['student_number'] 
    TEXT_CC = data['consent'] + data['student_name_surname'] + '\n' + '\n' + "PLATFORM : "+str(platform.uname()) + '\n' +"PYTHON VERSION : " + str(platform.python_version())+ '\n'+ 'IP: ' + str(get_public_ip())

    auth = {}
    auth['user'] = data['user']
    auth['pass'] = data['password']  

    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT
    msg['To'] = data['cc']
    attachment = MIMEApplication(open(data['script_name'], "rb").read(), _subtype="py")
    attachment.add_header('Content-Disposition', 'attachment', filename=data['script_name'])           
    msg.attach(attachment)
    msg.attach(MIMEText(TEXT_CC))
    if  data['image_name'] != '':
        img = MIMEImage(open(data['image_name'], 'rb').read())
        msg.attach(img)
    
    # Gmail Sign In
    gmail_sender = auth['user']
    gmail_passwd = auth['pass']

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)

    try:
        if data['cc'] != '':
            server.sendmail(gmail_sender, [data['cc']], msg.as_string())
        server.sendmail(gmail_sender, [TO], msg.as_string())
        return 'email sent'
    except:
        return 'error sending mail'
    server.quit()

def print_version():
    print("version:",version)
