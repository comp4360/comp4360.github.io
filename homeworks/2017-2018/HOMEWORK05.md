---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
title: Homework 5
permalink: /homeworks/HOMEWORK05
---
{% include latex.html %}

# HOMEWORK05 (Deadline 31.05.2018 23:59:59)
- In this homework you will write a python script and submit your homework as a single python file with **.py** file extension **NOT an IPYNB file**!!!
- The script will read the input image file name and output image file name from **command line**.
- The aim of the program is to filter out selected frequency regions of an image by using rectangle selector of **matplotlib**.
- First of all you must be able to get the following sample code up and running on your system. This is a basic usage of rectangle selector of matplotlib.

```python
from __future__ import print_function
from matplotlib.widgets import RectangleSelector
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def line_select_callback(eclick, erelease):
    'eclick and erelease are the press and release events'
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    print("(%3.2f, %3.2f) --> (%3.2f, %3.2f)" % (x1, y1, x2, y2))
    print(" The button you used were: %s %s" % (eclick.button, erelease.button))


def toggle_selector(event):
    print(' Key pressed.')
    if event.key in ['Q', 'q'] and toggle_selector.RS.active:
        print(' RectangleSelector deactivated.')
        toggle_selector.RS.set_active(False)
    if event.key in ['A', 'a'] and not toggle_selector.RS.active:
        print(' RectangleSelector activated.')
        toggle_selector.RS.set_active(True)

%matplotlib inline
fig, current_ax = plt.subplots()                 # make a new plotting range
N = 100000                                       # If N is large one can see
x = np.linspace(0.0, 10.0, N)                    # improvement by use blitting!

plt.plot(x, +np.sin(.2*np.pi*x), lw=3.5, c='b', alpha=.7)  # plot something
plt.plot(x, +np.cos(.2*np.pi*x), lw=3.5, c='r', alpha=.5)
plt.plot(x, -np.sin(.2*np.pi*x), lw=3.5, c='g', alpha=.3)

print("\n      click  -->  release")

# drawtype is 'box' or 'line' or 'none'
toggle_selector.RS = RectangleSelector(current_ax, line_select_callback,
                                       drawtype='box', useblit=True,
                                       button=[1, 3],  # don't use middle button
                                       minspanx=5, minspany=5,
                                       spancoords='pixels',
                                       interactive=True)
plt.connect('key_press_event', toggle_selector)
plt.show()

```

- Your program should be able to make the user able to select multiple areas to be filtered out till the user pushes q or Q button.
- Once the user stops selecting areas the program should reconstruct the output image from the filtered out frequency domain image.
- Prepare a project report and explain your work in as much detail as possible but with your own words. Send a separate pdf file for the report.
- Submit your homework according to the submission guideline below.
- See below the video of how a desired script run would look like:

<div align="center">
  <a href="https://www.youtube.com/watch?v=wZMMWjlZZ5Q&feature=youtu.be"><img src="https://img.youtube.com/vi/wZMMWjlZZ5Q/0.jpg" alt="HW05 SAMPLE RUN" target="blank"></a>
</div>


# HOMEWORK SUBMISSION GUIDELINE:

The homework submission guideline is of grave importance for this course. Improper submissions will not be graded!.

- In this homework you will send one python script file and a report pdf file.
- The python script should be named accordingly. It should both indicate your student number (lets assume it is 12345678) and the corresponding homework number (lets assume it is homework 5). Hence the file should be renamed as **12345678HW05.py** (Beware of the capital HW letters!)
- The project report should be named accordingly. It should both indicate your student number (lets assume it is 12345678) and the corresponding homework number (lets assume it is homework 5). Hence the file should be renamed as **12345678HW05.pdf** (Beware of the capital HW letters!) The report should be in an academic article format. [Use this word article format](https://drive.google.com/open?id=1brUR6dAqKebbB7BZWObShHEV9kLmAxcP) 
- You will submit your homework by mailing it to **ikcumee404@gmail.com** address. The subject of your mail should also be named accordingly. It contain course number (MEE404), the homework number (lets assume it is homework 5) and your student number (lets assume it is 12345678). Hence the subject field of your submission mail should be  MEE404 HW05 12345678 (each separated by a single space!)
- Co-operation is strongly prohibited!
- Try to submit before the announced deadline or 25 pts. will be taken off for the next day.
- Homeworks submitted later than one day will not be graded.
