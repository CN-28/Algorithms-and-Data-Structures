"""
A[i] - profit for cutting an i-th tree, you mustn't cut two trees in a row,
Find the maximum profit for cutting trees from array A
"""
def solve(A):
    n = len(A)
    S = [-1 for i in range(n)]

    x2 = A[0]
    if A[0] > A[1]:
        x1 = A[0]
        S[1] = 0
    else:
        x1 = A[1]

    for i in range(2, n):
        if x2 + A[i] > x1:
            S[i] = i - 2
            x1, x2 = x2 + A[i], x1
        else:
            x2 = x1
    

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



    return x1



A = [3, 5, 9, 1000, 7, 2, 6, 1, 15]
print(solve(A))