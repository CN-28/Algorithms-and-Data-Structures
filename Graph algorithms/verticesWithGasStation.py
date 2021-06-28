class station:
    def __init__(self):
        self.stat = float("inf")
        self.statFuel = 0
        self.nonstat = float("inf")
        self.nonstatFuel = 0



def jak_dojade(G, P, d, a, b):
    def dijkstraAM(G, P, a, b, d):
        n = len(G)
        visited = [False for _ in range(n)]
        dist = [station() for _ in range(n)]
        parent = [((-1, 0), (-1, 1)) for _ in range(n)]
        dist[a].stat = 0
        dist[a].nonstat = 0
        dist[a].statFuel = d
        dist[a].nonstatFuel = d


        for i in range(n):
            mini = float("inf")
            for j in range(n):
                if min(dist[j].stat, dist[j].nonstat) < mini and not visited[j]:
                    mini = min(dist[j].stat, dist[j].nonstat)
                    u = j
                

            visited[u] = True
            for j in range(n):
                if not visited[j] and G[u][j] > 0:
                    if u == a or u not in P:
                        if G[u][j] <= dist[u].nonstatFuel and dist[j].nonstat > dist[u].nonstat + G[u][j]:
                            dist[j].nonstat = dist[u].nonstat + G[u][j]
                            dist[j].nonstatFuel = dist[u].nonstatFuel - G[u][j]
                            if j in P:
                                dist[j].nonstatFuel = d
                            parent[j] = (u, 0), parent[j][1] 
                        elif G[u][j] <= dist[u].statFuel and dist[j].nonstat > dist[u].stat + G[u][j]:
                            dist[j].nonstat = dist[u].stat + G[u][j]
                            dist[j].nonstatFuel = dist[u].stat - G[u][j]
                            if j in P:
                                dist[j].nonstatFuel = d
                            parent[j] = (u, 1), parent[j][1] 
                    else:
                        if dist[j].stat > dist[u].stat + G[u][j] and dist[u].statFuel >= G[u][j]:
                            dist[j].stat = dist[u].stat + G[u][j]
                            dist[j].statFuel = d - G[u][j]
                            if j in P:
                                dist[j].statFuel = d
                            parent[j] = parent[j][0], (u, 1) 
                        if dist[j].stat > dist[u].nonstat + G[u][j] and dist[u].nonstatFuel >= G[u][j]:
                            dist[j].stat = dist[u].nonstat + G[u][j]
                            dist[j].statFuel = d - G[u][j]
                            if j in P:
                                dist[j].statFuel = d
                            parent[j] = parent[j][0], (u, 0) 

        if dist[b].nonstat < dist[b].stat:
            return parent, 0
        else:
            return parent, 1
    parent, which = dijkstraAM(G, P, a, b, d)
    temp = b
    res = []
    while True:
        res.append(temp)
        temp, which = parent[temp][which]
        if temp == a:
            res.append(temp)
            break
        if temp == -1:
            return None

    return res[::-1]


G = [
[-1, 5, -1, 2],
[-1, -1, -1, -1],
[5, -1, -1, 5],
[2, 2, -1, -1]
]
P = [2, 0]
d =  6
a =  2
b =  1
print(jak_dojade(G, P, d, a, b))