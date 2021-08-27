from maxFlowEdmondsKarp import edmonds_karp
#time complexity: O((V**2) * (E**2))
def edgeConnectivity(G):
    n = len(G)
    k = float("inf")
    GG = [[G[i][j] for j in range(n)] for i in range(n)]


    for i in range(1, n):
        k = min(k, edmonds_karp(GG, 0, i))
        GG = [[G[i][j] for j in range(n)] for i in range(n)]


    return k



G = [
    [0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 0, 0]
]
print(edgeConnectivity(G))