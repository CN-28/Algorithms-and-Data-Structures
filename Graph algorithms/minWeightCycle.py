#find the cycle with minimum weight and return an array of its vertices 
from copy import deepcopy
def findMinCycle(G):
    n = len(G)
    dist = [[float("inf") for _ in range(n)] for _ in range(n)]
    parent = [[-1 for _ in range(n)] for _ in range(n)]
    min_val = float("inf")
    path = 0, 0, 0
    cycle = []
    def dijkstraAM(G, V_s):
        n = len(G)
        visited = [False for _ in range(n)]
        dist[V_s][V_s] = 0
        nonlocal min_val, path

        for i in range(n):
            mini = float("inf")
            for j in range(n):
                if dist[V_s][j] < mini and not visited[j]:
                    mini = dist[V_s][j]
                    u = j
                

            visited[u] = True
            for j in range(n):
                if G[u][j] >= 0 and not visited[j] and min_val > dist[V_s][j] + dist[V_s][u] + G[u][j]:
                    path = deepcopy(parent[V_s]), (u, j), V_s
                    min_val = dist[V_s][j] + dist[V_s][u] + G[u][j]
                if G[u][j] >= 0 and not visited[j] and dist[V_s][j] > dist[V_s][u] + G[u][j]:
                    dist[V_s][j] = dist[V_s][u] + G[u][j]
                    parent[V_s][j] = u
                

    for i in range(n):
        dijkstraAM(G, i)
    if path != (0, 0, 0):
        def getSol(Arr, ind, temp, parent):
            if parent[ind] != temp:
                getSol(Arr, parent[ind], temp, parent)
            Arr.append(ind)
        getSol(cycle, path[1][0], -1, path[0])
        
        
        cycle.append(path[1][1])
        temp = path[0][path[1][1]]
        while temp != path[2]:
            cycle.append(temp)
            temp = path[0][temp]
    

    return cycle



G = [
    [-1, 2,-1,-1, 1],
    [ 2,-1, 4, 1,-1],
    [-1, 4,-1, 5,-1],
    [-1, 1, 5,-1, 3],
    [ 1,-1,-1, 3,-1]
]
print(findMinCycle(G))