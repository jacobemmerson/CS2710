#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:01:00 2019
vanilla breadth first search
- relies on  Puzzle8.py module

@author: milos
"""

from Puzzle8 import *


 #### ++++++++++++++++++++++++++++++++++++++++++++++++++++
 #### breadth first search         
        

def depth_first_search_limit(problem, limit):
    n_expanded = 0
    n_generated = 0
    queue_len = 0
    path_len = 0
    found = 0
    queue =deque([])
    root=TreeNode(problem,problem.initial_state)
    queue.append(root) # push initial state in queue
    best_pathes = HashTable()

    while len(queue)>0:
        if len(queue) > queue_len:
            queue_len = len(queue) # finds max queue length

        next=queue.pop()
        if next.g >= limit:
            continue
        
        n_expanded += 1 # popping indicates expansion
        path_len = len(next.path())

        if best_pathes.in_hashp(next.state): # if node in ht
            if best_pathes.get_hash_value(next.state) > path_len: # if shorter path, update path len
                best_pathes.add_hash(item = next.state, value = len(next.path()))
            else:
                continue # otherwise skip this node
        else:  # add if not in table
            best_pathes.add_hash(item = next.state, value = len(next.path()))

        if next.goalp(): 
            found = True # have we found a single goal condition?
            found = next # assign to the node; if a worse path to the goal is found again it will not reach this point

        # continue searching bc DFS may not return best sol
        new_nodes=next.generate_new_tree_nodes() 
        n_generated += len(new_nodes) # generate_new_tree_nodes -> lst[], 
        for new_node in new_nodes:
            queue.append(new_node)  
                       
    if found: 
        return {
            'path' : found.path(),
            'Nodes Expanded' : n_expanded,
            'Nodes Generated' : n_generated,
            'Max Queue Length' : queue_len,
            'Path Length' : len(found.path())
        }
    else: 
        print('No solution')
    return NULL
  
problem=Puzzle8_Problem(Example1) 
output=  depth_first_search_limit(problem, 10)
if output != NULL:
    print('Solution Example 1:')
    for k,v in output.items():
        if k == 'path': continue

        print(f"{k}: {v}")

    print_path(output['path'])

wait = input("PRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example2) 
output=  depth_first_search_limit(problem, 10)
if output != NULL:
    print('Solution Example 2:')
    for k,v in output.items():
        if k == 'path': continue

        print(f"{k}: {v}")

    print_path(output['path'])

wait = input("PRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example3) 
output=  depth_first_search_limit(problem, 10)
if output != NULL:
    print('Solution Example 3:')
    for k,v in output.items():
        if k == 'path': continue

        print(f"{k}: {v}")

    print_path(output['path'])

wait = input("PRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example4) 
output=  depth_first_search_limit(problem, 10)
if output != NULL:
    print('Solution Example 4:')
    for k,v in output.items():
        if k == 'path': continue

        print(f"{k}: {v}")

    print_path(output['path'])

wait = input("PRESS ENTER TO CONTINUE.")

# Solution to Example 5 may take too long to calculate using vanilla bfs
output=  depth_first_search_limit(problem, 10)
if output != NULL:
    print('Solution Example 5:')
    for k,v in output.items():
        if k == 'path': continue

        print(f"{k}: {v}")

    print_path(output['path'])
 