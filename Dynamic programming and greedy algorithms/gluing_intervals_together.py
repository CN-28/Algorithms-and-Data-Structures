#determine whether it is possible to get interval [a, b] by gluing together intervals from array A
#time complexity: O(n**3)
def canGlue(A, a, b):
    n = len(A)
    A = sorted(A)
    F = [[False for _ in range(n)] for _ in range(n)]


    for i in range(n):
        for j in range(n):
            if A[i][1] == A[j][0] or i == j:
                F[i][j] = True
    
        
    for i in range(n - 1):
        for j in range(i + 1, n):
            for k in range(n):
                if A[k][1] == A[j][0] and F[i][k]:
                    F[i][j] = True
    

    start = []
    end = []
    for i in range(n):
        if A[i][0] == a:
            start.append(i)
        if A[i][1] == b:
            end.append(i)
    
   
    for i in range(len(start)):
        for j in range(len(end)):
            if F[start[i]][end[j]]:
                return True
    return False



#each section has a cost, find the minimal cost to build interval [a, b]
#time complexity: O(n**3)
def minCostGlue(A, C, a, b):
    n = len(A)
    A = [(A[i][0], A[i][1], C[i]) for i in range(n)]
    A = sorted(A)
    F = [[float("inf") for _ in range(n)] for _ in range(n)]


    for i in range(n):
        for j in range(n):
            if A[i][1] == A[j][0]:
                F[i][j] = A[i][2] + A[j][2]
            if i == j:
                F[i][j] = A[i][2]
    
        
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if A[k][1] == A[j][0]:
                    F[i][j] = min(F[i][j], F[i][k] + A[j][2])
    

    start = []
    end = []
    for i in range(n):
        if A[i][0] == a:
            start.append(i)
        if A[i][1] == b:
            end.append(i)
    

    mini = float("inf")
    for i in start:
        for j in end:
            mini = min(F[i][j], mini)


    return mini



#find the length of the longest possible interval glued from at most k intervals
#time complexity: O(n**3)
def longest(A, k):
    n = len(A)
    A = sorted(A)

    F = [[(0, 1) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if A[i][1] == A[j][0]:
                F[i][j] = max(F[i][j][0], A[j][1] - A[i][0]), 2
            if i == j:
                F[i][j] = A[j][1] - A[i][0], 1


    for i in range(n):
        for j in range(n):
            for l in range(n):
                if A[l][1] == A[j][0] and F[i][l][1] + 1 <= k and F[i][l][0] != 0:
                    F[i][j] = max(F[i][j][0], F[i][l][0] + A[j][1] - A[j][0]), F[i][l][1] + 1
            
    maxi = 0
    for i in range(n):
        for j in range(n):
            if F[i][j][1] <= k:
                maxi = max(maxi, F[i][j][0])
    
    return maxi



A = [(2, 3), (15, 20), (25, 30), (3, 5), (4, 5), (5, 8), (7, 15), (8, 15), (4, 7), (15, 25)]
C = [15, 4, 4, 16, 12, 7, 1, 8, 1, 5]
print(canGlue(A, 4, 30))
print(minCostGlue(A, C, 4, 30))
print(longest(A, 4))