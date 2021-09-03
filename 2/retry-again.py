"""
You can create any other helper funtions.
Do not modify the given functions
"""

import numpy as np
import collections

class Node:
    def __init__(self, state, parent, cost):
        self.cost = cost # path cost till now
        self.parent = parent # who its parents are
        self.state = state # aka its value rn

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
    if not cost or not start_point or not goals or (start_point>(len(cost)-1)):
        return []

    frontier = collections.deque()
    expanded = [False] * len(cost)
    # print(expanded)

    ele = Node(start_point, [], 0)

    frontier.append(ele)

    parents = {key: [] for key in range(1, len(cost))}
    # print(parents)

    while True:
        if len(frontier) == 0:
            # print("No solution")
            return []

        # remove node from top of stack
        top = frontier.pop()

        value = top.state
        if not expanded[value]:
            # expand node if not already expanded
            expanded[value] = True
            # add largest ele in stack first
            for j in reversed(range(1, len(cost))):
                # print("j", j)
                if (not expanded[j]) and (cost[value][j] != 0) and (cost[value][j] != -1): 
                    frontier.append(Node(j, [], 0))
                    parents[j] = value

        if top.state in goals:
            break        

    #PROBLEM: need to do smn so that it picks smaller parent first !!!!!!!!! time to sleep, good job Aditi :)

    # goal reached
    v = top.state
    tempath = []
    path.append(v)
    # add parent of top into tempath until start_point is added, then reverse tempath and quit
    while v != start_point:
        path.append(parents[v])
        v=parents[v]
        
    path.reverse()

    return path

# remove later   
cost = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 5, 9, -1, 6, -1, -1, -1, -1, -1],
            [0, -1, 0, 3, -1, -1, 9, -1, -1, -1, -1],
            [0, -1, 2, 0, 1, -1, -1, -1, -1, -1, -1],
            [0, 6, -1, -1, 0, -1, -1, 5, 7, -1, -1],
            [0, 1, -1, -1, 2, 0, -1, -1, -1, 2, -1],
            [0, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1],
            [0, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1],
            [0, -1, -1, -1, -1, 2, -1, -1, 0, -1, 8],
            [0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 7],
            [0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0]]

heuristic = [0, 5, 7, 3, 4, 6, 0, 0, 6, 5, 0]
start = 1

goals = [6, 7, 10]
# goals = [6]

try:
    if DFS_Traversal(cost,start, goals)==[1, 2, 3, 4, 7]:
    # if DFS_Traversal(cost,start, goals)==[]:
        print("Test Case 2 for DFS Traversal PASSED")
    else:
        print("Test Case 2 for DFS Traversal FAILED")
except Exception as e:
    print("Test Case 2 for DFS Traversal FAILED due to ",e)
