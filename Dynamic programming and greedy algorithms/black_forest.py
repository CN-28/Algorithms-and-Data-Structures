"""
A[i] - profit for cutting an i-th tree, you mustn't cut two trees in a row,
Find the maximum profit for cutting trees from array A
"""
def maxCutProfit(A):
    n = len(A)
    F = [0 if i != 0 else A[i] for i in range(n)]
    F[1] = max(A[0], A[1])

    
    for i in range(2, n):
        F[i] = max(F[i - 1], F[i - 2] + A[i])
    

    i = n - 1
    res = []
    while i >= 2:
        if F[i] == F[i - 1]:
            i -= 1
        elif F[i] != F[i - 2]:
            res.append(A[i])
            i -= 2
    
    
    if len(res) > 0 and res[len(res) - 1] == 2:
        res.append(A[0])
    else:
        if A[1] > A[0]:
            res.append(A[1])
        else:
            res.append(A[0])    
    print(res[::-1])
    

    return F[n - 1]



forest = [5, 12, 6, 3, 2, 52, 11, 5, 34, 54]
print(maxCutProfit(forest))