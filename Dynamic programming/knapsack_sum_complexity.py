def knapsack(W, P, MaxW):
    n = len(W)
    suum = 0
    for i in range(len(P)):
        suum += P[i]
    F = [[0]*(suum + 1) for i in range(n)]

    F[0][P[0]] = W[0]

    for i in range(1, n):
        for j in range(1, suum + 1):
            
            F[i][j] = F[i - 1][j]
            if j - P[i] == 0 and F[i - 1][j] == 0:
                F[i][j] = W[i]
            elif F[i - 1][j - P[i]] != 0 and F[i][j] == 0:
                F[i][j] = F[i - 1][j - P[i]] + W[i]
            elif F[i - 1][j - P[i]] != 0 and F[i][j] != 0:
                F[i][j] = min(F[i - 1][j - P[i]] + W[i], F[i][j])
                
    for i in range(suum, -1, -1):
        if F[n - 1][i] != 0 and F[n - 1][i] <= MaxW:
            return F[n - 1][i], i, F



P = [10, 8, 4, 5, 3, 7]
W = [4, 5, 12, 9, 1, 13]
print(knapsack(W, P, 15)[0])

F = knapsack(W, P, 15)[2]
j = knapsack(W, P, 15)[1]
for i in range(len(F) - 1, 0, -1):
    if F[i - 1][j] == 0:
        j = j - P[i]
        print(i)
    elif F[i - 1][j] != F[i][j]:
        print(i)
if F[0][j] != 0:
    print(0)