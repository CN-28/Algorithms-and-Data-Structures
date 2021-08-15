def ferryLoading(A, L):
    n = len(A)
    F = [[[False for _ in range(L + 1)] for _ in range(L + 1)] for _ in range(n)]
    for i in range(L + 1):
        for j in range(L + 1):
            if i - A[0] >= 0 or j - A[0] >= 0:
                F[0][i][j] = True


    for i in range(1, n):
        for j in range(A[i], L + 1):
            for k in range(A[i], L + 1):
                F[i][j][k] = F[i - 1][j - A[i]][k] or F[i - 1][j][k - A[i]]
    

    cnt = 0
    for i in range(n):
        for j in range(L + 1):
            for k in range(L + 1):
                if F[i][j][k]:
                    cnt = i + 1
    
    return cnt



A = [5, 3, 2, 6, 4, 1, 7, 4]
print(ferryLoading(A, 15))