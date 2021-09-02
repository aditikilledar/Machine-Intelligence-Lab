"""
You can create any other helper funtions.
Do not modify the given functions
"""

import numpy as np
import collections

class Node:
    def __init__(self, state, parent, cost):
        self.cost = 0 # path cost till now
        self.parent = [] # who its parents are
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
