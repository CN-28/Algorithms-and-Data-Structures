def euler(G):
    n = len(G)
    edges = 0
    for i in range(n):
        degree = sum(G[i])
        edges += degree
        if degree % 2 != 0:
            return False


    G_alt = [[G[i][j] for j in range(n)] for i in range(n)]
    visited = 0
    cycle = []
    def DFSVisit(i):
        nonlocal visited
        for j in range(n):
            if G_alt[i][j] == 1:
                G_alt[i][j] = 0
                G_alt[j][i] = 0
                visited += 1
                DFSVisit(j)
        
        cycle.append(i)


    DFSVisit(0)
    if visited != edges//2:
        return False
    

    return cycle
    
  
  
#not all degrees of vertices are even
G1 = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 0, 0]
]
#exists
G2 = [
    [0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 0]
]
#not connected graph
G3 = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0]
]
print(euler(G1))
print(euler(G2))
print(euler(G3))