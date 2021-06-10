#find the shortest paths from source in DAG, time complexity: O(V + E)
def topological_sort(G):
    n = len(G)
    visited = [False for _ in range(n)]
    top_sorted = []
    def DFSVisit(i):
        visited[i] = True
        for j in range(len(G[i])):
            if not visited[G[i][j][0]]:
                DFSVisit(G[i][j][0])
        top_sorted.append(i)


    for i in range(n):
        if not visited[i]:
            DFSVisit(i)
    

    return top_sorted



def shortestPaths(G, v_s):
    n = len(G)
    dist = [float("inf") for _ in range(n)]
    top_sorted = topological_sort(G)
    dist[v_s] = 0


    while top_sorted:
        v = top_sorted.pop()
        for u, w in G[v]:
            if dist[u] > dist[v] + w:
                dist[u] = dist[v] + w

    return dist



G = [[(1, 40), (2, 5)], [(3, 20)], [(3, 2)], []]
print(shortestPaths(G, 0))