#Time complexity: O(V^3), space complexity: O(V^2)
"""
There is an undirected, weighted (E -> N) graph G and a two-mile shoes.
Two-mile shoes allow you to jump through two edges at one time, paying only for maximum of these two edges.
Between each use of two-mile shoes you must go through at least 1 edge without the mile-shoes.
Find the minimum cost to get from the vertex s to the vertex t.
"""
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


G = [
[0, 1, 0, 0],
[1, 0, 2, 0],
[0, 2, 0, 3],
[0, 0, 3, 0]
]
print(jumper(G, 0, 3))