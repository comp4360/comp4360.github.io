---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
title: Exercise 0
permalink: /exercises/exercise00
---
{% include latex.html %}


# Hello World!


This simple example is to show you how to work with a Jupyter Notebook file. This paragraph is written in a markdown cell. You can add or delete cells from the menu. The following cell is a **code** cell. Just by selecting the cell and clicking **run** you can run the code inside the cell. Alternatively you can hit shift+enter to run the code.


```python
import os
print os.getcwd()
print 'Hello World!'
```

You can call different libraries within the code. For this course we will be using pillow library which can be used simply as follows:


```python
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('lena.png')
%matplotlib inline
plt.imshow(np.asarray(img))
plt.show()
```


![png](/exercises/exercise00_files/exercise00_3_0.png)


**Matplotlib** can be used to view pillow image files inline within a notebook cell. See the ***inline*** usage of matplotlib in the above cell. I is also possible to write reference mathematical equations within **ipynb** files.  Equations further can be numbered and referenced.Can be referenced with Equation \eqref{eq:deneme}

$$ \begin{equation} 
F = m a\label{eq:deneme} 
\end{equation} 
$$

