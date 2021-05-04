"""
two dimensional knapsack problem, H - max height of the knapsack, W - max weight for the knapsack
we place items on top of each other
Time complexity: O(n*W*H)
"""
def solve(P, W, H):
    n = len(P)
    F = [[[0 for _ in range(H + 1)] for _ in range(W + 1)] for _ in range(n)]


    for j in range(1, W + 1):
        for k in range(1, H + 1):
            if j >= P[0][1] and k >= P[0][2]:
                F[0][j][k] = P[0][0]
    
    
    for i in range(1, n):
        for j in range(1, W + 1):
            for k in range(1, H + 1):
                F[i][j][k] = F[i - 1][j][k]
                if j >= P[i][1] and k >= P[i][2]:
                    F[i][j][k] = max(F[i - 1][j - P[i][1]][k - P[i][2]] + P[i][0], F[i][j][k])
    

    return F[n - 1][j][k]



W = 4
H = 6
P = [(2, 3, 4), (1, 1, 1), (4, 1, 2), (8, 1, 1), (5, 2, 3), (3, 4, 5)]
print(solve(P, W, H))