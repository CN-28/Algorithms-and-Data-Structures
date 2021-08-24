#time complexity: O(V**3)
def Floyd_Warshall(G):
    n = len(G)
    dist = [[float("inf") if i != j else 0 for j in range(n)] for i in range(n)]
    next = [[-1 if i != j else i for j in range(n)] for i in range(n)]
    for u in range(n):
        for v, c in G[u]:
            dist[u][v] = c
            next[u][v] = v


    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next[i][j] = next[i][k]


    def getPath(u, v):
        if next[u][v] == -1:
            return []
        
        path = [u]
        while u != v:
            u = next[u][v]
            path.append(u)

        return path

    return dist



G = [[(3, 1), (4, 2), (5, 3)], [(4, 2), (5, 3)], [(3, 5), (5, 4)], [(0, 1), (2, 5)], [(0, 2), (1, 2)], [(0, 3), (1, 3), (2, 4)]]
print(Floyd_Warshall(G))