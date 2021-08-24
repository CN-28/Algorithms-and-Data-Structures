#O(V**3), using modified Floyd-Warshall algorithm
def transitiveClosureAM(G):
    n = len(G)
    H = [[G[i][j] for j in range(n)] for i in range(n)]
    
    for i in range(n):
        H[i][i] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                H[i][j] |= H[i][k] and H[k][j]
    
    return H


G = [
    [0, 1, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]
for x in transitiveClosureAM(G):
    print(x)



#O(V*(V + E)), but graph must be represented as Adjacency List
def transitiveClosureAL(G):
    n = len(G)
    H = [[0 for _ in range(n)] for _ in range(n)]
    def DFS(u, v):
        H[u][v] = 1
        for w in G[v]:
            if H[u][w] == 0:
                DFS(u, w)



    for i in range(n):
        DFS(i, i)
    
    return H



G = [[1, 3], [2], [3], []]
print()
for x in transitiveClosureAL(G):
    print(x)