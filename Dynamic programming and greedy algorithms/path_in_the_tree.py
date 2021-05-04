"""
There is rooted tree, each vertex has value - negative or non-negative number, find the most valuable path in this tree.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.down = []
        self.f = 0

#tree
v = Node(75)
v.down.append(Node(-1000))
v.down.append(Node(601))
v.down.append(Node(-243))
v.down[0].down.append(Node(12))
v.down[0].down.append(Node(4))
v.down[2].down.append(Node(45))
v.down[2].down.append(Node(8))
v.down[2].down.append(Node(1))
v.down[2].down.append(Node(145))
v.down[2].down[1].down.append(Node(10000))
v.down[2].down[1].down.append(Node(-12))



def solve(v, maxi):
    if len(v.down) == 0:
        return v.val


    res = []
    for i in range(len(v.down)):
        res.append(max(0, v.val, v.val + solve(v.down[i], maxi)))
    
    
    next_max = 0
    index = -1
    for i in range(len(v.down)):
        if res[i] > v.f:
            v.f = res[i]
            index = i

    
    for i in range(len(v.down)):
        if res[i] > next_max and i != index:
            next_max = res[i]


    return max(0, v.f, v.f + next_max - abs(v.val))



print(solve(v, 0))