def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q)
        quicksort(A, q + 1, r)

def partition(A, p, r):
    pivot = A[p]
    left = p - 1
    right = r + 1

    while True:
        left += 1
        while A[left] < pivot:
            left += 1

        right -= 1
        while A[right] > pivot:
            right -= 1
        
        if left >= right:
            return right
        
        A[left], A[right] = A[right], A[left]

Arr = [4, 1, 2, 5, 2, 3]
quicksort(Arr, 0, len(Arr) - 1)
print(Arr)
