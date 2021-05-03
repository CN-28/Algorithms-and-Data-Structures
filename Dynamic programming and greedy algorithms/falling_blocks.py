"""
A - array of blocks, every block is an interval, find the minimum number of blocks which need
to be removed, so that each successive block may be placed entirely on the previous block
"""
def solve(A):
    n = len(A)
    F = [1 for _ in range(n)]


    for i in range(1, n):
        for j in range(i):
            if A[i][0] >= A[j][0] and A[i][1] <= A[j][1]:
                F[i] = max(F[i], F[j] + 1)
    
    
    return n - max(F)
            


A = [(5, 6), (2, 5), (2, 4), (3, 4), (15, 20), (3, 4)]
print(solve(A))