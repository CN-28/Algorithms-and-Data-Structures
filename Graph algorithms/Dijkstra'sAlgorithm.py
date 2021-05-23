from queue import PriorityQueue


def dijkstra(G, V_s):
    n = len(G)
    visited = [False for _ in range(n)]
    dist = [float('inf') for _ in range(n)]
    parent = [-1 for _ in range(n)]
    dist[V_s] = 0
    

    queue = PriorityQueue()
    queue.put((dist[V_s], V_s))
    while not queue.empty():
        c, u = queue.get()
        visited[u] = True
        for v, w in G[u]:
            if not visited[v]:
                if c + w < dist[v]:
                    dist[v] = c + w
                    parent[v] = u
                    queue.put((c + w, v))


    return parent, dist


G = [[(3, 1), (4, 2), (5, 3)], [(4, 2), (5, 3)], [(3, 5), (5, 4)], [(0, 1), (2, 5)], [(0, 2), (1, 2)], [(0, 3), (1, 3), (2, 4)]]
print(dijkstra(G, 0))