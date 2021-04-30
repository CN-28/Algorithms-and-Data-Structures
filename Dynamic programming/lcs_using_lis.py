#find the longest increasing subsequence using longest common subsequence
def lcs(A):
    n = len(A)
    B = sorted(A)
    F = [[None]*(n + 1) for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                F[i][j] = 0
            elif A[i - 1] == B[j - 1]:
                F[i][j] = F[i - 1][j - 1] + 1
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])
    
    return F[n][n]

Arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

print(lcs(Arr))