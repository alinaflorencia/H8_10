#!/usr/bin/env python
# coding: utf-8

# In[1]:


def perkalian(*data):
    hasil = 1
    for item in data:
        hasil *= item
    return hasil

