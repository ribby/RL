# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 22:36:29 2015

@author: oromi_000
"""

# Imports
import numpy as np

#grid = np.zeros((5,5))
a = np.arange(25).reshape(5,5)
values = np.zeros([5,5])

temp = values.copy() # COPY IS THE ANSWER
values[0,0] += 1
print temp is values
print values
print temp