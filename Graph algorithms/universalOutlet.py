"""
Find the vertex to which there is an edge from every other vertex,
and from this vertex there is no edge to any other vertex.
"""
#O(n^2) solution
def solve(G):
    n = len(G)
    Arr = []
    for i in range(n):
        temp = True
        for j in range(n):
            if G[i][j] == 1:
                temp = False
                break
        if temp:
            Arr.append(i)
    

    for x in Arr:
        temp = True
        for j in range(n):
            if G[j][x] == 0:
                temp = False
                break
        if temp:
            return x
    

    return False



#O(n) solution
def solveFaster(G):
    n = len(G)
    i = 0
    j = 0
    while j < n and (G[i][j] == 0 or G[i][j] == -1):
        j += 1
        while j < n and G[i][j] == 1:
            i += 1
    
    
    for j in range(n):
        if G[i][j] == 1 or G[j][i] == 0:
            return False
    

    return i
           


G = [
    [-1, 1, 1, 0, 0, 1],
    [1, -1, 1, 1, 1, 1],
    [1, 0, -1, 0, 0, 1],
    [1, 1, 1, -1, 1, 1],
    [1, 1, 1, 0, -1, 1],
    [0, 0, 0, 0, 0, -1]
]
print(solve(G))
print(solveFaster(G))