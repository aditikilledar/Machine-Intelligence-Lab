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

# HEAP FUNCTIONS
# MinHeap:

def heapify(arr, size, pos):
    # single element or no elements
    if size == 1 or size == 0:
        return

    smallest = pos
    leftindex = 2*pos+1
    rightindex = 2*pos+2

    if leftindex < size and arr[leftindex].cost < arr[smallest].cost and leftindex > 0:
        smallest = leftindex

    if rightindex < size and arr[rightindex].cost < arr[smallest].cost and rightindex > 0:
        smallest = rightindex 

    if smallest != pos:
        #swap smallest and pos !!!!! check if works or else change
        arr[pos], arr[smallest] = arr[smallest], arr[pos]
        heapify(arr, size, smallest)

def makeMinHeap(arr, size):
    start = (size//2)-1

    if start < 0:
        return

    for i in range(start, -1, -1):
        heapify(arr, size, i)

def addNode(arr, ele):
    size = len(arr)
    # print("child added ", ele.cost)
    if not size:
        arr.append(ele)
    else:
        lastparent = size//2
        arr.append(ele)
        makeMinHeap(arr, len(arr))    

def popMin(arr):
    # root has minimum
    root = arr[0]
    size = len(arr)

    # replace root with last one 
    arr[0] = arr[size-1]
    popd = arr.pop() #remove last element in the list

    size = len(arr)
    # make into a heap
    lastparent = size//2
    heapify(arr, size, 0)

    return root

def makepath(camefrom, node):
    fullpath = [node]

    while node in camefrom.keys():
        node = camefrom[node]
        fullpath.insert(0, node)

    return fullpath

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

    # cost function for start_point
    startcost = heuristic[start_point]
    start = Node(start_point, start_point, startcost)

    goalDist = {key: float('inf') for key in goals}

    frontier = [start]
    expanded = [False]*len(cost)

    camefrom = {}
    #  g(n) for each node n
    pathtillnow = {key: float('inf') for key in range(1, len(cost))}
    pathtillnow[start_point] = 0

    while len(frontier):
        # if len(frontier) == 0: # no path
        #     break

        popped = frontier[0]

        if popped.state in goals:
            # print("GOAL REACHED")
            return makepath(camefrom, popped.state)

        popMin(frontier)

        if not expanded[popped.state]:
            #  expand it
            expanded[popped.state] = True

            for j in range(1, len(cost)):
                if(cost[popped.state][j] != -1 and popped.state != j):
                    # set parents to popped.state
                    parent = popped.state

                    Gvalue = pathtillnow[parent] + cost[parent][j]

                    if Gvalue < pathtillnow[j]:
                        # found a better path for j
                        camefrom[j] = popped.state
                        pathtillnow[j] = Gvalue
                        Fcost = (Gvalue) + heuristic[j]

                        child = Node(j, parent, Fcost)
                        
                        # very important part
                        if child not in frontier:
                            child = Node(j, parent, Fcost)
                            addNode(frontier, child)

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

    ele = Node(start_point, [], 0)

    frontier.append(ele)

    parents = {key: [] for key in range(1, len(cost))}

    while True:
        if len(frontier) == 0:
            return []

        # remove node from top of stack
        top = frontier.pop()

        value = top.state
        if not expanded[value]:
            # expand node if not already expanded
            expanded[value] = True
            # add largest ele in stack first
            for j in reversed(range(1, len(cost))):
                if (not expanded[j]) and (cost[value][j] != 0) and (cost[value][j] != -1): 
                    frontier.append(Node(j, [], 0))
                    parents[j] = value

        if top.state in goals:
            break        

    # goal reached
    v = top.state
    path.append(v)
    while v != start_point:
        path.append(parents[v])
        v=parents[v]    
    path.reverse()

    return path