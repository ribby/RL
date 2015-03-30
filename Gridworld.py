# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 22:36:29 2015

@author: oromi_000
"""

# Imports
import numpy as np

#grid = np.zeros((5,5))
a = np.arange(25).reshape(5,5)
print a
values = np.zeros([5,5])
print values

i = 0
j = 1
temp = values

if j == 0:
    left = temp[i,j]
else: 
    left = temp[i,j-1]
if j == 4:
    right = temp[i,j]
else:
    right = temp[i,j+1]
if i == 0:
    up = temp[i,j]
else:
    up = temp[i-1,j]
if i == 4:
    down = temp[i,j]
else:
    down = temp[i+1,j]
print left, right, up, down
values[i,j] = 0.25*(-4 + left + right + up + down)
print values
print temp

j += 1

#==============================================================================
# i += 1
# j = 0
# while j < 5:
#     if j == 0:
#         left = temp[i,j]
#     else: 
#         left = temp[i,j-1]
#     if j == 4:
#         right = temp[i,j]
#     else:
#         right = temp[i,j+1]
#     if i == 0:
#         up = temp[i,j]
#     else:
#         up = temp[i-1,j]
#     if i == 4:
#         down = temp[i,j]
#     else:
#         down = temp[i+1,j]
#     print left, right, up, down
#     values[i,j] = 0.25*(-4 + left + right + up + down)
#==============================================================================
#    j += 1
#print values

#==============================================================================
# def update_value(mat):
#     temp = mat
#     i = 0
#     j = 1
#     for ele in range(0,mat.size):
#         if j == 0:
#             left_val = temp[i,j]
#         else:
#             left_val = temp[i,j-1]
#         print left_val
#         j += 1
#         j = i % 5
#==============================================================================
#update_value(a)
