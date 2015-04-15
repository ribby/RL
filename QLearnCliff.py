# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:28:09 2015

@author: oromi_000

KNOWN BUGS:
* epsilon should be revalued. Currently messy for use in next_action()
* hardcoded a range in next_state
* yet to implement first-visit business
* need to deal with repetition in next_action
"""

import numpy as np

# Define Q-learning specific constants
gamma = 1
epsilon = 100 # Epsilon effectively equals 0.1%,
maxEpisodes = 100
alpha = 0.5
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
        
# Define cliff states and directions (to be used when changing states)
start_state = 36
terminal_state = 47
cliff = [37, 38, 39, 40, 41, 42, 43, 44, 45, 46]
direction = {0: '<', 1: '>', 2: '^', 3: 'v'}
inv_direction = {v: k for k, v in direction.items()}



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

def next_action(state, Q):
    '''
    Determines the [value_of_the_next_action, and direction_of_next_action] 
    using epsilon greedy methods.
    '''
    global epsilon
#    global Q
    max_action = max(Q[state])
    for_direction = list(Q[state][:]) # To be used in exploration
    if np.random.randint(0,100000) > epsilon: # greedy action
        if list(Q[state]).count(max_action) != 1: # If there is more that one max in Q[state]
            indices = [i for i, x in enumerate(list(Q[state])) if x == max_action]        
            return [max_action, direction[indices[np.random.randint(0,len(indices))]]] # randomly pick one of those maximums          
        else: # Single maxima
            return [max_action, direction[np.argmax(Q[state])]]
    else: # exploration
        for_direction.remove(max_action)
        non_optimal_action = for_direction[np.random.randint(0,3)]
        return [non_optimal_action, direction[for_direction.index(non_optimal_action)]]

#%%

#==============================================================================
#     max_action_per_state = []
#     possible_states = all_next_states(state)
#     for state in possible_states:
#         max_action_per_state.append(max(Q[state])) # left, right, up, down
#     max_action = max(max_action_per_state) 
#     for_direction = max_action_per_state[:] # to be used in else clause for direction
#     if np.random.randint(0,100000) > epsilon: # greedy action
#         if max_action_per_state.count(max_action) != 1: # Case with multiple maxima
#             indices = [i for i, x in enumerate(max_action_per_state) if x == max_action]        
#             return [max_action, direction[indices[np.random.randint(0,len(indices))]]] # randomly pick one of those maximums
#         else: # Single maxima
#             return [max_action, direction[max_action_per_state.index(max_action)]]
#     else: # exploration
#         max_action_per_state.remove(max_action)
#         non_optimal_action = max_action_per_state[np.random.randint(0,3)]
#         return [non_optimal_action, direction[for_direction.index(non_optimal_action)]]
#==============================================================================

#==============================================================================
# Q[37] = [-1, -1, -1, -1]
# test = []
# print next_action(36)
# for i in xrange(10000):
#     test.append(next_action(36)[1])
# print test.count('>')
#==============================================================================

def next_state(state, direction):
    '''
    Helper function to be used in defining the next state in update_Q.
    Returns the number of the next state.
    '''
    global grid
    global start_state
    if state in range(25,35):
        if direction == 'v':
            return start_state
    if state == 36:
        if direction == '>':
            return start_state
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
            
def reward(state, direction):
    global cliff
    if state == 36:
        if direction == '>':
            return -100
        else:
            return -1
    elif state in range(25,35):
        if direction == 'v':
            return -100
    else:
        return -1

def update_Q(state,Q):
    '''
    Updates one entry in Q, and returns the next state
    '''
    global cliff
    global gamma
    global alpha
    global terminal_state
    [value,direction] = next_action(state)
    if state == terminal_state:
        Q[state][inv_direction[direction]] = 0
        return "Done updating!"
    else:
        Q[state][inv_direction[direction]] += alpha*(reward(state, direction) + gamma*next_action(state)[0] - Q[state][inv_direction[direction]])
        print "The current state, direction pair is,", state, direction
        print "The next_state is", next_state(state,direction)
        return next_state(state,direction) # THIS MIGHT BE UNNECESSARY
        
        
#==============================================================================
# update_Q(36,Q)
# print Q[36]
# print reward(36, 'v')
#==============================================================================




#==============================================================================
# def main(maxEpisodes):
#     global Q
#     global start_state
#     nEpisodes = 0
#     maxVisits = 10
#     while nEpisodes < maxEpisodes:
#         nVisits = 0
#         print "The starting state is:", start_state
#         state = update_Q(start_state,Q)
#         print type(state)
#         while state != "Done updating!" and nVisits < maxVisits:
#             state = next_state(state,direction)
#             update_Q(state,Q)
#             nVisits += 1
#         print "The number of visits was", nVisits
#==============================================================================
#        nEpisodes += 1

new_state = update_Q(start_state,Q)
for i in xrange(5):
    update_Q(new_state,Q)

# main(1)


# If I run main for ~10 loops, nVisits almost never hits 500.
# As I go to ~100 loops, it shows up extremely often

#==============================================================================
# num_action = np.empty(nStates)
# visual_action = np.empty(nStates, np.dtype((str,3)))
# for i in xrange(48):
#     num_action[i] = np.argmax(Q[i])
#     visual_action[i] = direction[num_action[i]]
# visual_action = visual_action.reshape([HEIGHT,WIDTH])
# 
# QMax = np.empty(nStates)
# for i in xrange(48):
#     QMax[i] = max(Q[i])
#==============================================================================
#print QMax



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
