"""
Find the minimum number of frog jumps to get from index 0 to n - 1, with given
array A with energy potions on each index, to get to j-th index from i-th frog need to consume
j - i energy points, frog starts with 0 energy points, and energy points mustn't drop below 0
"""
def solve(A):
    n = len(A)
    F = [[float("inf") for _ in range(n)] for _ in range(n)]
    F[0][0] = 0
    

    for i in range(1, n):
        for j in range(n):
            for k in range(i):
                if j + A[k] - (i - k) >= 0:
                    F[i][min(j + A[k] - (i - k), n - 1)] = min(F[i][min(j + A[k] - (i - k), n - 1)], F[k][j] + 1)
        
    
    
    return min(F[n - 1])



A = [2, 2, 1, 0, 0, 0]
print(solve(A))