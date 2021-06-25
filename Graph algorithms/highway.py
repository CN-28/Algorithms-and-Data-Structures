#EXAM 2020, task 2, second exam date
from math import ceil

class MakeSet:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self



def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent



def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        if x.rank > y.rank:
            y.parent = x
        else:
            x.parent = y
            if x.rank == y.rank:
                y.rank += 1
        return True



def kruskal(G, edge, lenA):
    n = len(G)
    V = [MakeSet(i) for i in range(n)]


    res = []
    for u, v, w in G[edge:]:
        if union(V[u], V[v]):
            res.append((u, v, w))
    if len(res) < lenA - 1:
        return float("inf")
    

    maxi = 0
    for i in range(len(res)):
        if res[i][2] > maxi:
            maxi = res[i][2]

    
    return maxi - G[edge][2]




def highway(A):
    n = len(A)
    G = []
    for i in range(n):
        for j in range(n):
            if i != j:    
                G.append((i, j, ceil(((A[i][0] - A[j][0])**2 + (A[i][1] - A[j][1])**2)**(1/2))))
    
    G.sort(key = lambda x: x[2])
    minTime = float("inf")
    for i in range(len(G)):
        minTime = min(minTime, kruskal(G, i, n))

    return minTime