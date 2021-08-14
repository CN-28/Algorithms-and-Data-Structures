def coins(A, T):
    n = len(A)
    F = [float("inf") if i != 0 else 0 for i in range(T + 1)]
    
    for i in range(n):
        for j in range(A[i], T + 1):
            F[j] = min(F[j], F[j  - A[i]] + 1)
    
    if F[T] == float("inf"):
        return False
    return F[T]
    
    

A = [1, 2, 3]
print(coins(A, 50))