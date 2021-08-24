"""
In the graph G each edge has weight, check if there is a path from vertex v to vertex u
which passes along edges with smaller and smaller weights.
Weights of edges are from set {1, ... , |E|} (every pair of edges has different values) 
time complexity: O(E)
"""
def existsPath(G, x, y):
    m = len(G)
    bucketSort(G)
    n = 0
    for u, v, _ in G:
        n = max(n, u + 1, v + 1)
    

    path = [False for _ in range(n)]
    path[x] = True
    for u, v, c in G:
        path[v] |= path[u]
        path[u] |= path[v]
    
    return path[y]



def bucketSort(G):
    n = len(G)
    buckets = [[] for _ in range(n)]

    for i in range(n):
        buckets[G[i][2] - 1].append(G[i])

    for i in range(n):
        G[i] = buckets[n - 1 - i][0]



G = [(0, 1, 1), (0, 2, 6), (1, 5, 2), (2, 5, 5), (4, 5, 3), (3, 5, 4)]
print(existsPath(G, 0, 4))