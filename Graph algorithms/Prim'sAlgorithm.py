from queue import PriorityQueue


def prim(G):
    n = len(G)
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    queue = PriorityQueue()
    

    cost = 0
    queue.put((0, 0, -1))

    while not queue.empty():
        c, u, prev = queue.get()
        if not visited[u]:
            parent[u] = prev
            cost += c 
        visited[u] = True
        for v, w in G[u]:
            if not visited[v]:
                queue.put((w, v, u))


    return cost, parent


G = [[(3, 1), (4, 2), (5, 3)], [(4, 2), (5, 3)], [(3, 5), (5, 4)], [(0, 1), (2, 5)], [(0, 2), (1, 2)], [(0, 3), (1, 3), (2, 4)]]
G = [[(1, 1), (2, 12)], [(0, 1), (2, 7), (4, 5)], [(0, 12), (1, 7), (4, 6), (3, 8)], [(2, 8), (4, 4), (5, 9)], [(1, 5), (2, 6), (3, 4), (5, 3000)], [(4, 3000), (3, 9)]]
print(prim(G))