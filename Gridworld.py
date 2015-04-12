# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 22:36:29 2015
@author: Alex Rybchuk

Solves the gridworld example as given in Sutton & Barto Chapter 4, Section 2
"""

# Imports
import numpy as np

a = np.arange(25).reshape(5,5) # Test matrix
# Initial value matrix
values = np.zeros([4,4])

i = 0
j = 1

def adj_val(mat, i, j):
    # Getting adjacent values of single element
    if j == 0:
        left = mat[i,j]
    else:
        left = mat[i,j-1]
    if j == len(mat[0])-1:
        right = mat[i,j]
    else:
        right = mat[i,j+1]
    if i == 0:
        up = mat[i,j]
    else:
        up = mat[i-1,j]
    if i == len(mat)-1:
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
    while j < len(mat[0]):
        mat[i,j] = 0.25*(-4 + adj_val(temp,i,j)[0] + adj_val(temp,i,j)[1] + adj_val(temp,i,j)[2] + adj_val(temp,i,j)[3])
        j += 1
    i += 1
    # Middle rows
    while i < len(mat)-1:
        j = 0
        while j < len(mat[0]):
            mat[i,j] = 0.25*(-4 + adj_val(temp,i,j)[0] + adj_val(temp,i,j)[1] + adj_val(temp,i,j)[2] + adj_val(temp,i,j)[3])
            j += 1
        i += 1
    # Last row
    j = 0
    while j < len(mat[0])-1:
        mat[i,j] = 0.25*(-4 + adj_val(temp,i,j)[0] + adj_val(temp,i,j)[1] + adj_val(temp,i,j)[2] + adj_val(temp,i,j)[3])
        j += 1
    return mat
    
for i in range(0,1000):
    print update_val(values)

