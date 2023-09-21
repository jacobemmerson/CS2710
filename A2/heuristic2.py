#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 18:32:46 2019

@author: milos
"""

# a heuristic function for the 'current' state and the target state
# currently returns 0 (no heuristics used)
def h_function(state,target_state):
    total_man_dist = 0

    for n in state:
        x = (n-1) // 3 # x of true pos
        y = (n-1) % 3 # y of true pos
        n_index = state.index(n)
        curr_x = (n_index) // 3
        curr_y = (n_index) % 3
        total_man_dist += (abs(curr_x - x) + abs(curr_y - y))

    return total_man_dist