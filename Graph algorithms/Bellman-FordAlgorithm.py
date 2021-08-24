#time complexity: O(V * E)
def Bellman_Ford(G, s):
    n = len(G)
    dist = [float("inf") for _ in range(n)]
    parent = [-1 for _ in range(n)]


    dist[s] = 0
    for _ in range(n - 1):
        for u in range(n):
            for v, c in G[u]:
                if dist[u] + c < dist[v]:
                    dist[v] = dist[u] + c
                    parent[v] = u
    

    #check for negative-weight cycles
    for u in range(n):
        for v, c in G[u]:
            if dist[u] != float("inf") and dist[u] + c < dist[v]:
                return False
        
    return dist



G = [[(3, 1), (4, 2), (5, 3)], [(4, 2), (5, 3)], [(3, 5), (5, 4)], [(0, 1), (2, 5)], [(0, 2), (1, 2)], [(0, 3), (1, 3), (2, 4)]]
print(Bellman_Ford(G, 0))