#Knapsack problem, time complexity: O(n * (from i = 0 to n - 1)∑(P[i]))
def knapsackSum(W, P, MaxW):
    n = len(W)
    MaxSum = 0
    for i in range(n):
        MaxSum += P[i]
    
    F = [[float("inf") for _ in range(MaxSum + 1)] for _ in range(n)]
    for i in range(n):
        F[i][0] = 0
    F[0][P[0]] = W[0]

    for i in range(1, n):
        for s in range(MaxSum + 1):
            if s < P[i]:
                F[i][s] = F[i - 1][s]
            else:
                F[i][s] = min(F[i - 1][s], F[i - 1][s - P[i]] + W[i])
    

    for s in range(MaxSum, -1, -1):
        if F[n - 1][s] <= MaxW:
            return s, F
    


def getSolution(F, W, P, i, s):
    if i == 0:
        if s >= P[0]:
            return [0]
        return []

    if s >= P[i] and F[i][s] == F[i - 1][s - P[i]] + W[i]:
        return getSolution(F, W, P, i - 1, s - P[i]) + [i]
    return getSolution(F, W, P, i - 1, s)



P = [10, 8, 4, 5, 3, 7]
W = [4, 5, 12, 9, 1, 13]
res, F = knapsackSum(W, P, 15)
print(res, getSolution(F, W, P, len(W) - 1, res))