from queue import PriorityQueue
def maxCapacity(G, s, t):
    n = len(G)
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    capacity = [float("inf") for _ in range(n)]

    Q = PriorityQueue()
    Q.put((-float("inf"), s))
    while not Q.empty():
        c, u = Q.get()
        c = -c
        visited[u] = True
        for v, w in G[u]:
            if not visited[v]:
                parent[v] = u
                capacity[v] = min(c, w)
                Q.put((-capacity[v], v))
    

    temp = t
    path = []
    if capacity[t] == float("inf"):
        return False


    while temp != -1:
        path.append(temp)
        temp = parent[temp]
    print(path[::-1])


    return capacity[t]



G = [[(1, 4), (2, 3)], [(3, 5)], [(3, 5)], []]
print(maxCapacity(G, 0, 3))