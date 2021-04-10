def lis(A):
    n = len(A)
    P = [0 for _ in range(n)]
    M = [0 for _ in range(n + 1)]
    l = 0
    cnt = 0
    for i in range(n):
        lo = 1
        hi = l
        
        while lo <= hi:
            mid = (lo + hi)//2
            if A[M[mid]] < A[i]:
                lo = mid + 1
            else:
                hi = mid - 1
        
        newL = lo
        P[i] = M[newL - 1]
        M[newL] = i

        if newL > l:
            l = newL
    
    print(cnt)
    
    print("M:", M)
    print("P:", P)
    print(l)
    
    S = [0 for _ in range(l)]
    
    k = M[l]
    print(k)
    for i in range(l - 1, -1, -1):
        S[i] = A[k]
        k = P[k]
        print(k)
    
    return S

Arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print("A: ", Arr)
print(lis(Arr))