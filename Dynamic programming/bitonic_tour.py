from math import *

C = [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1]]

def bitonicTSP( C ):
    n = len(C)
    C.sort(key = lambda x: x[1])
    D = [[round(((C[i][1] - C[j][1])**2 + (C[i][2] - C[j][2])**2)**(1/2), 2) for j in range(n)] for i in range(n)]
    R = [[-1]*n for _ in range(n)]



    F = [[float("inf")]*n for i in range(n)]
    F[0][1] = D[0][1]

    def tspf(i, j, F, D, R):
        if F[i][j] != float("inf"):
            return F[i][j]
        
        if i == j - 1:
            index = -1
            best = float("inf")
            for k in range(j - 1):
                if tspf(k, j - 1, F, D, R) + D[k][j] < best:
                    best = tspf(k, j - 1, F, D, R) + D[k][j]
                    index = k

            R[j - 1][j] = index
            F[j - 1][j] = best

        else:
            F[i][j] = tspf(i, j - 1, F, D, R) + D[j - 1][j]
            R[i][j] = j - 1

        return F[i][j]
    
    res = float("inf")
    for i in range(n - 1):
        res = min(res, tspf(i, n - 1, F, D, R) + D[i][n - 1])
    print(res)


    T = []
    S = [[] for _ in range(2)]
    k = 0
    i = n - 2
    j = n - 1
    while j > 0:
        S[k].append(j)
        j = R[i][j]
        if j < i:
            i, j = j, i
            k = 1 - k
    
    S[0].append(0)
    while len(S[1]) > 0:
        S[0].append(S[1].pop())
    
    for i in range(n):
        T.append(C[S[0].pop()])
    
    for i in range(n//2 - 1, n):
        print(T[i][0], end=" ")

    for i in range(0, n//2):
        print(T[i][0], end=" ")


bitonicTSP( C )