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
    '''
    Updates the location on the board and also outputs reward for motion
    '''
    global x, y
    direction = np.random.random_integers(0,3)
    reward = 0 # Will use as flag
    # Special positions A and B
    if (x,y) == (0,1):
        x = 4
        reward = 10
    elif (x,y) == (0,3):
        x = 2
        reward = 5
    # General motion
    else:
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
            reward = -1
        if x == 5:
            x = 4
            reward = -1
        if y == -1:
            y = 0
            reward = -1
        if y == 5:
            y = 4
            reward = -1
    print a[x,y], reward

# Useful ML: http://math.stackexchange.com/questions/213998/recursively-solving-a-bellman-equation

update_loc()
