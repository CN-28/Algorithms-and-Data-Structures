def lis(A):
    n = len(A)
    P = [0 for _ in range(n)]
    M = [0 for _ in range(n + 1)]
    length = 0

    for i in range(n):
        lo = 1
        hi = length
        while lo <= hi:
            mid = (lo + hi)//2
            if A[M[mid]] < A[i]:
                lo = mid + 1
            else:
                hi = mid - 1
        

        P[i] = M[lo - 1]
        M[lo] = i
        length = max(length, lo)
    

    S = [0 for _ in range(length)]
    k = M[length]
    for i in range(length - 1, -1, -1):
        S[i] = A[k]
        k = P[k]
    
    
    return S



Arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print("A: ", Arr)
print(lis(Arr))