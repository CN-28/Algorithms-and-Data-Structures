#find bridges in an undirected graph
def findBridges(G):
    n = len(G)
    visited = [False for _ in range(n)]
    time = 0
    timeArr = [-1 for _ in range(n)]
    low = [float("inf") for _ in range(n)]
    parent = [-1 for _ in range(n)]


    def DFSVisit(i):
        nonlocal time
        visited[i] = True
        time += 1
        timeArr[i] = time
        low[i] = time
        for j in range(n):
            if G[i][j] == 1:
                if not visited[j]:
                    parent[j] = i
                    DFSVisit(j)
                    low[i] = min(low[i], low[j])
                elif parent[i] != j and G[i][j] == 1:
                    low[i] = min(timeArr[j], low[i])
        

        if timeArr[i] == low[i] and parent[i] != -1:
            print(i, parent[i])
    

    for i in range(n):
        if not visited[i]:
            DFSVisit(i)
        


G = [
    [0, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0]
]
findBridges(G)