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
alpha = 0.1

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
        
# Define terminal states
terminal = [37, 38, 39, 40, 41, 42, 43, 44, 45, 46]

def next_states(state):
    '''
    Returns all possible next states in the form [left,right,up,down]
    '''
    global grid
    next_states = []
    # Left
    if state in grid[:,0]:
        next_states.append(state)
    else:
        next_states.append(state-1)
    # Right
    if state in grid[:,-1]:
        next_states.append(state)
    else:
        next_states.append(state+1)
    # Up
    if state in grid[0]:
        next_states.append(state)
    else:
        next_states.append(state-len(grid[0]))
    # Down
    if state in grid[-1]:
        next_states.append(state)
    else:
        next_states.append(state+len(grid[0]))
    return next_states
    
def next_action(state):
    global Q
    global epsilon
    epsilon *= 1000 # Assume epsilon >= 0.001
    rndm = np.randint(0,100000)
    if rndm > epsilon:
        max_action_per_state = []
        next_state = next_states(state)
        for state in next_state:
            max_action_per_state.append(max(Q[state]))
        max_action = max(max_action_per_state)
        return max_action
    else:
        break
        
def update_Q(state,Q,next_state,reward):
    global terminal
    global gamma
    if state in terminal:
        Q = 0
    else:
        Q += alpha * (reward + gamma)
    
print Q
print grid
