"""
Carol needs to trasport some hazardous substance from lab x to lab y.
Max needs to the same but in the opposite direction.
The substances cannot get closer to each other than d.
There is an undirected, weighted graph G.
If needed one of then may stay in place for some time.
Carol and Max cannot drive through the same edge at one time.
Plan Carol's and Max's routes.
"""
def keep_distance(M, x, y, d):
    n = len(M)
    dist = [[float("inf") if i != j else 0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if M[i][j] > 0:
                dist[i][j] = M[i][j]
            

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    ArrOfPairs = []
    ArrOfPairs.append((x, y))
    ArrOfPairs.append((y, x))
    for i in range(n):
        for j in range(n):
            if dist[i][j] >= d and (i, j) != (x, y) and (i, j) != (y, x):
                ArrOfPairs.append((i, j))
    
      
    G = [[0 for _ in range(len(ArrOfPairs))] for _ in range(len(ArrOfPairs))]
    for i in range(len(G)):
        for j in range(len(G)):
            if ArrOfPairs[i] != ArrOfPairs[j] and (M[ArrOfPairs[i][0]][ArrOfPairs[j][0]] or ArrOfPairs[i][0] == ArrOfPairs[j][0]) > 0 and (M[ArrOfPairs[i][1]][ArrOfPairs[j][1]] > 0 or ArrOfPairs[i][1] == ArrOfPairs[j][1]):
                G[i][j] = 1
            

    visited = [False for _ in range(len(ArrOfPairs))]
    parent = [-1 for _ in range(len(ArrOfPairs))]
    def DFSVisit(G, i):
        visited[i] = True
        for j in range(len(G)):
            if G[i][j] == 1 and not visited[j] and ArrOfPairs[i] != ArrOfPairs[j][::-1]:
                parent[j] = i
                DFSVisit(G, j)
    

    DFSVisit(G, 0)
    path = []
    temp = 1
    while temp != -1:
        path.append(ArrOfPairs[temp])
        temp = parent[temp]
    


    return path[::-1]



M = [
[0, 1, 1, 0],
[1, 0, 0, 1],
[1, 0, 0, 1],
[0, 1, 1, 0],
]
print(keep_distance(M, 0, 3, 2))