"""
You can create any other helper funtions.
Do not modify the given functions
"""

import collections

class Node:
    def __init__(self, state, parent, cost):
        self.cost = cost # predicted cost, f(n) = path cost + heuristic
        self.parent = parent # who its parent is
        self.state = state # aka its value rn

        # self.parentcost = (self.parent, self.cost)

# HEAP FUNCTIONS
# MinHeap:

def heapify(arr, size, pos):
    # Dont forget its for array of Node objects

    # print("inside heapify of position ", pos)
    
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

        # print("-----\nSwapped",arr[pos].state, "and ", arr[smallest].state)
        # print("inside heapify")
        # for i in arr:
        #     print(i.cost, end= " ")
        # make heapify recursively

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
    
    # print("inside add node")
    # for i in arr:
    #     print(i.cost, end= " ")

def popMin(arr):
    # root has minimum
    root = arr[0]
    size = len(arr)

    # print("size = ", size)

    # print("inside popMin")
    # for i in arr:
    #     print(i.cost, end= " ")

    # replace root with last one 
    arr[0] = arr[size-1]
    popd = arr.pop() #remove last element in the list
    # print("element popd", popd.cost)

    # print("after popd popMin")
    # for i in arr:
    #     print(i.cost, end= " ")

    size = len(arr)
    # make into a heap
    lastparent = size//2
    heapify(arr, size, 0)

    return root


    # HEAP TEST
    # a = []

    # for i in range(9, 3, -1):
    #     child = Node(i, i, i)
    #     addNode(a, child)

    # for i in a:
    #     print(i.state, end= " ")

    # for i in range(1, 4):
    #     popped = popMin(a)
    #     print("popped MINIMUM", popped.cost)

    #     print("$$$")
    #     for i in a:
    #         print(i.state, end=" ")

def updateValue(arr, name, newvalue):
    index=0
    size = len(arr)
    for ele in arr:
        if ele.state == name:
            break

    ele.cost = newvalue
    makeMinHeap(arr, size)

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
    print(frontier)
    expanded = [False]*len(cost)
    #  g(n) for each node n
    pathtillnow = {key: float('inf') for key in range(1, len(cost))}
    # pathtillnow = {key: 0 for key in range(1, len(cost))}

    pathtillnow[start_point] = 0
    print("pathtillnow", pathtillnow)

    parentof = {key: float('inf') for key in range(1, len(cost))}

    while True:
        if len(frontier) == 0: # no path
            break
            #  return []

        for ele in frontier:
            print("(", ele.state, ele.parent, ele.cost, ")")        

        popped = popMin(frontier)
        print("len=", len(frontier), " after pop of ", popped.state, "with predcost", popped.cost)
        # print(popped)

        if popped.state in goals:
            # createPath
            print("GOAL REACHED", popped.state)
            goalDist[popped.state] = pathtillnow[popped.state]

        if not expanded[popped.state]:
            #  expand it
            expanded[popped.state] = True

            for j in range(1, len(cost)):
                if(cost[popped.state][j] != -1 and popped.state != j):
                    # set parents to popped.state
                    momdad = popped.state

                    # pathtillnow[momdad] = min(pathtillnow[momdad] + cost[momdad][j], pathtillnow[j])

                    pathtillnow[j] = min(pathtillnow[momdad] + cost[momdad][j], pathtillnow[j])

                    print("f(",j,")","g + h", pathtillnow[momdad]+ cost[momdad][j]+ heuristic[j])

                    predcost = (pathtillnow[momdad] + cost[momdad][j]) + heuristic[j]

                    # give it a parent
                    parentof[j] = momdad

                    child = Node(j, momdad, predcost)
                    addNode(frontier, child)

                    # update path length till now
                    

            print("pathtillnow", pathtillnow)
            print("everyone's parents: ", parentof)


    print("!!!!!!!!!!goaldist", goalDist)
    # extract key w lowest value
    temp = min(goalDist.values())
    optimalGoal = [key for key in goalDist if goalDist[key] == temp]
    print("closest goal", optimalGoal)

    # actually calculate where goal came fgrom
    # find path

    end = optimalGoal[0]
    tempath = []

    # while end != start_point:
    #     tempath.append(parentof[end])
    #     end = parentof[end]
    #     print(end)

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

    ele = Node(start_point, -1, 0)

    frontier.append(ele)

    parents = {key: [] for key in range(1, len(cost))}
    print(parents)

    for each in frontier:
                print("AAAAAAA (state, parent)",each.state, each.parent)

    while True:
        if len(frontier) == 0:
            print("No solution")
            return []

        # remove node from top of stack
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
    if A_star_Traversal(cost, heuristic, start, goals)==[1,5,4,7]:
        print("Test Case 1 for A* Traversal PASSED")
    else:
        print("Test Case 1 for A* Traversal FAILED")
except exception as e:
    print("Test Case 1 for A* Traversal FAILED due to ",e)