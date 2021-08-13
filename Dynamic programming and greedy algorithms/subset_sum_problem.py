def subsetSum(A, T):
    n = len(A)
    F = [[False for _ in range(T + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        F[i][0] = True

    for i in range(1, n + 1):
        for j in range(T + 1):
            if j < A[i - 1]:
                F[i][j] = F[i - 1][j]
            else:
                F[i][j] = F[i - 1][j] or F[i - 1][j - A[i - 1]]
    
    return F[n][T]



A = [5, 3, 1, 4, 7, 2, 9]
print(subsetSum(A, 25))