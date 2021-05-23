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



def kruskal(G, n):
    V = [MakeSet(i) for i in range(n)]
    G.sort(key = lambda x: x[2])

    res = []
    for u, v, w in G:
        if union(V[u], V[v]):
            res.append((u, v))
    
    return res
    

    
G = [(0, 1, 2), (0, 5, 7), (0, 3, 3), (0, 4, 8), (5, 4, 1), (1, 2, 5), (2, 4, 4), (2, 3, 6), (3, 4, 12)]
n = 6
print(kruskal(G, n))