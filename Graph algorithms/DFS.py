#adjacency list
def DFS(G):
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

    for u in range(n):
        if not visited[u]:
            DFSVisit(u)
    
    return pre, post


#adjacency matrix
def DFS(G):
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
        for v in range(n):
            if G[u][v] == 1 and not visited[v]:
                DFSVisit(v)
        proccessed_time += 1
        post[u] = proccessed_time

    for u in range(n):
        if not visited[u]:
            DFSVisit(u)
    
    return pre, post