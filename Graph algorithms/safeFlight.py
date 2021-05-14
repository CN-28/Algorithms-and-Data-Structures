"""
Every edge in the graph G represents air corridor between vertices.
Each air corridor has an optimum flight ceiling for aircraft.
You can fly through a corridor only if the aircraft ceiling differs from optimal ceiling for this corridor by no more than t.
Check whether it is possible to fly from vertex x to vertex y without changing aircraft ceiling.
"""
def solve(G, x, y, t):
    n = len(G)
    visited = [False for _ in range(n)]
    def DFSVisit(i, visited, mini=float("inf"), maxi=0):
        visited[i] = True
        if i == y:
            if maxi - mini <= 2 * t:
                return True
        

        for j in range(n):
            if G[i][j] != 0 and G[i][j] != -1 and not visited[j]:
                if DFSVisit(j, visited, min(G[i][j], mini), max(maxi, G[i][j])):
                    return True
        
        
        visited[i] = False

    
    if DFSVisit(x, visited):
        return True
    return False 



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
print(solve(G, 0, 6, 15))