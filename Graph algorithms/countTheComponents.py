def count(G):
    n = len(G)
    visited = [False for _ in range(n)]
    def DFSVisit(i):
        visited[i] = True
        for j in range(len(G[i])):
            if not visited[G[i][j]]:
                DFSVisit(G[i][j])
        

    cnt = 0
    for i in range(n):
        if not visited[i]:
            DFSVisit(i)
            cnt += 1
    
    
    return cnt



G = [[3, 4, 5], [4, 5], [3, 5], [0, 2], [0, 1], [0, 1, 2]]
print(count(G))