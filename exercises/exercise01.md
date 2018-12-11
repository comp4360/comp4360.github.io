---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
title: Exercise 1
permalink: /exercises/exercise01
---
{% include latex.html %}
# Creating an Image from Scratch


### QUESTION : 

Remember the definitions of Image and Digital Image;
- An image can be defined as a two dimensional function $$f(x,y)$$ where $$x$$ and $$y$$ are plane coordinates and the amplitude of f at any pair of coordinates $$(x, y)$$ is called the intensity or gray level of image at that point.
- When $$x$$, $$y$$ and the intensity values of $$f$$ are all finite, discrete quantities, we call the image a digital image.


The aim of this exercis is to create an image which is darkest at its center and brightest at image corners. In order to create such an image, mathematical definition of circle can be used. We can use the folllowing circle equation which defines a circle centered at $$(200,300)$$. 
\begin{equation}
f(x,y)=(x−200)^2 +(y−300)^2 
\end{equation}

The following code is trying to create such an image. It defines a circle located at the image center. The desired result is the image on the right but if you run the following script you get the image at the top. There is a little flaw in the following script. Can you find and fix it such that the code generates the image at the bottom?

![circle bad](/exercises/circle-bad.png)

![circle good](/exercises/circle-good.png)



```python
import numpy as np
from PIL import Image

height = 400
width = 600

# Create an empty array
img = np.zeros((height, width), dtype=np.uint8)

#Create [x,y] coordinate combinations on grid
xx, yy = np.mgrid[:height, :width]
#Mathematical definiton of a circle centered at (200,200)
circle = (xx - 200) ** 2 + (yy - 300) ** 2

# Set the RGB values
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        intensity  = circle[x][y]
        img[x][y] = intensity

#Save Image directly from buffer
Image.fromarray(img,'L').save('circle-bad.png','PNG')
```

### ANSWER:

The problem is happening because we are working in 8-bit integer arithmetic and some pixel values cause overflow. (Check the values of array circle). Overflow means that the calculated values are out of 8-bit range ([0, 255]).
The best way to solve such a problem is to normalize the values such that they correctly map into the 8-bit range. Use min-max normalization procedure. Consider the image array as I. Let p represents intensity of an arbitrary pixel from image I and p′ be the normalized pixel intensity, then we can define p′ as follows:

$$ 
\begin{equation}
p' =\frac{255∗ p−\texttt{min}(I)}{\texttt{max}(I) − \texttt{min}(I) }  
\end{equation}
$$


You can use $$\texttt{np.amin()}$$ and $$\texttt{np.amax()}$$ to calculate maximum and minimum values of an array respectively.
