"""
In the graph G each edge has weight, check if there is a path from vertex v to vertex u
which passes along edges with smaller and smaller weights
"""
def existsPath(G, Vs, Vf):
    n = len(G)
    visited = [False for _ in range(n)]
    prev = float("inf")


    visited[Vs] = True
    def DFSVisit(i, prev):
        visited[i] = True
        for j in range(n):
            if not visited[j] and G[i][j] > 0 and G[i][j] < prev:
                if j == Vf:
                    return True

                prev = G[i][j]
                if DFSVisit(j, prev):
                    return True
                

    for i in range(n):
        if not visited[i]:
            if DFSVisit(i, prev):
                return True
            
            
    return False



G = [
    [-1, 18, 16, 0, 0, 0],
    [18, -1, 0, 17, 0, 0],
    [16, 0, -1, 15, 0, 0],
    [0, 17, 15, -1, 14, 0],
    [0, 0, 0, 14, -1, 13],
    [0, 0, 0, 0, 13, -1]
]
print(existsPath(G, 0, 5))