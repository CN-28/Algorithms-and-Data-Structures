def breaking(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    disc = [float("inf") for _ in range(n)]
    low = [float("inf") for _ in range(n)]
    
    maxi = 0
    time = 0
    max_v = None
    def DFSVisit(G, u):
        nonlocal maxi, max_v, time
        visited[u] = True
        disc[u] = time
        low[u] = time
        children = 0
        time += 1
        for v in range(n):
            if not visited[v] and G[u][v] == 1:
                parent[v] = u
                children += 1
                DFSVisit(G, v)

                low[u] = min(low[u], low[v])
                if parent[u] == -1 and children > 1:
                    if children > maxi:
                        maxi = children
                        max_v = u

                if parent[u] != -1 and low[v] >= disc[u]:
                    if children + 1 > maxi:
                        maxi = children + 1
                        max_v = u
            elif G[u][v] == 1:
                low[u] = min(low[u], disc[v])


    
    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u)
    
    return max_v