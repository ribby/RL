# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:28:09 2015

@author: oromi_000

KNOWN BUGS:
* epsilon should be revalued. Currently messy for use in next_action()
* hardcoded a range in next_state
* yet to implement first-visit business
* need to deal with repetition in next_action
* in next_action, I only remove one optimal action. Instead I should be removing all optimal actions
"""

import numpy as np

# Define Q-learning specific constants
gamma = 1
epsilon = 0.001 # Epsilon effectively equals 0.1%,
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
number_to_direction = {0: '<', 1: '>', 2: '^', 3: 'v'}
direction_to_number = {v: k for k, v in number_to_direction.items()} # {'<':0, '>':1 ...}


def next_action(state):
    '''
    Determines the [value_of_the_next_action, and direction_of_next_action] 
    using epsilon greedy methods.
    '''
    global epsilon
    global Q
    max_action = max(Q[state])
    if np.random.random() > epsilon: # greedy action
        if list(Q[state]).count(max_action) != 1: # If there is more that one max in Q[state]
            indices = [i for i, x in enumerate(list(Q[state])) if x == max_action]        
            return [max_action, number_to_direction[indices[np.random.randint(0,len(indices))]]] # randomly pick one of those maximums          
        else: # Single maxima
            return [max_action, number_to_direction[np.argmax(Q[state])]]
    else: # simplified exploration, will sometimes cause exploration to move in direction of maximum
        return [max_action, number_to_direction[np.random.randint(0,4)]]

#==============================================================================
# Q[25] = np.array([-2, -1, -4, -3])
# test = []
# print next_action(25)
# for i in xrange(10000):
#     test.append(next_action(25)[1])
# print "The amount of left is", test.count('<')
# print "The amount of right is", test.count('>')
# print "The amount of up is", test.count('^')
# print "The amount of down is", test.count('v')
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
    global terminal_state
    if state == terminal_state:
        return 0
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
    else:
        return -1

#==============================================================================
# for i in xrange(0,47):
#     print "State:", i, "Direction: down Reward:", reward(i, 'v')
#==============================================================================


def update_Q(state):
    '''
    Updates one entry in Q, and returns the next state
    '''
    global Q
    global cliff
    global gamma
    global alpha
    global terminal_state
    [value,direction] = next_action(state)
    if state == terminal_state:
        Q[state][direction_to_number[direction]] = 0
        return terminal_state
    else:
        Q[state][direction_to_number[direction]] += alpha*(reward(state, direction) + gamma*next_action(state)[0] - Q[state][direction_to_number[direction]])
#        print "The current state, direction pair is,", state, direction
#        print "The next state is", next_state(state,direction)
        return next_state(state,direction) # THIS MIGHT BE UNNECESSARY

# Every time I run updateQ, Q is updated AND a direction is returned

#==============================================================================
# z = 47
# print "The next state is:", update_Q(z)
# print "\n"
# print Q[z]
#==============================================================================

#==============================================================================
# print Q
# for i in xrange(5):
#     q = update_Q(5) # Just assigning the variable will update q
# print "\n"
# print Q
#==============================================================================

def main(maxEpisodes):
    global Q
    global start_state
    global terminal_state
    nEpisodes = 0
    maxVisits = 1000
    while nEpisodes < maxEpisodes:
        nVisits = 0
        next_state = update_Q(start_state)
        while next_state != terminal_state and nVisits < maxVisits:
            next_state = update_Q(next_state)
            nVisits += 1
        print "The number of visits was", nVisits
        nEpisodes += 1
        
main(1)

#==============================================================================
# def main(maxEpisodes):
#     global Q
#     global start_state
#     global terminal_state
#     nEpisodes = 0
#     maxVisits = 100
#     while nEpisodes < maxEpisodes:
#         nVisits = 0
# #        print "The starting state is:", start_state
#         state = update_Q(start_state)
#         direction = next_action(state)[1]
#         while state != terminal_state and nVisits < maxVisits:
#             state = next_state(state,direction)
#             update_Q(state)
#             nVisits += 1
#         print "The number of visits was", nVisits
#==============================================================================
#        nEpisodes += 1

#main(1)

#==============================================================================
# new_state = update_Q(start_state,Q)
# for i in xrange(5):
#     update_Q(new_state,Q)
#==============================================================================



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
# print Q[22][direction_to_number['>']]
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
