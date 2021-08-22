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

    DFSVisit(s)
    

    return top_sorted



def shortestPaths(G, v_s):
    n = len(G)
    dist = [float("inf") for _ in range(n)]
    top_sorted = topological_sort(G, v_s)
    dist[v_s] = 0


    while top_sorted:
        v = top_sorted.pop()
        for u, w in G[v]:
            if dist[u] > dist[v] + w:
                dist[u] = dist[v] + w

    return dist



G = [
    [(1, 1), (4, 8)],
    [(2, 2)],
    [(3, 4)],
    [],
    [(3, 1)]
]
print(shortestPaths(G, 0))