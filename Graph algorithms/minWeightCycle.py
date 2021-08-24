#find the cycle with minimum weight and return an array of its vertices 
#time complexity: O(V**3), space complexity: O(V**2)
def dijkstraAM(G, v_s, min_cycle, s, t, start_v):
    n = len(G)
    visited = [False for _ in range(n)]
    dist = [float("inf") for _ in range(n)]
    dist[v_s] = 0


    for i in range(n):
        mini = float("inf")
        for j in range(n):
            if dist[j] < mini and not visited[j]:
                mini = dist[j]
                u = j
            
    
        visited[u] = True
        for v in range(n):
            if G[u][v] >= 0 and not visited[v]:
                if dist[v] + dist[u] + G[u][v] < min_cycle:
                    s, t, start_v = u, v, v_s
                    min_cycle = dist[v] + dist[u] + G[u][v]
                    

                if dist[v] > dist[u] + G[u][v]:
                    dist[v] = dist[u] + G[u][v]
    

    return min_cycle, s, t, start_v



def getCycle(G, v_s, min_cycle):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    dist = [float("inf") for _ in range(n)]
    dist[v_s] = 0


    for i in range(n):
        mini = float("inf")
        for j in range(n):
            if dist[j] < mini and not visited[j]:
                mini = dist[j]
                u = j
        

        visited[u] = True
        for v in range(n):
            if G[u][v] >= 0 and not visited[v]:
                if dist[v] + dist[u] + G[u][v] == min_cycle:
                    return parent
                    
                if dist[v] > dist[u] + G[u][v]:
                    dist[v] = dist[u] + G[u][v]
                    parent[v] = u



def min_cycle( G ):
    n = len(G)
    min_cycle = float("inf")
    s, t, start_v = -1, -1, -1
    for i in range(n):
        min_cycle, s, t, start_v = dijkstraAM(G, i, min_cycle, s, t, start_v)
    

    if min_cycle == float("inf"):
        return []
        

    cycle = []
    parent = getCycle(G, start_v, min_cycle)
    def getSol(parent, cycle, ind):
        if parent[ind] != -1:
            getSol(parent, cycle, parent[ind])
        cycle.append(ind)
    if s != -1:
        getSol(parent, cycle, s)

    
    temp = t
    while temp != start_v:
        cycle.append(temp)
        temp = parent[temp]


    return min_cycle, cycle
  
  

#test cases
G1 = [
    [-1, 2,-1,-1, 1],
    [ 2,-1, 4, 1,-1],
    [-1, 4,-1, 5,-1],
    [-1, 1, 5,-1, 3],
    [ 1,-1,-1, 3,-1]
]
G2 = [
    [-1, 1, -1, 1],
    [1, -1, 1, -1],
    [-1, 1, -1, 1],
    [1, -1, 1, -1]
]
G3 = [
    [-1, 5, 5, 5],
    [5, -1, 4, 5],
    [5, 4, -1, 5],
    [5, 5, 5, -1]
]
G4 = [
    [-1, 1, 2, -1, 4],
    [1, -1, -1, -1, -1],
    [2, -1, -1, 3, -1],
    [-1, -1, 3, -1, -1],
    [4, -1, -1, -1, -1]
]
G5 = [
    [-1, 1, -1, -1, -1, 1],
    [1, -1, 1, 300, -1, 400],
    [-1, 1, -1, 1, -1, -1],
    [-1, 300, 1, -1, 1, 200],
    [-1, -1, -1, 1, -1, 1],
    [1, 400, -1, 200, 1, -1]
]
print(min_cycle(G1))
print(min_cycle(G2))
print(min_cycle(G3))
print(min_cycle(G4))
print(min_cycle(G5))