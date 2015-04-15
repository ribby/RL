# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:28:09 2015

@author: oromi_000

KNOWN BUGS:
* epsilon should be revalued. Currently messy for use in next_action()
* the way I deal with repeated state-value pairs in next_state() can be improved
"""

import numpy as np

# Define Q-learning specific constants
gamma = 1
epsilon = 100 # Epsilon effectively equals 0.1%,
maxEpisodes = 100
alpha = 0.1
stopping = 1e-3

# Initializing the number of actions. Assuming same number of actions for all state
nActions = 4
action = np.zeros(nActions,)
    
# Define grid size
HEIGHT = 4
WIDTH = 12
nStates = HEIGHT * WIDTH

# Initializing the action-value function
grid = np.arange(nStates).reshape([HEIGHT,WIDTH]) # Assigns a number to each state
Q = {}
for i in grid:
    for j in i:
        Q[j] = action.copy()
        
# Define terminal states and directions (to be used when changing states)
terminal = [37, 38, 39, 40, 41, 42, 43, 44, 45, 46]
direction = {0: '<', 1: '>', 2: '^', 3: 'v'}
inv_direction = {v: k for k, v in direction.items()}

def reward():
    return -1

def all_next_states(state):
    '''
    Returns all possible next states in the form [left,right,up,down]
    '''
    global grid
    all_next_states = []
    # Left
    if state in grid[:,0]:
        all_next_states.append(state)
    else:
        all_next_states.append(state-1)
    # Right
    if state in grid[:,-1]:
        all_next_states.append(state)
    else:
        all_next_states.append(state+1)
    # Up
    if state in grid[0]:
        all_next_states.append(state)
    else:
        all_next_states.append(state-len(grid[0]))
    # Down
    if state in grid[-1]:
        all_next_states.append(state)
    else:
        all_next_states.append(state+len(grid[0]))
    return all_next_states

def next_action(state):
    '''
    Determines the [value_of_the_next_action, and direction_of_next_action] 
    using epsilon greedy methods. The way I deal with state-value repetition
    still needs to be improved.
    '''
    global epsilon
    max_action_per_state = []
    next_state = all_next_states(state)
    for state in next_state:
        max_action_per_state.append(max(Q[state])) # left, right, up, down
    max_action = max(max_action_per_state) 
    if max_action_per_state.count(max_action) != 1: # If any sort of repetition in state-value pair
        return [max_action, direction[np.random.randint(0,4)]] # pick a completely random direction (super grungy)
    for_direction = max_action_per_state[:] # to be used in else clause for direction
    if np.random.randint(0,100000) > epsilon: # greedy action
        return [max_action, direction[max_action_per_state.index(max_action)]]
    else: # exploration
        max_action_per_state.remove(max_action)
        non_optimal_action = max_action_per_state[np.random.randint(0,3)]
        return [non_optimal_action, direction[for_direction.index(non_optimal_action)]]
        
def next_state(state, direction):
    '''
    Helper function to be used in defining the next state in update_Q.
    Returns the number of the next state.
    '''
    global grid
    if direction == '<':
        if state in grid[:,0]:
            return state
        else:
            return state - 1
    if direction == '>':
        if state in grid[:,-1]:
            return state
        else:
            return state + 1
    if direction == '^':
        if state in grid[0]:
            return state
        else:
            return state - len(grid[0])
    if direction == 'v':
        if state in grid[-1]:
            return state
        else:
            return state + len(grid[0])

def update_Q(state,Q):
    global terminal
    global gamma
    global alpha
    if state in terminal:
        Q[state][inv_direction[next_action(state)[1]]] = 0
        return "Done updating!"
    else:
        Q[state][inv_direction[next_action(state)[1]]] += alpha*(reward() + gamma*next_action(state)[0] - Q[state][inv_direction[next_action(state)[1]]])
    return next_state(state,next_action(state)[1])

def update_Q(state,Q):
    global terminal
    global gamma
    global alpha
    if state in terminal:
        Q[state][inv_direction[next_action(state)[1]]] = 0
    else:
        Q[state][inv_direction[next_action(state)[1]]] += alpha*(reward() + gamma*next_action(state)[0] - Q[state][inv_direction[next_action(state)[1]]])
    return next_state(state,next_action(state)[1])

following = update_Q(start_state,Q)
for i in xrange(10):
    following = update_Q(following,Q)
#==============================================================================
# Q[22][1] = 5
# print Q[22][inv_direction['>']]
#==============================================================================
        
        
#==============================================================================
# print Q[14]
# Q[14][0] = 7
# Q[3][2] = 10
# Q[16][3] = 5
# print Q[14]
# test = []
# for i in xrange(10000):
#     test.append(next_action(15))
#==============================================================================
