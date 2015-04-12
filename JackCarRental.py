# -*- coding: utf-8 -*-
"""
Created on Sat Apr 04 19:27:07 2015

@author: oromi_000, inspired by waxworskmath's MATLAB code

Formulation of Jack's Car Rental Problem as MDP
Time step: 1 day
state: # of cars at each location
action: # of cars moved between two locations A and B overnight
"""

# Library imports
import numpy as np

# Constants
lambdareq1 = 3
lambdareq2 = 4
lambdaret1 = 3
lambdaret2 = 2

max_cars = 20
max_transfer = 5
gamma = 0.9

# Initial state
v = np.zeros([max_cars,max_cars])

# Policy evaluation


# Policy improvement