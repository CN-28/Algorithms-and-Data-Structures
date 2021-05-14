"""
The driver wants to go from town (vertex) A to town (vertex) B. Some roads (edges) have a 0 or 1 unit toll.
Find the miminal cost to get from town A to town B.
"""
from collections import deque

def findCheap(G, Vs, Vf):
    n = len(G)
    cost = [float("inf") for _ in range(n)]
    queue = deque()


    queue.append(Vs)
    cost[Vs] = 0
    while queue:
        u = queue.popleft()
        for j in range(n):
            if G[u][j] != -1 and cost[j] > cost[u] + G[u][j]:
                cost[j] = cost[u] + G[u][j]

                
                if G[u][j] == 0:
                    queue.appendleft(j)
                else:
                    queue.append(j)


    return cost[Vf]



G = [
    [-1, 0, 0, 1, 1, 1],
    [0, -1, 0, 0, 1, 1],
    [1, 0, -1, 1, 0, 1],
    [1, 1, 1, -1, 0, 1],
    [1, 1, 0, 1, -1, 1],
    [1, 1, 1, 1, 0, -1]
]
print(findCheap(G, 5, 0))