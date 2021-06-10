#G = (V, E) with weights E -> N/{0}, find the path from u to v with the smallest product of weights, time complexity: O(E*logV)
from math import log10
from queue import PriorityQueue
def minProductPath(G, u, v):
    n = len(G)
    dist = [float("inf") for _ in range(n)]
    parent = [-1 for _ in range(n)]
    dist[u] = 0


    Q = PriorityQueue()
    Q.put((dist[u], u))
    while not Q.empty():
        c, s = Q.get()
        for t, w in G[s]:
            if c + log10(w) < dist[t]:
                dist[t] = c + log10(w)
                parent[t] = s
                Q.put((c + log10(w), t))

    path = []
    path.append(v)
    temp = parent[v]
    while temp != -1:
        path.append(temp)
        temp = parent[temp]


    for i in range(len(path) - 1, -1, -1):
        if i != 0:
            print(path[i], end='---> ')
        else:
            print(path[i])



G = [[(1, 24), (2, 58)], [(0, 24), (3, 24)], [(0, 58), (3, 9)], [(1, 24), (2, 9)]]
minProductPath(G, 0, 3)