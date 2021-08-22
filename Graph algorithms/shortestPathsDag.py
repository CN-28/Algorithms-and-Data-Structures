#find the shortest paths from source in DAG, time complexity: O(V + E)
def topological_sort(G, s):
    n = len(G)
    visited = [False for _ in range(n)]
    top_sorted = []
    def DFSVisit(i):
        visited[i] = True
        for v, c in G[i]:
            if not visited[v]:
                DFSVisit(v)
        top_sorted.append(i)

    for i in range(n):
        if not visited[i]:
            DFSVisit(i)


    return top_sorted



def shortestPaths(G, s):
    n = len(G)
    dist = [float("inf") for _ in range(n)]
    top_sorted = topological_sort(G, s)
    dist[s] = 0


    while top_sorted:
        u = top_sorted.pop()
        if dist[u] != float("inf"):
            for v, w in G[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    return dist



G = [
    [(1, 1), (4, 8)],
    [(2, 2)],
    [(3, 4)],
    [],
    [(3, 1)]
]
print(shortestPaths(G, 0))