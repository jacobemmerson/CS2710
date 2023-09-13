#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:01:00 2019
vanilla breadth first search
- relies on  Puzzle8.py module

@author: milos
"""

from Puzzle8 import *
   
def check_cyclic_repeats(node):
    stop = len(node.path()) - 1
    for n in node.path()[:stop]:
        if n.state == node.state:
            return True
        
    return False

def breadth_first_search_cycles(problem):
    n_expanded = 0
    n_generated = 0
    queue_len = 0
    path_len = 0
    queue =deque([])
    root=TreeNode(problem,problem.initial_state)
    queue.append(root) # push initial state in queue
    while len(queue)>0:
        if len(queue) > queue_len:
            queue_len = len(queue) # finds max queue length

        next=queue.popleft()
        if check_cyclic_repeats(next):
            continue

        n_expanded += 1 # popping indicates expansion if it does not induce a cycle
        if next.goalp(): # does the current state satisfy the goal condition? (defined by TreeNode)
            del(queue) 
            path_len = len(next.path())
            return {
                'path' : next.path(),
                'Nodes Expanded' : n_expanded,
                'Nodes Generated' : n_generated,
                'Max Queue Length' : queue_len,
                'Path Length' : path_len
            }
        else:
            new_nodes=next.generate_new_tree_nodes() 
            n_generated += len(new_nodes) # generate_new_tree_nodes -> lst[], 
            for new_node in new_nodes:
                queue.append(new_node)         
    print('No solution')
    return NULL

problem=Puzzle8_Problem(Example1) 
output=  breadth_first_search_cycles(problem)
print('Solution Example 1:')
for k,v in output.items():
    if k == 'path': continue
    
    print(f"{k}: {v}")

print_path(output['path'])

wait = input("PRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example2) 
output=  breadth_first_search_cycles(problem)
print('Solution Example 2:')
for k,v in output.items():
    if k == 'path': continue
    
    print(f"{k}: {v}")

print_path(output['path'])

wait = input("PRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example3) 
output=  breadth_first_search_cycles(problem)
print('Solution Example 3:')
for k,v in output.items():
    if k == 'path': continue
    
    print(f"{k}: {v}")

print_path(output['path'])

wait = input("PRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example4) 
output=  breadth_first_search_cycles(problem)
print('Solution Example 4:')
for k,v in output.items():
    if k == 'path': continue
    
    print(f"{k}: {v}")

print_path(output['path'])

wait = input("PRESS ENTER TO CONTINUE.")

# Solution to Example 5 may take too long to calculate using vanilla bfs
problem=Puzzle8_Problem(Example5) 
output=  breadth_first_search_cycles(problem)
print('Solution Example 5:')
for k,v in output.items():
    if k == 'path': continue
    
    print(f"{k}: {v}")

print_path(output['path'])