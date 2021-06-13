from queue import PriorityQueue
def findMaxCap(G, s, t):
    n = len(G)
    capacity = [-float("inf") for _ in range(n)]
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    Q = PriorityQueue()


    Q.put((-float("inf"), s))
    while not Q.empty():
        c, u = Q.get()
        c = -c
        visited[u] = True
        for v, w in G[u]:
            if not visited[v] and capacity[v] < min(w, c):
                capacity[v] = min(w, c)
                parent[v] = u
                Q.put(((-capacity[v], v)))


    if capacity[t] != float("inf"):
        path = []
        temp = t
        while temp != -1:
            path.append(temp)
            temp = parent[temp]
        print(path)


    return capacity[t]



G = [
    [(1,4), (2,3)],
    [(3,2)],
    [(3,5)],
    []
]
print(findMaxCap(G, 0, 3))