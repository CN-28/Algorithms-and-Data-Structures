"""
Alice and Bob are on trip. They are driving in turns and car driver is being changed after every city.
Find the shortest path from source to destination, that Alice drove least miles.
Alice get to choose who drives the car first.
"""
from queue import PriorityQueue
def twoDrivers(G, x, y):
    n = len(G)
    dist_taken = [float("inf") for _ in range(n)]
    parent_taken = [-1 for _ in range(n)]
    dist_nontaken = [float("inf") for _ in range(n)]
    parent_nontaken = [-1 for _ in range(n)]
    Q = PriorityQueue()


    Q.put((0, x))
    dist_taken[x] = 0
    dist_nontaken[x] = 0
    while not Q.empty():
        c, u = Q.get()
        for v, w in G[u]:
            temp = False
            if dist_nontaken[u] + w < dist_taken[v]:
                dist_taken[v] = dist_nontaken[u] + w
                parent_taken[v] = u
                temp = True
            
            if dist_taken[u] < dist_nontaken[v]:
                dist_nontaken[v] = dist_taken[u]
                parent_nontaken[v] = u
                temp = True
            
            if temp:
                Q.put((min(dist_taken[v], dist_nontaken[v]), v))


    path = []
    temp = y
    if dist_nontaken[y] < dist_taken[y]:
        last = "nt"
        while temp != -1:
            path.append(temp)
            if last == "nt":
                temp = parent_nontaken[temp]
                last = "t"
            else:
                temp = parent_taken[temp]
                last = "nt"

        path = path[::-1]
        index = -1
        if len(path) - 2 >= 0:
            index = path[len(path) - 2]
        while True:
            if index - 2 < 0:
                break
            index -= 2
        if index <= 0:
            return dist_nontaken[y], path, "Alice drives second"
        else:
            return dist_nontaken[y], path, "Alice drives first"

    else:
        last = "t"
        while temp != -1:
            path.append(temp)
            if last == "nt":
                temp = parent_nontaken[temp]
                last = "t"
            else:
                temp = parent_taken[temp]
                last = "nt"
        
        path = path[::-1]
        index = -1
        if len(path) - 1 >= 0:
            index = path[len(path) - 1]
        while True:
            if index - 2 < 0:
                break
            index -= 2
        if index <= 0:
            return dist_taken[y], path, "Alice drives second"
        else:
            return dist_taken[y], path, "Alice drives first"
    


G = [
    [(1, 200), (3, 300)],
    [(0, 200), (2, 6)],
    [(1, 6), (3, 200)],
    [(2, 200), (0, 300), (4, 500)],
    [(3, 500), (5, 1)],
    [(4, 1)]
]
print(twoDrivers(G, 0, 5))