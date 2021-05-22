class Node:
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
    if x == y:
        return False
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1



def kruskal(G):
    n = len(G)
    G.sort(key = lambda x: x[2])
    print(G)

    
    res = []
    
    A = Node(G[0][0])
    union(A, Node(G[0][1]))
    for i in range(1, n):
        e = Node(G[i][0])
        union(e, Node(G[i][1]))
        union(A, e)
    
    print(A.val)

    

G = [(0, 1, 2), (0, 5, 7), (0, 3, 3), (0, 4, 8), (5, 4, 1), (1, 2, 5), (2, 4, 4), (2, 3, 6), (3, 4, 12)]
kruskal(G)