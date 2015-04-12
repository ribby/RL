# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:28:09 2015

@author: oromi_000
"""

import numpy as np

# Define grid size
HEIGHT = 4
WIDTH = 12

nStates = HEIGHT * WIDTH
nActions = 4

# Define Q-learning specific constants
gamma = 1
epsilon = 0.1
maxEpisodes = 100

# Initializing the action-value function
Q = np.zeros([nStates,nActions])
loc = np.arange(nStates).reshape([HEIGHT,WIDTH])
print loc

#==============================================================================
# for ep in xrange(0,maxEpisodes):
#     for step in xrange(0,ep:
#         break    
#==============================================================================
