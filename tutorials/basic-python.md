---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
title: Basic Python Tutorial
permalink: /tutorials/basic-python/
---

### **Basic Python Tutorial**

It is strongly recommended that you first finish this tutorial. I will be using Python version 3.6 , hence for convenience, you are expected to install Python version3.6 on your sytem. The walkthrough for the installation is platform specific, you should refer to the official [Python Website](https://www.python.org){:target='_blank'}. Once you're sure that you installed the correct python version on your system CD to correspnding directory for COMP4360 class you created by using whichever name you want to use. Here I preferred COMP4360 for convenience. 

```sh
cd COMP4360
```

It is very common to use virtual environments for specific tasks. It helps you to create and work on a virtual environment specifically tailored for one specific task. It includes a python instance and keeps the core installation isolated. This makes it possible to install and try different python packages without compromising the core installation. Running the following command will create a virtual environment hosted in **venv** directory. It is a common practice to name the directory as **venv**.

```sh
virtualenv -p python3.6 venv
```

"-p  python3.6" option ensures that you create the virtual environment by using python3.6 interpreter. Once you create virtual instance you can work on it by simply running the following command in the terminal. 

```sh
source venv/bin/activate
```

In python installations pip installer comes as dafault. It is straightforward to install a package by using pip. In this class you will need a couple of libraries installed to your system. It is possible to install them one by one but more convenient way is to install them by using a [requirements.txt ](/homeworks/requirements.txt/){:target='_blank'}file. 

```sh
pip3 install -r requirements.txt
```

We will also extensively use pillow,matplotlib and numpy in this course. You can refer to the documents pages of these libraries for more information. During the course necessary and sufficient information will be given to you.

Jupyter  is another common way to interpret with python scripts easily. You can edit, modify and run python scripts within your browser. Contemporary works, especially on machine learning etc., are mostly displayed in jupyter environment. In this course we will NOT be relying on jupyter but I strongly recommend you to install and play with and work on this environment.  See [iPython Tutorial](/tutorials/ipython-tutorial/){:target='_blank'} for further details. 


It is possible to stop virtual environment with the following command

```sh
deactivate
```

I recommend you to check the documentation pages for the libraries given above. You can start with the following tutorials. It is important for you to understand why and where we do use libraries, i.e. pillow, numpy and matplotlib. 

- [Pillow Tutorial](/tutorials/pillow-tutorial/){:target='_blank'}
- [Python Numpy and Matplotlib Tutorial](/tutorials/python-numpy-tutorial/){:target='_blank'}

<!-- 
- [EXERCISE 0](/exercises/exercise00){:target='_blank'}
- [EXERCISE 1](/exercises/exercise01){:target='_blank'}
-->
