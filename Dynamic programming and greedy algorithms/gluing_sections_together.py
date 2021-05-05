#determine whether it is possible to get interval [a, b] by gluing together sections from array A
#Time complexity: O(n*n*m)
def solve(A, a, b):
    n = len(A)
    maxi = max(A, key=lambda x:x[1])[1]
    mini = min(A)[0]
    m = maxi - mini + 1
    F = [[False for _ in range(m)] for _ in range(m)]
    for i in range(n):
        F[A[i][0] - mini][A[i][1] - mini] = True


    for i in range(n):
        for j in range(n):
            if A[j][0] == A[i][1]:
                F[A[i][0] - mini][A[j][1] - mini] = True
                for k in range(A[i][1] - mini + 1):
                    if F[k][A[i][0] - mini]:
                        F[k][A[j][1] - mini] = True
    

    return F[a - mini][b - mini]
    
            

A = [(2, 3), (15, 20), (3, 5), (4, 5), (7, 15), (8, 15), (4, 7), (15, 25)]
print(solve(A, 4, 25))



#each section has a cost, find the minimal cost to build interval [a, b]
def mincost(A, C, a, b):
    n = len(A)
    maxi = max(A, key=lambda x:x[1])[1]
    mini = min(A)[0]
    m = maxi - mini + 1
    F = [[float("inf") for _ in range(m)] for _ in range(m)]
    for i in range(n):
        F[A[i][0] - mini][A[i][1] - mini] = min(C[i], F[A[i][0] - mini][A[i][1] - mini])


    for i in range(n):
        for j in range(n):
            if A[j][0] == A[i][1]:
                F[A[i][0] - mini][A[j][1] - mini] = min(C[i] + C[j], F[A[i][0] - mini][A[j][1] - mini])
                for k in range(A[i][1] - mini + 1):
                    if F[k][A[i][0] - mini] != float("inf"):
                        F[k][A[j][1] - mini] = min(F[k][A[j][1] - mini], F[k][A[i][0] - mini] + F[A[i][0] - mini][A[j][1] - mini])
                
    
    return F[a - mini][b - mini]



A = [(2, 3), (15, 20), (25, 30), (3, 5), (4, 5), (5, 8), (7, 15), (8, 15), (4, 7), (15, 25)]
C = [15, 4, 4, 16, 12, 7, 1, 8, 1, 5]
print(mincost(A, C, 4, 30))



#find the longest possible section glued from at most k sections
def longest(A, k):
    n = len(A)
    maxi = max(A, key=lambda x:x[1])[1]
    mini = min(A)[0]
    m = maxi - mini + 1
    F = [[(False, float("inf")) for _ in range(m)] for _ in range(m)]
    max_length = 0
    for i in range(n):
        F[A[i][0] - mini][A[i][1] - mini] = True, 1
        max_length = max(A[i][1] - A[i][0], max_length)

    
    for i in range(n):
        for j in range(n):
            if A[j][0] == A[i][1]:
                F[A[i][0] - mini][A[j][1] - mini] = True, 2
                if A[j][1] - A[i][0] > max_length and 2 <= k:
                    max_length = A[j][1] - A[i][0]
                for l in range(A[i][1] - mini + 1):
                    if F[l][A[i][0] - mini][0]:
                        F[l][A[j][1] - mini] = True, min(F[l][A[i][0] - mini][1] + 2, F[l][A[j][1] - mini][1])
                        if A[j][1] - mini - l > max_length and F[l][A[j][1] - mini][1] <= k:
                            max_length = A[j][1]  - mini - l
                            
    

    return max_length   



A = [(2, 3), (15, 20), (25, 30), (3, 5), (4, 5), (5, 8), (7, 15), (8, 15), (4, 7), (15, 25)]
print(longest(A, 6))