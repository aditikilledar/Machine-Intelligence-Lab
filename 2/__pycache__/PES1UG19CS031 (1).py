"""
You can create any other helper funtions.
Do not modify the given functions
"""

import numpy as np
# from Collections import deque

def A_star_Traversal(cost, heuristic, start_point, goals):
    """
    Perform A* Traversal and find the optimal path 
    Args:
        cost: cost matrix (list of floats/int)
        heuristic: heuristics for A* (list of floats/int)
        start_point: Staring node (int)
        goals: Goal states (list of ints)
    Returns:
        path: path to goal state obtained from A*(list of ints)
    """
    path = []
    # TODO
    
 
    
    return path


def DFS_Traversal(cost, start_point, goals):
    """
    Perform DFS Traversal and find the optimal path 
    cost: cost matrix (list of floats/int)
    start_point: Staring node (int)
    goals: Goal states (list of ints)
    Returns:
    path: path to goal state obtained from DFS(list of ints)
    """
    path = []
    # TODO
    """  
    create frontier
    create expanded list
    push root into frontier
    
    while True:
    pop node from frontier
    if already expanded
    ignore
    if goal
    exit
    else
    expand node
    push expanded node to frontier
    
    """
    # frontier = deque()
    frontier = []
    frontier.append(start_point)
    expanded = []
    
    success = 0
    
    npCost = np.array(cost)
    
    while True and success!=1:
        print('frontier ', frontier)
        ele = frontier.pop(0)
        print(ele, ' popped')

        if ele in goals:
            print('Goal reached!')
            success = 1
            exit
        
        print('expanded ', expanded)
        
        if ele in expanded:
            pass
        else:
            expanded.append(ele)
            for j in range(1, npCost.shape[1]):
                if (cost[ele][j] != -1) and (cost[ele][j] != 0) and (j not in frontier):
                    frontier.append(j)
            print('now expanding ', ele)
            # path.append(ele)
            print('expanded ', expanded)
            
                

    return path

## remove later   
cost = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 5, 9, -1, 6, -1, -1, -1, -1, -1],
            [0, -1, 0, 3, -1, -1, 9, -1, -1, -1, -1],
            [0, -1, 2, 0, 1, -1, -1, -1, -1, -1, -1],
            [0, 6, -1, -1, 0, -1, -1, 5, 7, -1, -1],
            [0, -1, -1, -1, 2, 0, -1, -1, -1, 2, -1],
            [0, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1],
            [0, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1],
            [0, -1, -1, -1, -1, 2, -1, -1, 0, -1, 8],
            [0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 7],
            [0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0]]

heuristic = [0, 5, 7, 3, 4, 6, 0, 0, 6, 5, 0]
start = 1
goals = [6, 7, 10]

try:
    if DFS_Traversal(cost,start, goals)==[1, 2, 3, 4, 7]:
        print("Test Case 2 for DFS Traversal PASSED")
    else:
        print("Test Case 2 for DFS Traversal FAILED")
except Exception as e:
    print("Test Case 2 for DFS Traversal FAILED due to ",e)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
