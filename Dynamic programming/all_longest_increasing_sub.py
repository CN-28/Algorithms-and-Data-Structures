def lis(A):
    n = len(A)
    F = [1] * n
    P = [[] for _ in range(n)]
    omi = 0
    omax = 0
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i].append(j)
        if F[i] > omax:
            omax = F[i]
            omi = i
        
    print(P)
    print(F)
    print(omi, omax)



    return (max(F), P)


def printsolution(A, P, i):
    if P[i] != -1:
        printsolution(A, P, P[i])
    print(A[i], end=" ")


Arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(Arr)
x = lis(Arr)
#printsolution(Arr, x[1], len(x[1]) - 1)