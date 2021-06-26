#EXAM 2020, task 2, third exam date
def tower(A):
    n = len(A)
    F = [1 for _ in range(n)]


    for i in range(1, n):
        for j in range(i):
            if A[i][0] >= A[j][0] and A[i][1] <= A[j][1]:
                if F[j] + 1 > F[i]:
                    F[i] = F[j] + 1
                
                
    return max(F)