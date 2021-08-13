#matrix chain multiplication, time complexity: O(n**3)
def matrixChainMultiplication(A):
    n = len(A)
    F = [[0 if i == j else float("inf") for j in range(n)] for i in range(n)]


    for k in range(1, n):
        for i in range(n - k):
            for j in range(k):
                F[i][i + k] = min(F[i][i + j] + F[i + j + 1][i + k] + A[i][0] * A[i + j][1] * A[i + k][1], F[i][i + k])
                
    return F[0][n - 1]



A = [(40, 20), (20, 30), (30, 10), (10, 30)]
print(matrixChainMultiplication(A))