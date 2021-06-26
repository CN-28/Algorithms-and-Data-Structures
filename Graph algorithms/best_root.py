#EXAM 2020, task 1, third exam date
#Time complexity: O(V + E)
from collections import deque
def BFS(L, t):
    n = len(L)
    visited = [False for _ in range(n)]
    dist = [float("inf") for _ in range(n)]
    Q = deque()
    
    visited[t] = True
    dist[t] = 0
    Q.append(t)
    while Q:
        u = Q.popleft()
        for v in L[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                Q.append(v)
    return dist



def best_root( L ):
    ind1 = DFS(L)
    Arr1 = BFS(L, ind1)
    Arr2 = BFS(L, Arr1.index(max(Arr1)))
    mini = float("inf")
    index = -1
    for i in range(len(Arr1)):
        if Arr1[i] == Arr2[i] and Arr1[i] < mini:
            mini = Arr1[i]
            index = i
    return index



def DFS(G, i=0):
    n = len(G)
    visited = [False for _ in range(n)]
    pre = [0 for _ in range(n)]
    post = [0 for _ in range(n)]
    entry_time = 0
    proccessed_time = 0
    def DFSVisit(u):
        nonlocal entry_time, proccessed_time
        entry_time += 1
        pre[u] = entry_time
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFSVisit(v)
        proccessed_time += 1
        post[u] = proccessed_time
    DFSVisit(i)
    visited[i] = True
    for u in range(n):
        if not visited[u]:
            DFSVisit(u)
    return pre.index(max(pre))



A = [[2], [2], [0, 1, 3, 4, 5, 6], [2], [2], [2], [2]] 
print(best_root(A))