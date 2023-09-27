#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Name: Jacob Emmerson
CS2710 Assignment 3

This script demonstrates simulated annealing with a logit cooling schedule.
'''

from TSP import *

def compute_probability(energy_diff, temp):
    return math.e ** (energy_diff / temp)

def adjust_temp_logit(init_temp, no_of_steps, current_step, params = {'slope' : -1/5000, 'mid_adj' : 0}):
    k = no_of_steps
    i = current_step
    C = 1/10000 # prevents float div by 0

    beta = -params['slope'] * 4
    alpha = -(((k/2) + params['mid_adj']) * beta)
    s = alpha + beta * i

    adj_temp = (1 / (1 + math.e**(-s))) * init_temp

    return (init_temp - adj_temp) + C

def sim_anneal_logit(TSP_problem, no_of_steps, init_temperature, temp_params = {
                                                                                    'slope' : -1/20000,
                                                                                    'mid_adj' : 0
                                                                                }):

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
        temp = adjust_temp_logit(
                            init_temp = init_temperature, 
                            no_of_steps = no_of_steps + 1, 
                            current_step = s,
                            params = temp_params
                           )

    return {
        'Initial Tour' : init_tour,
        'Initial Distance' : init_E,
        'Initial Temperature' : init_temperature,
        'Tours Tried' : tried_tours,
        'Tours Accepted' : accepted_tours,
        'Best Tour' : best_tour,
        'Best Distance' : best_E
    }


def _main():
    tours = []
    problem = TSP_Problem(Standard_Cities)

    for t in range(10):
        print(f"\nsalesman {t} is traveling...")
        tour = sim_anneal_logit(TSP_problem = problem, no_of_steps = 20000, init_temperature = 100,
                                temp_params={'slope' : -1/1000, 'mid_adj' : -2500})  # max(slope) = slope
                                                                                        # d2/dx(slope) = 0 @ x = (no_of_steps / 2) + mid_adj
        tours.append(tour['Best Distance'])
        print('-'*20)
        for k,v in tour.items():
            print(f"{k} = {v}")
        print('-'*20)

    print('\n'*3)
    print(f"best distances {[round(n,2) for n in tours]}")
    print(f"tours mean best dist. = {sum(tours)/len(tours)}")

_main()