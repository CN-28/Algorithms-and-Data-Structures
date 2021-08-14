"""
A - two dimensional array(nxn) filled with rational numbers that indicate the cost of standing on the
(i, j) field, starting from (0, 0) find the cheapest way, which leads to the A[n - 1][n - 1]
"""
#Time complexity: O(n**2), space complexity: O(n**2), if only the cost of the cheapest path is needed space complexity can be reduced to O(n)
def minpath(A):
    n = len(A)
    F = [[float("inf") for _ in range(n)] for _ in range(2)]
    S = [[-1 for _ in range(n)] for _ in range(n)]
    F[0][0] = A[0][0]


    for i in range(n):
        for j in range(n):
            if j + 1 < n and F[0][j] + A[i][j + 1] < F[0][j + 1]:
                F[0][j + 1] = F[0][j] + A[i][j + 1]
                S[i][j + 1] = (i, j)
            if i + 1 < n and F[0][j] + A[i + 1][j] < F[1][j]:
                F[1][j] = F[0][j] + A[i + 1][j]
                S[i + 1][j] = (i, j)
        if i + 1 < n:
            for i in range(n):
                F[0][i], F[1][i] = F[1][i], float("inf")
    
    res = []
    index = n - 1, n - 1
    while index != -1:
        res.append((index[0], index[1]))
        index = S[index[0]][index[1]]
    
    for i in range(len(res) - 1, - 1, -1):
        print(res[i], end="-->")
    print()


    return F[0][n - 1]



A = [
    [1, 1, 1, 1, 6],
    [1, 1, 3, 4, 5],
    [1, 2, 3, 4, 1],
    [5, 2, 1, 1, 1],
    [8, 1, 1, 1, 1]
]
print(minpath(A))