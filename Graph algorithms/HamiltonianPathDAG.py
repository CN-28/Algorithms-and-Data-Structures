#find hamiltonian path in DAG, time complexity: O(V + E)
def topological_sort(G):
    n = len(G)
    visited = [False for _ in range(n)]
    top_sorted = []
    def DFSVisit(i):
        visited[i] = True
        for j in range(len(G[i])):
            if not visited[G[i][j]]:
                DFSVisit(G[i][j])
        top_sorted.append(i)


    for i in range(n):
        if not visited[i]:
            DFSVisit(i)
    

    return top_sorted



def DFSVis(G, visited, top_sorted, i):
    visited[top_sorted[i]] = True
    for v in G[top_sorted[i]]:
        if i - 1 >= 0 and not visited[v] and v == top_sorted[i - 1]:
            if DFSVis(G, visited, top_sorted, i - 1):
                return True
            else:
                return False


    for check in visited:
        if not check:
            return False
    return True



G = [[], [0, 2], [0], [1, 2]]
top_sorted = topological_sort(G)
visited = [False for _ in range(len(G))]
print(DFSVis(G, visited, top_sorted, top_sorted[len(top_sorted) - 1]))