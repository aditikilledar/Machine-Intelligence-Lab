
"""
You can create any other helper funtions.
Do not modify the given functions
"""

import collections
# from Collections import deque
class Node:
    def __init__(self, state, parent, cost):
        self.cost = cost # path cost till now
        self.parent = parent # who its parents are
        self.state = state # aka its value rn

        self.parentcost = (self.parent, self.cost)

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

    # state, path cost, parent, action
    # frontier = []
    frontier = collections.deque()
    expanded = [False] * len(cost)
    print(expanded)

    ele = Node(start_point, [], 0)

    frontier.append(ele)

    # TEST
    child = Node(99, 22, 44)
    print("TEST: parentcost", child.parentcost)
    # END TEST

    parents = {key: [] for key in range(1, len(cost))}
    print(parents)

    for each in frontier:
                print("AAAAAAA (state, parent)",each.state, each.parent)

    while True:
        if len(frontier) == 0:
            print("No solution")
            return []

        # remove node from top of stack
        # top = frontier.pop(0)
        top = frontier.pop()
        print("TOP: ",top.state)

        value = top.state
        print(value, 'expanded?', expanded[value])
        if not expanded[value]:
            # expand node if not already expanded
            expanded[value] = True
            # add largest ele in stack first
            for j in reversed(range(1, len(cost))):
                # print("j", j)
                if (not expanded[j]) and (cost[value][j] != 0) and (cost[value][j] != -1): 
                    # frontier.insert(0, Node(j, [], 0))
                    frontier.append(Node(j, [], 0))
                    # parents[j].append(value)
                    parents[j] = value
                    # print("parent added to",j,":", parents)

            # print frontier
            # for each in frontier:
            #     print("(state, parent)",each.state, each.parent, end = " ")


        if top.state in goals:
            print("Soln found!!!!!!!!!!!!!!")
            break        

    #PROBLEM: need to do smn so that it picks smaller parent first !!!!!!!!! time to sleep, good job Aditi :)

    # goal reached
    v = top.state
    tempath = []
    path.append(v)
    # add parent of top into tempath until start_point is added, then reverse tempath and quit
    while v != start_point:
        path.append(parents[v])
        print(path)
        v=parents[v]
        
    print(path)
    path.reverse()
    print(path)

    if not path:
        print("PATH Is EMPTY $$$$$$$$")

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

# DFS_Traversal([],start, goals)