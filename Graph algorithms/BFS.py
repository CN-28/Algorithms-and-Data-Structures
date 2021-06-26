#adjacency list
from collections import deque
def BFS(G):
    n = len(G)
    visited = [False for _ in range(n)]
    dist = [float("inf") for _ in range(n)]
    Q = deque()
    
    visited[0] = True
    dist[0] = 0
    Q.append(0)
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                Q.append(v)



#adjacency matrix
def BFS(G):
    n = len(G)
    visited = [False for _ in range(n)]
    dist = [float("inf") for _ in range(n)]
    Q = deque()


    visited[0] = True
    dist[0] = 0
    Q.append(0)
    while Q:
        u = Q.popleft()
        for v in range(n):
            if G[u][v] == 1 and not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                Q.append(v) 