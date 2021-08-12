#T[N] filled with rational values from k intervals located in array P, for each interval there is probability of choosing number from this interval
#number from the interval is chosen from a uniform distribution, sort array T, interval starting or ending is a natural number from 1 to N

from math import floor

def SortTab(T, P):
    n = len(T)
    buckets = [[] for _ in range(n)]
    for i in range(n):
        buckets[floor(T[i] - 1)].append(T[i])
    

    for i in range(n):
        if len(buckets[i]) != 0:
            bucketSort(buckets[i], i, i + 1)
    

    k = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            T[k] = buckets[i][j]
            k += 1



def bucketSort(A, i, j):
    n = len(A)
    buckets = [[] for _ in range(n)]
    bucket_range = 1 / n
    for k in range(n):
        buckets[int((A[k] - (i + 1)) // bucket_range)].append(A[k])
    
    for k in range(n):
        buckets[k].sort()
    
    m = 0
    for k in range(n):
        for l in range(len(buckets[k])):
            A[m] = buckets[k][l]
            m += 1



P = [(1,5, 0.75) , (4,8, 0.25)]
T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]
SortTab(T, P)
print(T)