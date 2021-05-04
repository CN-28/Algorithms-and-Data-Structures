def solve(A, L):
    n = len(A)
    F = [[[None for _ in range(L + 1)] for _ in range(L + 1)] for i in range(n)]
    

    for j in range(L + 1):
        for k in range(L + 1):
            if j - A[0] >= 0:
                F[0][j][k] = 1
            if k - A[0] >= 0:
                F[0][j][k] = 1
        

    for i in range(1, n):
        for j in range(L + 1):
            for k in range(L + 1):
                if j - A[i] >= 0:
                    F[i][j][k] = F[i - 1][j - A[i]][k]
                if k - A[i] >= 0:
                    F[i][j][k] = F[i - 1][j][k - A[i]]
    
    
    cnt = 0
    for i in range(n):
        for j in range(L + 1):
            for k in range(L + 1):
                if F[i][j][k]:
                    cnt = i + 1
    
    
    return cnt
                    
                

L = 5
A = [5, 3, 2, 6, 4, 1, 7, 4]
print(solve(A, L))