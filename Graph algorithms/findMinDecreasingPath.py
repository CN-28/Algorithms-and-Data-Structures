#array of edges representation
def decreasing_path(G, s, t):
    #m - number of edges
    m = len(G)
    #n - number of vertices
    n = 0
    for i in range(m):
        n = max(n, G[i][0], G[i][1])
    n += 1

    
    G.sort(key=lambda x: x[2], reverse=True)

    
    dist = [float('inf') for _ in range(n)]
    parent = [-1 for _ in range(n)]
    dist[s] = 0
    for i in range(m):
        u, v, w = G[i]
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            parent[v] = u
        elif dist[v] + w < dist[u]:
            dist[u] = dist[v] + w
            parent[u] = v

    
    return dist[t]


G = [(0, 1, 4), (1, 2, 10), (0, 4, 8), (1, 4, 11), (4, 5, 7), (4, 6, 4), (5, 6, 6), (2, 3, 2), (2, 5, 9), (3, 6, 3),
     (6, 7, 5), (3, 7, 15), (3, 8, 8), (7, 8, 1)]
print(decreasing_path(G, 0, 8))