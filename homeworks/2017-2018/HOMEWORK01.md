---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
title: Homework 1
permalink: /homeworks/HOMEWORK01
---
{% include latex.html %}
# HOMEWORK01

Image resizing is a widely use operation in image processing. Either for scaling up and for scaling down we need interpolation to find corresponding pixel intensity in the resulting image. Choice of the interpolation method is so important that it directly increases or decreases the quality  of the resulting image.

Recalling the last lecture; we have seen three main interpolation methods:

 - Nearest Neighbour Interpolation
 - Bilinear Interpolation
 - Bicubic Interpolation

If you look at [pillows reference page](http://pillow.readthedocs.io/en/3.1.x/reference/Image.html#functions) you can see that the **resize()** function has predefined resampling functions namely:

 - PIL.Image.NEAREST
 - PIL.Image.BILINEAR
 - PIL.Image.BICUBIC
 - PIL.Image.LANCZOS

From which the first three are the methods we have seen in the lecture. LANCZOS is a more sophisticated method which gives better results compared to first three methods. If you're interested search the internet for more details on **LANCZOS Resampling Method**.

In this homework you will implement a jupyter notebook script and it will perform these operations:

 - The program will read colored "lena.png",
 - The program will convert colored lena image to grayscale image,
 - The program will resize the grayscale lena image to its half size then resize it back to its original size by using **resize()** with PIL.Image.NEAREST then display it inline and print the PSNR value wrt original image below the result image.
 - The program will resize the grayscale lena image to its half size then resize it back to its original size by using **resize()** with PIL.Image.BILINEAR then display it inline and print the PSNR value wrt original image below the result image.
 - The program will resize the grayscale lena image to its half size then resize it back to its original size by using **resize()** with PIL.Image.BICUBIC then display it inline and print the PSNR value wrt original image below the result image.

_PSNR (Peak signal to Noise Ratio):  PSNR is a metric which measures the difference between two images. We can define it as Equation \eqref{eq:PSNR}, where R is the maximum intensity observed in the source image. MSE is the mean square cumulative difference between the source and the target image._

$$ \begin{equation}
PSNR = 10 log_{10}(\frac{R^2}{MSE})\label{eq:PSNR}
\end{equation} $$

_The following function can be used to calculate  PSNR between a source (im1) and target (im2) image._


```python
def PSNR(im1,im2):
	R2 = np.amax(im1)**2
	MSE =  np.sum(np.power(np.subtract(im1,im2),2))
	MSE /= (im1.size[0]*im1.size[1])
	PSNR = 10*np.log10(R2/MSE)
	return PSNR
```

Your program will create a inline 3 by 1 matplotlib plot, by using subplot method, inside your ipython notebook file which looks as follows.


![png](HOMEWORK01_files/HOMEWORK01_4_0.png)


From left to right:

 - The result image created with down-up scaling using Nearest Neighbour Interpolation.
 - The result image created with down-up scaling using Bilinear Interpolation.
 - The result image created with down-up scaling using Bicubic Interpolation.

 x axis of the figures should be the corresponding PSNR value with respect to original input image where y axis of the figures should be the interpolation method.

### Your homework file should contain not only the python script performing desired task but also your explanations and your interpretations. For example make the following interpretations in your homework in your own words:
 - What does this change in PSNR value for each case mean to us?.
 - Perform the same operation with the quarter and one eighth size of the original image. How does the PSNR value change? What does it tell us?

# HOMEWORK SUBMISSION GUIDELINE:

The homework submission guideline is of grave importance for this course. Improper submissions will not be graded!.

 - Rename your ipynb file accordingly. It should both indicate your student number (lets assume it is 12345678) and the corresponding homework number (lets assume it is homework 1). Hence the file should be renamed as **12345678HW01.ipynb** (Beware of the capital HW letters!)
 - You will submit your homework by mailing it to **ikcumee404@gmail.com** address. The subject of your mail should also be named accordingly. It contain course number (MEE404), the homework number (lets assume it is homework 1) and your student number (lets assume it is 12345678). Hence the subject field of your submission mail should be  MEE404 HW01 12345678 (each separated by a single space!)
 - Co-operation is strongly prohibited!
 - Try to submit before the announced deadline or 25 pts. will be taken off for the next day.
 - Homeworks submitted later than one day will not be graded.
