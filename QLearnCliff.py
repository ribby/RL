# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:28:09 2015

@author: oromi_000
"""

import numpy as np

# Define Q-learning specific constants
gamma = 1
epsilon = 0.1
maxEpisodes = 100

# Initializing the number of actions. Assuming same number of actions for all state
nActions = 4
action = []
for i in xrange(0,nActions):
    action.append(0)
    
# Define grid size
HEIGHT = 4
WIDTH = 12
nStates = HEIGHT * WIDTH

# Initializing the action-value function
grid = np.arange(nStates).reshape([HEIGHT,WIDTH])        # Assigns a number to each state
Q = {}
for i in grid:
    for j in i:
        Q[j] = action
print Q
print state

