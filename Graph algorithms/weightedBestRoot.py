from collections import deque
def weightedBestRoot(G):
    dist, _ = BFS(G, 0)
    index = dist.index(max(dist))
    
    dist, parent = BFS(G, index)
    index = dist.index(max(dist))
    x = dist[index]/2
    
    
    temp = index
    mini = float("inf")
    ind = -1
    while temp != -1:
        if abs(x - dist[temp]) < mini:
            mini = abs(x - dist[temp])
            ind = temp
        temp = parent[temp]
    
    return ind



def BFS(G, i):
    n = len(G)
    visited = [False for _ in range(n)]
    dist = [0 for _ in range(n)]
    parent = [-1 for _ in range(n)]

    Q = deque()
    Q.append(i)
    visited[i] = True
    while Q:
        u = Q.popleft()
        for v, c in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                dist[v] = dist[u] + c
                Q.append(v)

    return dist, parent



G = [
    [(1, 100)],
    [(2, 5), (0, 100)],
    [(3, 98), (6, 95), (5, 96), (4, 97), (1, 5)],
    [(2, 98)],
    [(2, 97)],
    [(2, 96)],
    [(2, 95)]
]
G = [
    [(1, 1000)],
    [(2, 450), (0, 1000)],
    [(3, 250), (5, 600), (1, 450)],
    [(2, 250)],
    [(3, 400)],
    [(2, 600)]
]
print(weightedBestRoot(G))