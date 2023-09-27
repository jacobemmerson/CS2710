#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Name: Jacob Emmerson
CS2710 Assignment 3

This script demonstrates simulated annealing with a linear cooling schedule.
'''

from TSP import *

def adjust_temp_linear(init_temp, no_of_steps, current_step):
    if current_step == 0:
        return init_temp
    
    k = no_of_steps
    i = current_step
    adj_temp = (init_temp / k) * (k - i)

    return adj_temp

def compute_probability(energy_diff, temp):
    return math.e ** (energy_diff / temp)

def sim_anneal(TSP_problem, no_of_steps, init_temperature):

    problem = TSP_problem
    curr_E = 0 # objective function (energy) : manhattan distance
    temp = init_temperature
    accepted_tours = 0
    tried_tours = 0
    best_tour = []
    best_E = 0

    current = problem.generate_random_tour() # random start
    curr_E = problem.evaluate_tour(current) 

    init_tour = current
    init_E = curr_E
    for s in range(no_of_steps):
        candidate = problem.permute_tour(tour = current) # attach opposites
        cand_E = problem.evaluate_tour(candidate)
        tried_tours += 1 

        d_E = cand_E - curr_E # energy difference; d_E < 0 indicates lower total man. dist.
        if d_E < 0: # update best
            accepted_tours += 1
            current = candidate
            curr_E = cand_E
            best_tour = candidate
            best_E = curr_E

        else: # otherwise use prob 
            prob = compute_probability(-d_E, temp) # negate energy diff so p in [0,1]

            if random.random() <= prob: # accept but don't update best... prob -> 0, progressively accept less
                accepted_tours += 1
                current = candidate
                curr_E = cand_E

        # update temp from steps
        temp = adjust_temp_linear(init_temp = init_temperature, 
                           no_of_steps = no_of_steps + 1, 
                           current_step = s)

    return {
        'Initial Tour' : init_tour,
        'Initial Distance' : init_E,
        'Initial Temperature' : init_temperature,
        'Tours Tried' : tried_tours,
        'Tours Accepted' : accepted_tours,
        'Best Tour' : best_tour,
        'Best Distance' : best_E
    }

print("\nsalesman is traveling...")
problem = TSP_Problem(Standard_Cities)
s = sim_anneal(TSP_problem = problem, no_of_steps = 300000, init_temperature = 40)

print('-'*20)
for k,v in s.items():
    print(f"{k} = {v}")
print('-'*20)