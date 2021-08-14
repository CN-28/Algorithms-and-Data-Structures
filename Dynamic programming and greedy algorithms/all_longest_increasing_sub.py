def printAllLIS(A):
    n = len(A)
    F = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if A[i] > A[j] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
    
    
    return getSolution(A, F, max(F), n, n)



def getSolution(A, F, length, ind, n, str="", cnt=0):
    if length == 0:
        print(str)
        return cnt + 1

    for i in range(ind - 1, -1, -1):
        if (ind == n or A[i] < A[ind]) and F[i] == length:
            cnt = getSolution(A, F, length - 1, i, n, f"{A[i]} {str}", cnt)
    
    return cnt
    


A = [2, 1, 4, 3, 5]
print(printAllLIS(A))