"""
The tourist guide wants to transport K tourists from the town A to the town B. There are many other towns along the way
and buses with different capacities c_i run between the different towns. Find the minimum number of groups into which the guide must divide
his group in order for everyone to get from A to B, such that the group don't need to divide into smaller ones during the trip.
"""
from queue import PriorityQueue
def TGP(G, A, B, K):
    n = 0
    for u, v, cost in G:
        n = max(n, u + 1, v + 1)

    GG = [[] for _ in range(n)]
    for u, v, cost in G:
        GG[u].append((v, cost))

    
    maxCap = [0 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    maxCap[A] = float("inf")
    Q = PriorityQueue()
    Q.put((-float("inf"), A))
    while not Q.empty():
        c, u = Q.get()
        c = -c
        for v, w in GG[u]:
            capacity = min(w, c)
            if capacity > maxCap[v]:
                maxCap[v] = capacity
                parent[v] = u
                Q.put((-capacity, v))
    
    
    cnt = 0
    if K % maxCap[B] == 0:
        cnt = K // maxCap[B]
    else:
        cnt = K // maxCap[B] + 1

    
    path = []
    temp = B
    while temp != -1:
        path.append(temp)
        temp = parent[temp]
    

    return cnt, path[::-1]



G = [(0, 2, 15), (2, 0, 15), (1, 0, 31), (0, 1, 31), (0, 3, 25), (3, 0, 25), (5, 2, 20), (2, 5, 20), (3, 5, 21), (5, 3, 21), (1, 4, 34), (4, 1, 34), (5, 4, 29), (4, 5, 29)]
print(TGP(G, 0, 5, 58))