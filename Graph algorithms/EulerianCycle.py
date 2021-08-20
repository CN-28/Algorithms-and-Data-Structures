#time complexity: O(V**2), space complexity: O(V + E)
def euler(G):
    n = len(G)
    edges = 0
    for i in range(n):
        degree = sum(G[i])
        edges += degree
        if degree % 2 != 0:
            return False
    

    cycle = []
    def DFSVisit(i):
        for j in range(n):
            if G[i][j] == 1:
                G[i][j] = 0
                G[j][i] = 0
                DFSVisit(j)
        
        cycle.append(i)
    

    DFSVisit(0)
    for i in range(1, len(cycle)):
        G[cycle[i - 1]][cycle[i]] = 1
        G[cycle[i]][cycle[i - 1]] = 1
    
    if len(cycle) != edges//2 + 1:
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