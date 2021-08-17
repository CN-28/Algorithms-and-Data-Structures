"""
There is rooted tree, each vertex has value - negative or non-negative number, find the most valuable path in this tree.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.f = 0



def mostValuablePath(T, v, maxi=[]):
    n = len(T.children)
    if n == 0:
        T.f = T.val
        return T.f
    
    
    next_max = 0
    for i in range(n):
        temp = max(0, T.f, T.val, T.val + mostValuablePath(T.children[i], v, maxi))
        if temp != T.f:
            next_max = T.f
        T.f = temp

    
    if next_max != 0:
        maxi.append(T.f + next_max - T.val)
    maxi.append(T.f)
    if T == v:
        return max(maxi)
    return T.f



def makeTree():
    T = Node(70)
    T.children.append(Node(24))
    T.children.append(Node(-200))
    T.children.append(Node(11))
    T.children[0].children.append(Node(45))
    T.children[0].children.append(Node(-100))
    T.children[1].children.append(Node(5))
    T.children[1].children.append(Node(10))
    T.children[1].children.append(Node(30))
    T.children[1].children.append(Node(1000))
    T.children[2].children.append(Node(8))
    T.children[2].children.append(Node(7))
    T.children[2].children.append(Node(9))
    return T


T = makeTree()
print(mostValuablePath(T, T))