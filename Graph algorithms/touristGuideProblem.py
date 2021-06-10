"""
The tourist guide wants to transport K tourists from the town A to the town B. There are many other towns along the way
and buses with different capacities c_i run between the different towns. Find the minimum number of groups into which the guide must divide
his group in order for everyone to get from A to B.
"""
from queue import PriorityQueue
def TGP(G, A, B, K):
    n = len(G)
    dist = [0 for _ in range(n)]
    parent = [-1 for _ in range(n)]


    Q = PriorityQueue()
    Q.put((-float("inf"), A))
    while not Q.empty():
        c, u = Q.get()
        c = -c
        for v, w in G[u]:
            if dist[v] < min(w, c):
                dist[v] = min(w, c)
                parent[v] = u
                Q.put((-dist[v], v))
        
    cnt = 0
    if K % dist[v] == 0:
        cnt = K//dist[v]
    else:
        cnt = K//dist[v] + 1


    path = []
    path.append(B)
    temp = B
    while temp != A:
        temp = parent[temp]
        path.append(temp)
    for i in range(len(path) - 1, -1, -1):
        if i != 0:
            print(path[i], end="---> ")
        else:
            print(path[i])


    return cnt



G = [[(1, 25), (2, 15), (3, 17)], [(0, 25), (4, 22)], [(0, 15), (4, 20)], [(0, 17), (4, 35)], [(1, 22), (2, 20), (3, 35)]]
print(TGP(G, 0, 3, 27))