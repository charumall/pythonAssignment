#!/usr/bin/env python
# coding: utf-8

# # My Jupyter Notebook on IBM Watson Studio

# **Charu Mall**
# 
# Assistant Manager

# *I am interested in data science because I love playing with data*

# ### Following code finds the integer portion of a real number

# In[1]:


a = float(input("Enter a real number: "))
b = round(a)
if a > 0:
    if b > a:
        integerPortion = b-1
    else:
        integerPortion = b
    print(integerPortion)
else:
    if a > b:
        integerPortion = b+1
    else:
        integerPortion = b
    print(integerPortion)


# This file contains
# 
# 1. My Name
# 2. Designation
# 3. Code Sample

# [This is a link for google](https://www.google.com)

# Number1 | Number2 | Sum
# ---|---|:---:
# 2 | 6 | 8
# 8 | 9 | 17
