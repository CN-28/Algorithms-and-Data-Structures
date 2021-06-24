"""
Given a binary tree T, compute maximum-cost subtree that uses at most k edges
"""
class Node:
    def __init__(self):
        self.left    = None
        self.leftval = 0
        self.right   = None
        self.rightval= 0
        self.X       = None



class DP:
    def __init__(self, k):
        self.f = [None] * (k + 1)
        self.g = None



def f(T, k):
    if k == 0:
        return 0
    if not T:
        return -float("inf")
    if T.X == None:
        T.X = DP(k)
    if T.X.f[k]:
        return T.X.f[k]
    

    T.X.f[k] = -float("inf")
    if T.right:
        T.X.f[k] = max(T.X.f[k], T.rightval + f(T.right, k - 1))
    
    if T.left:
        T.X.f[k] = max(T.X.f[k], T.leftval + f(T.left, k - 1))
    
    if T.left and T.right and k >= 2:
        for i in range(1, k):
            T.X.f[k] = max(T.X.f[k], T.leftval + f(T.left, i - 1) + T.rightval + f(T.right, k - i - 1))
    

    return T.X.f[k]



def g(T, k):
    if k == 0:
        return 0
    if not T:
        return -float("inf")
    if T.X == None:
        T.X = DP(k)
    if T.X.g:
        return T.X.g
    
    
    T.X.g = max(g(T.left, k), g(T.right, k), f(T, k))
    return T.X.g



def valuableTree( T, k ):
    return g(T, k)



def make_tree():
    A = Node()
    B = Node()
    C = Node()
    D = Node()
    E = Node()
    F = Node()
    G = Node()
    A.left = B
    A.right = E
    B.left = D
    B.right = C
    C.left = F
    C.right = G
    A.leftval = 1
    A.rightval = 5
    B.leftval = 6
    B.rightval = 2
    C.leftval = 8
    C.rightval = 10
    return A



T = make_tree()
print(valuableTree(T, 3))