"""
Find the minimum number of frog jumps to get from index 0 to n - 1, with given
array A with energy potions on each index, to get to i-th index from j-th frog need to consume
i - j energy points, frog starts with 0 energy points, and energy points mustn't drop below 0
"""
def jump(A):
    n = len(A)
    F = [[float("inf") for _ in range(n)] for _ in range(n)]
    F[0][0] = 0

    for i in range(1, n):
        for j in range(i):
            for k in range(n):
                if k - (i - j) + A[j] >= 0:
                    F[i][min(k - (i - j) + A[j], n - 1)] = min(F[i][min(k - (i - j) + A[j], n - 1)], F[j][k] + 1)
    
    
    res = min(F[n - 1])
    if res == float("inf"):
        return False
    return res



A = [2, 2, 1, 0, 0, 0]
print(jump(A))