#E - edges, version with E -> N, N - natural numbers
from queue import PriorityQueue


#O(E*logV)
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
            if not visited[v] and c + w < dist[v] and (prevVal[u] == None or prevVal[u] > w):
                dist[v] = c + w
                parent[v] = u
                prevVal[v] = w
                Q.put((dist[v], v))

    return dist[t]


G = [[(3, 15), (4, 2), (5, 3)], [(4, 2), (5, 3)], [(3, 5), (5, 4)], [(0, 15), (2, 5)], [(0, 2), (1, 2)], [(0, 3), (1, 3), (2, 4)]]
print(findAL(G, 3, 4))


#O(V**2)
def findAM(G, s, t):
    ...