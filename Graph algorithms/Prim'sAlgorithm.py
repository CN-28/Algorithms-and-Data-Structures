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
        t = queue.get()
        if not visited[t[2]]:
            visited[t[2]] = True
            mst[t[1]].append(t[2])
            cost += t[0]
            for i in range(len(G[t[2]])):
                if not visited[G[t[2]][i][0]]:
                    queue.put((G[t[2]][i][1], t[2], G[t[2]][i][0]))

    return mst, cost


G = [[(3, 1), (4, 2), (5, 3)], [(4, 2), (5, 3)], [(3, 5), (5, 4)], [(0, 1), (2, 5)], [(0, 2), (1, 2)], [(0, 3), (1, 3), (2, 4)]]
print(prim(G))