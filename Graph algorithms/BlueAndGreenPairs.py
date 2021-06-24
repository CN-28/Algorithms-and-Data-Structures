"""
There is an undirected, weighted graph T.
T[i][j] > 0 means there exists edge from the vertex i to the vertex j.
Every vertex is blue or green, find the maximum number of pairs of vertices (p, q) e V X V, such that
q is green and p is blue and the distance between p and q is not less than D and every vertex belongs to only one pair.
"""
from maxFlowEdmondsKarp import edmonds_karp


def BlueAndGreen(T, K, D):
    n = len(T)
    dist = [[float("inf") if i != j else 0 for j in range(n)] for i in range(n)]

    for u in range(n):
        for v in range(n):
            if T[u][v] > 0:
                dist[u][v] = T[u][v]

    for u in range(n):
        for v in range(n):
            for k in range(n):
                if T[u][k] > 0 and T[k][v] > 0 and dist[u][k] + dist[k][v] < dist[u][v]:
                    dist[u][v] = dist[u][k] + dist[k][v]

    
    G1 = [[1 if i < n and j < n and dist[i][j] >= D and (K[i] == "B" and K[j] == "G" or K[i] == "G" and K[j] == "B") else 0 for j in range(n + 2)] for i in range(n + 2)]
    for i in range(n):
        if K[i] == "B":
            G1[n][i] = 1
        else:
            G1[i][n + 1] = 1
    
    
    return edmonds_karp(G1, n, n + 1)


T = [
    [0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0],
]
K = ['B', 'B', 'G', 'G', 'B']
D = 2

print(BlueAndGreen(T, K, D))