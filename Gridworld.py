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

# Initialize random location
x = np.random.random_integers(0,4)
y = np.random.random_integers(0,4)
print a[x,y]

def update_loc():
    global x, y
    direction = np.random.random_integers(0,3)
    if direction == 0:
        x += 1
    elif direction == 1:
        x += -1
    elif direction == 2:
        y += 1
    else:
        y += -1
    # Correcting for bounds
    if x == -1:
        x = 0
    if x == 5:
        x = 4
    if y == -1:
        y = 0
    if y == 5:
        y = 4
    print a[x,y]

update_loc()
update_loc()
update_loc()
update_loc()
update_loc()
update_loc()
update_loc()
update_loc()
update_loc()

        
