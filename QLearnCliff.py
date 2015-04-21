# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:28:09 2015

@author: oromi_000

KNOWN BUGS:
* first value in graph is arbitrary
* hardcoded a range in next_state
* yet to implement first-visit business
* need to deal with repetition in next_action
* in next_action, I only remove one optimal action. Instead I should be removing all optimal actions
"""

import numpy as np
import matplotlib.pyplot as plt

# Define Q-learning specific constants. Can mess with these to change plot shape.
gamma = 1
epsilon = 0.1       # ~10% of action is exploration
maxEpisodes = 100
alpha = 0.01        # Played with values. 0.1 will return ballpark -50
stopping = 1e-3

# Initializing the number of actions. Assuming same number of actions for all states
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
        
# Define cliff states and direction dicts (to be used when taking actions)
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
    max_action_value = max(Q[state])
    if np.random.random() > epsilon: # greedy action
        if list(Q[state]).count(max_action_value) != 1: # If there is more that one max in Q[state]
            indices = [i for i, x in enumerate(list(Q[state])) if x == max_action_value]        
            return [max_action_value, number_to_direction[indices[np.random.randint(0,len(indices))]]] # randomly pick one of those maximums          
        else: # Single maxima
            return [max_action_value, number_to_direction[np.argmax(Q[state])]]
    else: # simplified exploration, will sometimes cause exploration to move in direction of maximum
        return [max_action_value, number_to_direction[np.random.randint(0,4)]]


def next_state(state, direction):
    '''
    Helper function to be used in defining the next state in update_Q.
    Returns the number of the next state. Direction is an arrow.
    '''
    global grid
    global start_state
    if state in range(25,35):   # Above cliff
        if direction == 'v':
            return start_state
    if state == 36:             # Left of cliff
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


def update_Q(state, direction, state_prime, action_prime):
    '''
    Updates one entry in Q, and returns the next state. Direction is an arrow.
    '''
    global Q
    global cliff
    global gamma
    global alpha
    global terminal_state
    if state == terminal_state:
        Q[state][direction_to_number[direction]] = 0
        return terminal_state
    else:
        Q[state][direction_to_number[direction]] += \
            alpha*(reward(state, direction) + \
            + gamma*Q[state_prime][direction_to_number[action_prime]] + \
            - Q[state][direction_to_number[direction]])
        return


def main(maxEpisodes):
    global Q
    global start_state
    global terminal_state
    global temp
    nEpisodes = 0
    reward_list = []
    diff_list = [-50]   # First value chosen for nice plotting. Doesn't effect path.
    while nEpisodes < maxEpisodes:
        episode_reward = 0
        state = start_state
        action = next_action(start_state)[1]
        state_prime = next_state(state, action)
        action_prime = next_action(state_prime)[1]
        update_Q(state,action, state_prime, action_prime)
        while state != terminal_state:
            state = state_prime
            action = next_action(state)[1]
            state_prime = next_state(state, action)
            action_prime = next_action(state_prime)[1]
            update_Q(state,action, state_prime, action_prime)
        # Plotting the reward per episode
        for i in xrange(nStates-1):     
            for j in xrange(nActions):
                episode_reward += Q[i][j]
        nEpisodes += 1
        reward_list.append(episode_reward)
    for i in xrange(len(reward_list)-1):
        diff_list.append(reward_list[i+1] - reward_list[i])
    plt.plot(range(0, maxEpisodes), diff_list)
    plt.ylabel("Reward per episode")
    plt.xlabel("Episode")
    plt.show()
    
    
main(250)  # 2500, ep = 0.1, alp = 0.01  returns 2nd row as optimal path

# Prints out optimal direction of travel

direction_matrix = np.empty(nStates,str)
for i in xrange(nStates):
    direction_matrix[i] = number_to_direction[np.argmax(Q[i])]
direction_matrix = direction_matrix.reshape(HEIGHT, WIDTH)
print direction_matrix
    