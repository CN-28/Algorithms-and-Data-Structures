def min_cost(T):
    N = len(T)
    F = [[0] * N for _ in range(N)]
    F[0][0] = T[0][0]

    for i in range(1, N):
        F[i][0] = T[i][0] + F[i - 1][0]

    for i in range(1, N):
        F[0][i] = T[0][i] + F[0][i - 1]

    for i in range(1, N):
        for j in range(1, N):
            if F[i - 1][j] < F[i][j - 1]:
                F[i][j] = F[i - 1][j] + T[i][j]
            else:
                F[i][j] = F[i][j - 1] + T[i][j]

    return F[N - 1][N - 1], F


T = [
    [2, 8, 3, 1],
    [1, 4, 5, 2],
    [5, 8, 7, 2],
    [1, 9, 2, 3]
]

res, F = min_cost(T)
print(res)