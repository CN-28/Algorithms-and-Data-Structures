def quicksort(A, p, r):
    while p < r:
        q = partition(A, p, r)

        if q - p < r - q:
            quicksort(A, p, q - 1)
            p = q + 1
        else:
            quicksort(A, q + 1, r)
            r = q - 1
    
def partition(A, p, r):
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

tab = [4, 1, 5, 3, 4, 3]
quicksort(tab, 0 , len(tab) - 1)
print(tab)