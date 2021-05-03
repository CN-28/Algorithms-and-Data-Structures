def lcs(A, B):
    len_A = len(A)
    len_B = len(B)

    F = [[None]*(len_B + 1) for i in range(len_A + 1)]

    for i in range(len_A + 1):
        for j in range(len_B + 1):
            if i == 0 or j == 0:
                F[i][j] = 0
            elif A[i - 1] == B[j - 1]:
                F[i][j] = F[i - 1][j - 1] + 1
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])
    
    return F[len_A][len_B]

A = "AGGTAB"
B = "GXTXAYB"

print(lcs(A, B))