def islands(G, s, t):
    n = len(G)
    dist = [(float("inf"), float("inf"), float("inf")) for _ in range(n)]
    parent = [(-1, -1, -1) for _ in range(n)]

    dist[s] = 0, 0, 0
    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                if G[u][v] != 0:
                    if (parent[u][0] == -1 or G[parent[u][0]] != 8) and G[u][v] == 8 and dist[v][0] > min(dist[u][1], dist[u][2]) + G[u][v]:
                        dist[v] = min(dist[u][1], dist[u][2]) + G[u][v], dist[v][1], dist[v][2]
                        parent[v] = u, parent[v][1], parent[v][2]
                    
                    if (parent[u][1] == -1 or G[parent[u][0]] != 5) and G[u][v] == 5 and dist[v][1] > min(dist[u][0], dist[u][2]) + G[u][v]:
                        dist[v] = dist[v][0], min(dist[u][0], dist[u][2]) + G[u][v], dist[v][2]
                        parent[v] = parent[v][0], u, parent[v][2]
                    
                    if (parent[u][2] == -1 or G[parent[u][2]] != 1) and G[u][v] == 1 and dist[v][2] > min(dist[u][0], dist[u][1]) + G[u][v]:
                        dist[v] = dist[v][0], dist[v][1], min(dist[u][0], dist[u][1]) + G[u][v]
                        parent[v] = parent[v][0], parent[v][1], u


    return min(dist[t])
    


G = [
    [0, 5, 1, 8, 0, 0, 0],
    [5, 0, 0, 1, 0, 8, 0],
    [1, 0, 0, 8, 0, 0, 8],
    [8, 1, 8, 0, 5, 0, 1],
    [0, 0, 0, 5, 0, 1, 0],
    [0, 8, 0, 0, 1, 0, 5],
    [0, 0, 8, 1, 0, 5, 0]
]
print(islands(G, 5, 2))

G = [
[0, 1, 8, 0, 0],
[1, 0, 0, 5, 0],
[8, 0, 0, 1, 0],
[0, 5, 1, 0, 5],
[0, 0, 0, 5, 0]
]
print(islands(G, 0, 4))