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
    for i in range(n):
        if union(MakeSet(G[i][0]), MakeSet(G[i][1])) == None:
            res.append((G[i][0], G[i][1]))
    print(res)

    

G = [(0, 1, 2), (0, 5, 7), (0, 3, 3), (0, 4, 8), (5, 4, 1), (1, 2, 5), (2, 4, 4), (2, 3, 6), (3, 4, 12)]
kruskal(G)