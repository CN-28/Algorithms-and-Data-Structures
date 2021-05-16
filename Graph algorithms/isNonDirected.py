def isNonDirected(G):
    n = len(G)
    A = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(len(G[i])):
            A[i][G[i][j]] = 1
    
    
    for i in range(n):
        for j in range(i, n):
            if A[i][j] != A[j][i]:
                return False
    return True


G = [[3, 4, 5], [4, 5], [3, 5], [0, 2], [0, 1], [0, 1, 2]]
print(isNonDirected(G))