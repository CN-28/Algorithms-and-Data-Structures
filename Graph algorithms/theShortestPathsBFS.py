from collections import deque

def find(G, Vs, Vf):
    n = len(G)
    queue = deque()
    visited = [False for _ in range(n)]
    distance = [float("inf") for _ in range(n)]
    parent = [-1 for _ in range(n)]


    visited[Vs] = True
    distance[Vs] = 0
    queue.append((G[Vs], Vs))
    while queue:
        u = queue.popleft()
        for i in range(len(u[0])):
            if not visited[u[0][i]]:
                visited[u[0][i]] = True
                parent[u[0][i]] = u[1]
                distance[u[0][i]] = distance[u[1]] + 1
                queue.append((G[u[0][i]], u[0][i]))
    

    path = []
    v = Vf
    while v != -1:
        path.append(v)
        v = parent[v]

   
    for i in range(len(path) - 1, -1, -1):
        if i != 0:
            print(path[i], end=" ---> ")
        else:
            print(path[i])
    

    return distance[Vf]



G = [[3, 4, 5], [4, 5], [3, 5], [0, 2], [0, 1], [0, 1, 2]]
print(find(G, 0, 1))