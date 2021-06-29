#EXAM 2020
def find_cost(P):
    n = len(P)
    G = [[-1 for _ in range(n)] for _ in range(n)]
    min_index = P.index(min(P))
    max_index = P.index(max(P))

    
    count = [[0 for _ in range(10)] for _ in range(n)]
    for i in range(n):
        temp = P[i]
        while temp != 0:
            count[i][temp % 10] += 1
            temp //= 10
    
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            for k in range(10):
                if count[i][k] > 0 and count[j][k] > 0:
                    G[i][j] = abs(P[i] - P[j])
                    G[j][i] = abs(P[i] - P[j])
                    break


    return dijkstraAM(G, min_index, max_index)
    


def dijkstraAM(G, s, t):
    n = len(G)
    visited = [False for _ in range(n)]
    dist = [float("inf") for _ in range(n)]
    parent = [-1 for _ in range(n)]
    dist[s] = 0


    for i in range(n):
        mini = float("inf")
        for j in range(n):
            if dist[j] < mini and not visited[j]:
                mini = dist[j]
                u = j
            

        visited[u] = True
        for j in range(n):
            if G[u][j] > 0 and not visited[j] and dist[j] > dist[u] + G[u][j]:
                dist[j] = dist[u] + G[u][j]
                parent[j] = u

    if dist[t] != float("inf"):
        return dist[t]
    else:
        return -1