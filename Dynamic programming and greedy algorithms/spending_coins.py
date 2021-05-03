def mincoins(coins, T):
    n = len(coins)

    F = [float("inf") for _ in range(T + 1)]
    F[0] = 0
    for i in range(1, T + 1):
        for j in range(n):
            if coins[j] <= i and F[i-coins[j]] + 1 < F[i]:
                F[i] = F[i-coins[j]] + 1

    return F[T]


T = 25
coins = [1, 5, 8]
print(mincoins(coins, T))