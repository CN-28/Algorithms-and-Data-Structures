"""
A - two dimensional array(nxn) filled with rational numbers that indicate the cost of standing on the
(i, j) field, starting from (0, 0) find the cheapest way, which leads to the A[n - 1][n - 1]
"""
def mincost(A):
    n = len(A)
    F = [[0 for _ in range(n)] for _ in range(n)]
    S = [[-1 for _ in range(n)] for _ in range(n)]


    F[0][0] = A[0][0]
    for i in range(1, n):
        F[i][0] = F[i - 1][0] + A[i][0]
        F[0][i] = F[0][i - 1] + A[0][i]
    

    for i in range(1, n):
        for j in range(1, n):
            if F[i - 1][j] < F[i][j - 1]:
                S[i][j] = (i - 1, j)
                F[i][j] = F[i - 1][j] + A[i][j]
            else:
                S[i][j] = (i, j - 1)
                F[i][j] = F[i][j - 1] + A[i][j]
   

    R = []
    index = n - 1, n - 1
    while index[0] != 0 and index[1] != 0:
        R.append(index)
        index = S[index[0]][index[1]]
    R.append(index)
    R.append((0, 0))
    

    for i in range(len(R) - 1, -1 , -1):
        print(R[i], end=" --> ")
    print()
    return F[n - 1][n - 1]



A = [
    [2, 8, 3, 1],
    [1, 4, 5, 2],
    [5, 8, 7, 2],
    [1, 9, 2, 3]
]
for x in A:
    print(x)
print(mincost(A))