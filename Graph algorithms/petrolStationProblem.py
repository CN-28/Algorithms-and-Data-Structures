"""
You need to get from town A to town B. Your car consume 1l of fuel per kilometer.
The tank holds a maximum of D liters. The route is represented as a graph, in which
vertices are towns and edges are roads connecting them. The unit of road lengths is kilometer.
In every vertex there is a petrol station with a given price per liter of fuel.
Find a route from A to B with the smallest cost.
"""
from queue import PriorityQueue
def PSP(G, fuelCost, A, B, D):
    n = len(G)
    GG = [[] for _ in range((D + 1) * n)]
    for u in range(n):
        for l in range(D):
            GG[u*(D + 1) + l].append((u * (D + 1) + l + 1, fuelCost[u]))
    

    for u in range(n):
        for v, c in G[u]:
            for l in range(1, D + 1):
                if l - c >= 0:
                    GG[u * (D + 1) + l].append((v * (D + 1) + l - c, 0))


    dist = [float("inf") for _ in range((D + 1) * n)]
    parent = [-1 for _ in range((D + 1) * n)]
    dist[A * (D + 1)] = 0
    Q = PriorityQueue()
    Q.put((0, A * (D + 1)))
    while not Q.empty():
        c, u = Q.get()
        for v, w in GG[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                Q.put((dist[v], v))
    

    path = []
    temp = B * (D + 1)
    while temp != -1:
        u = temp // (D + 1)
        if len(path) == 0 or path[len(path) - 1] != u:
            path.append(u)
        temp = parent[temp]


    return dist[B * (D + 1)], path[::-1]



G = [
    [(1, 3), (2, 7), (3, 2)],
    [(0, 3), (4, 5)],
    [(0, 7), (4, 4)],
    [(0, 2), (4, 6)],
    [(1, 5), (2, 4), (3, 6)]
]
fuelCost = [2, 3, 4, 10, 5]
print(PSP(G, fuelCost, 0, 4, 7))