#EXAM 2021, task 3, 0 exam date
"""
There is an undirected, weighted (E -> N) graph G and a two-mile shoes.
Two-mile shoes allow you to jump through two edges at one time, paying only for maximum of these two edges.
Between each use of two-mile shoes you must go through at least 1 edge without the mile-shoes.
Find the minimum cost to get from the vertex s to the vertex t.
"""
#using Bellman-Ford, time complexity: O(V**3 + V**3)
def jumper(G, s, t):
    n = len(G)
    dist = [(float("inf"), float("inf")) for _ in range(n)]
    jumpEdges = [[float("inf") for _ in range(n)] for _ in range(n)]


    dist[s] = 0, 0
    for u in range(n):
        for v in range(n):
            for w in range(n):
                if u == v:
                    break
                if u == w or v == w:
                    continue
                    
                if G[u][w] != 0 and G[w][v] != 0:
                    jumpEdges[u][v] = min(jumpEdges[u][v], max(G[u][w], G[w][v]))
    


    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                if G[u][v] != 0:
                    dist[v] = min(dist[v][0], min(dist[u]) + G[u][v]), dist[v][1]
                

                dist[v] = dist[v][0], min(dist[v][1], dist[u][0] + jumpEdges[u][v])


    return min(dist[t])



#using Dijkstra, time complexity: O(V**3 + V**2)
def jumper1(G, s, t):
    n = len(G)
    jumpEdges = [[float("inf") for _ in range(n)] for _ in range(n)]


    for u in range(n):
        for v in range(n):
            for w in range(n):
                if u == v:
                    break
                if u == w or v == w:
                    continue
                    
                if G[u][w] != 0 and G[w][v] != 0:
                    jumpEdges[u][v] = min(jumpEdges[u][v], max(G[u][w], G[w][v]))
    
    
    def dijkstraAM(G, s, t, jumpEdges):
        n = len(G)
        visited = [False for _ in range(n)]
        dist = [(float("inf"), float("inf")) for _ in range(n)]
        parent = [-1 for _ in range(n)]
        dist[s] = 0, 0

        
        for i in range(n):
            mini = float("inf")
            for j in range(n):
                if not visited[j]:
                    if min(dist[j]) < mini:
                        mini = min(dist[j])
                        u = j
                    
                    
            visited[u] = True
            for j in range(n):
                if not visited[j]:
                    if G[u][j] > 0 and dist[j][0] > min(dist[u][0], dist[u][1]) + G[u][j]:
                        dist[j] = min(dist[u][0], dist[u][1]) + G[u][j], dist[j][1]
                        parent[j] = u
            

                    if dist[j][1] > dist[u][0] + jumpEdges[u][j]:
                        dist[j] = dist[j][0], dist[u][0] + jumpEdges[u][j]
                        parent[j] = u


        return min(dist[t])


    return dijkstraAM(G, s, t, jumpEdges)



G = [
[0, 1, 0, 0],
[1, 0, 2, 0],
[0, 2, 0, 3],
[0, 0, 3, 0]
]
print(jumper(G, 0, 3))
print(jumper1(G, 0, 3))