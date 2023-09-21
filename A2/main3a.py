from Puzzle8 import *

def print_solution(output):
    print('Solution:')
    
    for k,v in output.items():
        if k == 'path':
            continue
        print(f"{k} = {v}")

    print_path(output['path'])
    print('\n')

def eval_function_driven_search(problem):
     queue = Priority_Queue()
     root=TreeNode(problem,problem.initial_state)
     queue.add_to_queue(root)
     nodes_gen = 0
     nodes_exp = 0
     queue_len = 0
     solution_len = 0

     while (queue.is_empty() == False):
         if len(queue.queue) > queue_len: # update max queue
            queue_len = len(queue.queue)

         next=queue.pop_queue()
         nodes_exp += 1 # node popped
         if next.goalp():
             del(queue)
             solution_len = len(next.path())
             return {
                "path" : next.path(),
                "Nodes Generated" : nodes_gen,
                "Nodes Expanded" : nodes_exp,
                "Max Queue Length" : queue_len,
                "Solution Length" : solution_len
             }
         else:
             new_nodes=next.generate_new_tree_nodes() # returns list of nodes
             nodes_gen += len(new_nodes) # len(new nodes) = nodes generated
             for new_node in new_nodes:
                  queue.add_to_queue(new_node)         
     print('No solution')
     return NULL

problem=Puzzle8_Problem(Example1) 
output=  eval_function_driven_search(problem)
print_solution(output)

problem=Puzzle8_Problem(Example2) 
output=  eval_function_driven_search(problem)
print_solution(output)

problem=Puzzle8_Problem(Example3) 
output=  eval_function_driven_search(problem)
print_solution(output)