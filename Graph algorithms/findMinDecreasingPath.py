#E - edges, version with E -> N, N - natural numbers
#Modified Dijkstra's Algorithm
from queue import PriorityQueue


#O(E*logV), Adjacency List
def findAL(G, s, t):
    n = len(G)
    visited = [False for _ in range(n)]
    dist = [float("inf") for _ in range(n)]
    parent = [-1 for _ in range(n)]
    prevVal = [None for _ in range(n)]

    
    Q = PriorityQueue()
    dist[s] = 0
    Q.put((dist[s], s))
    while not Q.empty():
        c, u = Q.get()
        visited[u] = True
        for v, w in G[u]:
            if not visited[v] and c + w < dist[v] and (u == s or prevVal[u] > w):
                dist[v] = c + w
                parent[v] = u
                prevVal[v] = w
                Q.put((dist[v], v))

    return dist[t]


G = [[(3, 15), (4, 2), (5, 3)], [(4, 2), (5, 3)], [(3, 5), (5, 4)], [(0, 15), (2, 5)], [(0, 2), (1, 2)], [(0, 3), (1, 3), (2, 4)]]
print(findAL(G, 3, 4))



#O(V**2), Adjacency Matrix
def findAM(G, s, t):
    n = len(G)
    dist = [float("inf") for _ in range(n)]
    dist[s] = 0
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]

    for u in range(n):
        mini = float("inf")
        for v in range(n):
            if dist[v] < mini and not visited[v]:
                mini = dist[v]
                y = v
        

        visited[y] = True
        for v in range(n):
            if G[y][v] > 0 and not visited[v] and dist[v] > dist[y] + G[y][v] and (y == s or G[parent[y]][y] > G[y][v]):
                dist[v] = dist[y] + G[y][v]
                parent[v] = y
    
    return dist[t]



G = [
    [0, 0, 0, 15, 2, 3],
    [0, 0, 0, 0, 2, 3],
    [0, 0, 0, 5, 0, 4], 
    [15, 0, 5, 0, 0, 0],
    [2, 2, 0, 0, 0, 0], 
    [3, 3, 4, 0, 0, 0] 
]
print(findAM(G, 3, 4))



#version wiht E -> R, R - rational numbers
#Modified Bellman-Ford Algorithm
#O(V*E), Adjacency List
def findAL2(G, s, t):
    n = len(G)
    dist = [float("inf") for _ in range(n)]
    parent = [-1 for _ in range(n)]
    prevVal = [None for _ in range(n)]


    dist[s] = 0
    for i in range(n - 1):
        for j in range(n):
            for k in range(len(G[j])):
                if dist[j] + G[j][k][1] < dist[G[j][k][0]] and (j == s or prevVal[j] > G[j][k][1]):
                    dist[G[j][k][0]] = dist[j] + G[j][k][1]
                    parent[G[j][k][0]] = j
                    prevVal[G[j][k][0]] = G[j][k][1]


    for j in range(n):
        for k in range(len(G[j])):
            if dist[G[j][k][0]] > dist[j] + G[j][k][1]:
                print("Graph contains a negative cycle")
                return False


    return dist[t]


G = [[(3, 15), (4, 2), (5, 3)], [(4, 2), (5, 3)], [(3, 5), (5, 4)], [(0, 15), (2, 5)], [(0, 2), (1, 2)], [(0, 3), (1, 3), (2, 4)]]
print(findAL2(G, 3, 4))