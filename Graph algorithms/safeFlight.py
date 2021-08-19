"""
Every edge in the graph G represents air corridor between vertices.
Each air corridor has an optimum flight ceiling for aircraft.
You can fly through a corridor only if the aircraft ceiling differs from optimal ceiling for this corridor by no more than t.
Check whether it is possible to fly from vertex x to vertex y without changing aircraft ceiling.
"""
#time complexity: O(E * (V**2))
def solveEff(G, x, y, t):
    n = len(G)
    E = []    
    for i in range(n):
        for j in range(i + 1, n):
            if G[i][j] > 0:
                E.append((G[i][j], (i, j)))
    

    E.sort()
    m = len(E)
    for i in range(m):
        val = E[i][0] + 2*t
        left = 0
        right = m - 1
        mid = None
        while left <= right:
            mid = (left + right) // 2
            if E[mid][0] <= val:
                left = mid + 1
            else:
                right = mid - 1
        

        GG = [[0 for _ in range(n)] for _ in range(n)]
        for j in range(i, left):
            val, (k, l) = E[j]
            GG[k][l] = val
            GG[l][k] = val
        
        if DFS(GG, x, y):
            return True
    return False



def DFS(G, x, y):
    n = len(G)
    visited = [False for _ in range(n)]

    def DFSVisit(i):
        visited[i] = True
        for j in range(n):
            if not visited[j] and G[i][j] > 0:
                DFSVisit(j)
    
    DFSVisit(x)
    return visited[y]


#does not exist
G = [
    [-1, 70, 75, 105, 0, 0, 0],
    [70, -1, 0, 100, 0, 0, 0],
    [75, 0, -1, 0, 0, 55, 0],
    [105, 100, 0, -1, 70, 0, 0],
    [0, 0, 0, 70, -1, 65, 0],
    [0, 0, 55, 0, 65, -1, 90],
    [0, 0, 0, 0, 0, 90, -1]
]
#exist
G = [
    [-1, 70, 75, 95, 0, 0, 0],
    [70, -1, 0, 100, 0, 0, 0],
    [75, 0, -1, 0, 0, 55, 0],
    [95, 100, 0, -1, 70, 0, 0],
    [0, 0, 0, 70, -1, 65, 0],
    [0, 0, 55, 0, 65, -1, 90],
    [0, 0, 0, 0, 0, 90, -1]
]
print(solveEff(G, 0, 6, 15))