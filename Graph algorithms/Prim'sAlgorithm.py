from queue import PriorityQueue


def prim(G):
    n = len(G)
    mst = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    queue = PriorityQueue()
    

    cost = 0
    visited[0] = True
    for i in range(len(G[0])):
        queue.put((G[0][i][1], 0, G[0][i][0]))

    while not queue.empty():
        c, prev, curr = queue.get()
        if not visited[curr]:
            visited[curr] = True
            mst[prev].append(curr)
            cost += c
            for v, w in G[curr]:
                if not visited[v]:
                    queue.put((w, curr, v))

    return mst, cost


G = [[(3, 1), (4, 2), (5, 3)], [(4, 2), (5, 3)], [(3, 5), (5, 4)], [(0, 1), (2, 5)], [(0, 2), (1, 2)], [(0, 3), (1, 3), (2, 4)]]
print(prim(G))