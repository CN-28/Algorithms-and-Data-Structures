#finding strongly connected components in directed graph
def SCC(G):
    n = len(G)
    visited = [False for _ in range(n)]
    timeArr = [-1 for _ in range(n)]
    time = 0
    def DFSVisit(i):
        nonlocal time
        visited[i] = True
        for j in range(n):
            if G[i][j] == 1 and not visited[j]:
                DFSVisit(j)
        
        
        timeArr[time] = i
        time += 1
    

    for i in range(n):
        if not visited[i]:
            DFSVisit(i)
    
    
    for i in range(n):
        for j in range(n):
            if G[i][j] == 1:
                G[i][j] = 0
                G[j][i] = 2
    
    
    def DFSVisit_comp(i):
        visited[i] = False
        for j in range(n):

            if G[i][j] == 2 and visited[j]:
                DFSVisit_comp(j)
        
        temp_arr.append(i)


    SSC = []
    temp_arr = []
    for i in range(n - 1, -1, -1):
        if visited[timeArr[i]]:
            DFSVisit_comp(timeArr[i])
            SSC.append(temp_arr)
            temp_arr = []
    
    return SSC




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