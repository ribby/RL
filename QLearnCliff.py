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
action = np.zeros(nActions,)

    
# Define grid size
HEIGHT = 4
WIDTH = 12
nStates = HEIGHT * WIDTH

# Initializing the action-value function
grid = np.arange(nStates).reshape([HEIGHT,WIDTH])        # Assigns a number to each state
Q = {}
for i in grid:
    for j in i:
        Q[j] = action.copy()
        
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
#==============================================================================
#     global epsilon
#     epsilon *= 1000 # Assume epsilon >= 0.001. Using this as a work around for 
#                                  # random number generation domain
#==============================================================================
    max_action_per_state = []
    next_state = next_states(state)
    for state in next_state:
        max_action_per_state.append(max(Q[state])) # left, right, up, down
    max_action = max(max_action_per_state) 
    if np.random.randint(0,100000) > 100: # greedy action
        return max_action
    else: # exploration
        max_action_per_state.remove(max_action)
        non_optimal_action = max_action_per_state[np.random.randint(0,3)]
        return non_optimal_action
        
#==============================================================================
# def update_Q(state,Q,next_state,reward):
#     global terminal
#     global gamma
#     if state in terminal:
#         Q = 0
#     else:
#         Q += alpha * (reward + gamma)
#==============================================================================
    

print Q[14]
Q[14][0] = 7
Q[3][2] = 10
Q[16][3] = 5
print Q[14]
test = []
for i in xrange(10000):
    test.append(next_action(15))

#==============================================================================
# for i in xrange(10):
#     next_action(15)
#==============================================================================
