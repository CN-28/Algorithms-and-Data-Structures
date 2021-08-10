#finding k-th (counting from 0 - first element) largest element in array in linear time,
#assuming all pairs of numbers are different
def linearselect(A, l, r, k):
    while True:
        if l == r:
            return l

        pivotInd = pivot(A, l, r)
        pivotInd = partition(A, l, r, pivotInd)
        if k == pivotInd:
            return k
        elif k < pivotInd:
            r = pivotInd - 1
        else:
            l = pivotInd + 1



def partition(A, l, r, pivotInd):
    pivot = A[pivotInd]
    i = l - 1
    j = r + 1
    while True:
        i += 1
        while A[i] < pivot:
            i += 1
        
        j -= 1
        while A[j] > pivot:
            j -= 1
        
        if i >= j:
            return j
        
        A[i], A[j] = A[j], A[i]



def pivot(A, l, r):
    if r - l < 5:
        return partition5(A, l, r)
    
    for i in range(l, r + 1, 5):
        right5 = min(i + 4, r)
        median5 = partition5(A, i, right5)
        A[median5], A[l + (i - l)//5] = A[l + (i - l)//5], A[median5]
    
    mid = (r - l) // 10 + l + 1
    return linearselect(A, l, l + (r - l)//5, mid)



def partition5(A, l, r):
    i = l + 1
    while i <= r:
        for j in range(i - 1, l - 1, -1):
            if A[j] > A[i]:
                A[i], A[j] = A[j], A[i]
                break
        i += 1
    
    return (l + r)//2



A = [90, 45, 25, 432, 123, 43, 15]
print(A[linearselect(A, 0, len(A) - 1, 6)])