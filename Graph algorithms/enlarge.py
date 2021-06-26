from collections import deque
def enlarge(G, s, t):
    def BFS(G, w):
        n = len(G)
        visited = [False for _ in range(n)]
        dist = [float("inf") for _ in range(n)]
        parent = [-1 for _ in range(n)]
        Q = deque()


        Q.append(w)
        dist[w] = 0
        visited[w] = True
        while Q:
            u = Q.popleft()
            for v in G[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    dist[v] = dist[u] + 1
                    Q.append(v)
            
        return dist, parent


    Arr1, parent = BFS(G, s)
    Arr2 = BFS(G, t)[0]
    tempArr = [0 for _ in range(Arr1[t] + 1)]
    for i in range(len(Arr1)):
        if Arr1[i] + Arr2[i] == Arr1[t]:
            tempArr[Arr1[i]] += 1


    res = -1, -1
    for i in range(1, len(tempArr)):
        if tempArr[i - 1] == tempArr[i] == 1:
            res = i - 1, i
            break
    

    temp = t
    while temp != -1:
        if res[1] == Arr1[temp] and res[0] == Arr1[parent[temp]]:
            return (parent[temp], temp)
        temp = parent[temp]