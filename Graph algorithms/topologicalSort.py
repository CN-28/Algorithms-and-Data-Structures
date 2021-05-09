def topological_sort(G):
    n = len(G)
    visited = [False for _ in range(n)]
    top_sorted = []
    def DFSVisit(i):
        visited[i] = True
        for j in range(n):
            if G[i][j] == 1 and not visited[j]:
                DFSVisit(j)
        top_sorted.append(i)


    for i in range(n):
        if not visited[i]:
            DFSVisit(i)
    
    return top_sorted[::-1]

G = [
    [0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(topological_sort(G))