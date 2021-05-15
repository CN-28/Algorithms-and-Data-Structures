"""
A - nxn chessboard. The king travells across the board. He starts in the upper left corner and 
he must get to the bottom right corner. Each field (i, j) has an entry cost of between 1 and 5, placed on the field (j, i).
Find the cost of the king's path with mimimum total cost.
"""
from collections import deque
from random import randint


def save(G_mod, curr, next, A, M, n):
    if next[0] >= n or next[0] < 0 or next[1] >= n or next[1] < 0:
        return
    

    weight = A[next[1]][next[0]]
    for k in range(weight - 1):
        G_mod[curr[0]*n + curr[1] + k*M].append(curr[0]*n + curr[1] + (k + 1)*M)
    G_mod[curr[0]*n + curr[1] + (weight - 1)*M].append(next[0]*n + next[1])



def getEdges(A, n):
    #M - number of vertices
    M = n**2
    G_mod = [[] for _ in range(5*M)]
    for i in range(n):
        for j in range(n):
            curr = i, j
            save(G_mod, curr, (i + 1, j), A, M, n)
            save(G_mod, curr, (i + 1, j + 1), A, M, n)
            save(G_mod, curr, (i + 1, j - 1), A, M, n)
            save(G_mod, curr, (i - 1, j), A, M, n)
            save(G_mod, curr, (i - 1, j - 1), A, M, n)
            save(G_mod, curr, (i - 1, j + 1), A, M, n)
            save(G_mod, curr, (i, j + 1), A, M, n)
            save(G_mod, curr, (i, j - 1), A, M, n)
    

    return G_mod



def getCost(parent, A, u, Vs, n, cost=0):
    while u != Vs:
        if u < n*n:
            print(u, end="<--- ")
        cost += 1
        u = parent[u]
    print(Vs)
    cost += A[Vs % n][Vs // n]
    
    return cost



def findMinCost(G, A, Vs, Vf, n):
    N = len(G)
    visited = [False for _ in range(N)]
    parent = [-1 for _ in range(N)]
    visited[Vs] = True


    queue = deque()
    queue.append(Vs)
    while queue:
        u = queue.popleft()
        if u == Vf:
            return getCost(parent, A, u, Vs, n)


        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
                parent[v] = u
        


n = 6
A = [[randint(1, 5) for _ in range(n)] for _ in range(n)]
for x in A:
    print(x)
G = getEdges(A, n)
print(findMinCost(G, A, 0, n**2 - 1, n))