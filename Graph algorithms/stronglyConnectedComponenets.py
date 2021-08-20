#finding strongly connected components in directed graph
def SCC(G):
    n = len(G)
    
    processingTime = []
    visited = [False for _ in range(n)]
    def getTimes(i):
        visited[i] = True
        for j in range(n):
            if G[i][j] == 1 and not visited[j]:
                getTimes(j)

        processingTime.append(i)
    

    getTimes(0)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if G[i][j] != G[j][i]:
                G[i][j], G[j][i] = G[j][i], G[i][j]
            
    
    def DFSVisit(i, temp):
        visited[i] = False
        for j in range(n):
            if G[i][j] == 1 and visited[j]:
                DFSVisit(j, temp)

        temp.append(i)
    

    SCC = []
    for i in range(n - 1, -1, -1):
        temp = []
        if visited[processingTime[i]]:
            DFSVisit(processingTime[i], temp)
            SCC.append(temp)
    
    #reconstruct the initial graph
    for i in range(n - 1):
        for j in range(i + 1, n):
            if G[i][j] != G[j][i]:
                G[i][j], G[j][i] = G[j][i], G[i][j]

    return SCC



G = [
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
]
print(SCC(G))