#time complexity: O(E)
def decreasing_path(G, x, y):
    m = len(G)
    bucketSort(G)
    
    n = 0
    for u, v, c in G:
        n = max(n, u + 1, v + 1)

    
    dist = [float("inf") for _ in range(n)]
    dist[x] = 0
    for u, v, c in G:
        if dist[u] + c < dist[v]:
            dist[v] = dist[u] + c
        if dist[v] + c < dist[u]:
            dist[u] = dist[v] + c
    
    return dist[y]



def bucketSort(G):
    n = len(G)
    buckets = [[] for _ in range(n)]

    for i in range(n):
        buckets[G[i][2] - 1].append(G[i])

    for i in range(n):
        G[i] = buckets[n - 1 - i][0]



G = [(0, 1, 7), (0, 4, 4), (1, 2, 6), (4, 5, 3), (4, 3, 5), (2, 3, 1), (2, 4, 2)]
print(decreasing_path(G, 0, 3))

G = [(0, 1, 12), (1, 2, 10), (0, 4, 8), (1, 4, 11), (4, 5, 7), (4, 6, 4), (5, 6, 6), (2, 3, 2), (2, 5, 9), (3, 6, 3), (6, 7, 5), (3, 7, 14), (3, 8, 13), (7, 8, 1)]
print(decreasing_path(G, 0, 8))