#time complexity: O(V**2)
def articulationPoints(G):
    n = len(G)
    visited = [False for _ in range(n)]
    disc = [float("inf") for _ in range(n)]
    low = [float("inf") for _ in range(n)]
    parent = [-1 for _ in range(n)]
    AP = []


    time = 0
    def DFSVisit(u):
        nonlocal time
        children = 0
        visited[u] = True
        disc[u] = time
        low[u] = time
        time += 1

        for v in range(n):
            if G[u][v] == 1:
                if not visited[v]:
                    parent[v] = u
                    children += 1
                    DFSVisit(v)

                    low[u] = min(low[u], low[v])
                    if parent[u] == -1 and children > 1:
                        AP.append(u)
                    
                    elif parent[u] != -1 and low[v] >= disc[u]:
                        AP.append(u)
                    
                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])


    for u in range(n):
        if not visited[u]:
            DFSVisit(u)
    
    return AP



G = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
]
print(articulationPoints(G))