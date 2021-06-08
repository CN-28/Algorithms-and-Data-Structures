from queue import PriorityQueue

#adjacency list, time coplexity: O(E*logV)
def dijkstraAL(G, V_s):
    n = len(G)
    dist = [float('inf') for _ in range(n)]
    parent = [-1 for _ in range(n)]
    dist[V_s] = 0
    

    queue = PriorityQueue()
    queue.put((dist[V_s], V_s))
    while not queue.empty():
        c, u = queue.get()
        for v, w in G[u]:
            if c + w < dist[v]:
                dist[v] = c + w
                parent[v] = u
                queue.put((c + w, v))


    return parent, dist



#adjcacency matrix, time complexity: O(V**2)
def dijkstraAM(G, V_s):
    n = len(G)
    visited = [False for _ in range(n)]
    dist = [float("inf") for _ in range(n)]
    parent = [-1 for _ in range(n)]
    dist[V_s] = 0


    for i in range(n):
        mini = float("inf")
        for j in range(n):
            if dist[j] < mini and not visited[j]:
                mini = dist[j]
                u = j
            

        visited[u] = True
        for j in range(n):
            if G[u][j] > 0 and not visited[j] and dist[j] > dist[u] + G[u][j]:
                dist[j] = dist[u] + G[u][j]
                parent[j] = u


    return parent, dist



G = [[(3, 1), (4, 2), (5, 3)], [(4, 2), (5, 3)], [(3, 5), (5, 4)], [(0, 1), (2, 5)], [(0, 2), (1, 2)], [(0, 3), (1, 3), (2, 4)]]
print(dijkstraAL(G, 0))


H = [
    [0, 0, 0, 1, 2, 3],
    [0, 0, 0, 0, 2, 3],
    [0, 0, 0, 5, 0, 4],
    [1, 0, 5, 0, 0, 0],
    [2, 2, 0, 0, 0, 0],
    [3, 3, 4, 0, 0, 0]
]
print(dijkstraAM(H, 0))