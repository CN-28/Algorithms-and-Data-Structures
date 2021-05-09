def euler(G):
    n = len(G)
    for i in range(n):
        if sum(G[i]) % 2 != 0:
            return

    G_alt = [[G[i][j] for j in range(n)] for i in range(n)]
    cycle = []
    def DFSVisit(i):
        for j in range(n):
            if G_alt[i][j] == 1:
                G_alt[i][j] = 0
                G_alt[j][i] = 0
                DFSVisit(j)
        
        cycle.append(i)


    DFSVisit(0)
    
    return cycle
    
  

G1 = [
    [0,1,1,0,0,0],
    [1,0,1,1,0,1],
    [1,1,0,0,1,1],
    [0,1,0,0,0,1],
    [0,0,1,0,0,1],
    [0,1,1,1,1,0]
]
G2 = [
    [0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 0]
]
print(euler(G1))
print(euler(G2))