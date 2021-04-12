def printAllLIS(A):
    n = len(A)

    F = [1] * n
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
        
            
        
    res = []
    max_length = max(F)
    for i in range(n):
        if max_length == F[i]:
            res.append((max_length, i, A[i], f"{A[i]} "))


    cnt = 0
    while len(res) > 0:
        rem = res.pop()
        if rem[0] == 1:
            print(rem[3])
            cnt += 1
            

        for i in range(rem[1] - 1, -1, -1):
            if F[i] == rem[0] - 1 and A[i] <= rem[2]:
                res.append((F[i], i, A[i], f"{A[i]} {rem[3]}"))
        

    return cnt



A = [2,1,4,3]
print(printAllLIS(A))