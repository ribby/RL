# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 22:36:29 2015

@author: oromi_000
"""

# Imports
import numpy as np

# Initial value matrix
a = np.arange(25).reshape(5,5)
values = np.zeros([5,5])

i = 0
j = 1

def adj_val(mat, i, j):
    # Getting adjacent values of single element
    if j == 0:
        left = mat[i,j]
    else:
        left = mat[i,j-1]
    if j == 4:
        right = mat[i,j]
    else:
        right = mat[i,j+1]
    if i == 0:
        up = mat[i,j]
    else:
        up = mat[i-1,j]
    if i == 4:
        down = mat[i,j]
    else:
        down = mat[i+1,j]
    return [left, right, up, down]

def update_val(mat):    
    # Assigning values
    temp = mat.copy()
    i = 0
    j = 1
    # First row
    while j < 5:
        mat[i,j] = 0.25*(-4 + adj_val(temp,i,j)[0] + adj_val(temp,i,j)[1] + adj_val(temp,i,j)[2] + adj_val(temp,i,j)[3])
        j += 1
    i += 1
    # Middle rows
    while i < 4:
        j = 0
        while j < 5:
            mat[i,j] = 0.25*(-4 + adj_val(temp,i,j)[0] + adj_val(temp,i,j)[1] + adj_val(temp,i,j)[2] + adj_val(temp,i,j)[3])
            j += 1
        i += 1
    # Last row
    j = 0
    while j < 4:
        mat[i,j] = 0.25*(-4 + adj_val(temp,i,j)[0] + adj_val(temp,i,j)[1] + adj_val(temp,i,j)[2] + adj_val(temp,i,j)[3])
        j += 1
    return mat
    
print update_val(values)
print update_val(values)


