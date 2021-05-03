"""
A[i] - profit for cutting an i-th tree, you mustn't cut two trees in a row,
Find the maximum profit for cutting trees from array A
"""
def solve(A):
    n = len(A)
    F = [0 for i in range(n)]
    S = [-1 for i in range(n)]

    F[0] = A[0]
    if A[0] > A[1]:
        F[1] = A[0]
        S[1] = 0
    else:
        F[1] = A[1]

    for i in range(2, n):
        if F[i - 2] + A[i] > F[i - 1]:
            S[i] = i - 2
            F[i] = F[i - 2] + A[i]
        else:
            F[i] = F[i - 1]
    

    res = []
    index = n - 1
    while index != 0 and index != 1:
        if S[index] == -1:
            index -= 1
        else:
            res.append(index)
            index = S[index]
    

    if index == 1 and S[index] == 0:
        res.append(0)
    else:
        res.append(1)
    for i in range(len(res) - 1, -1, -1):
        print(res[i], end="--> ")
    print()



    return F[n - 1]



A = [3, 5, 9, 1000, 7, 2, 6, 1]
print(solve(A))