def heapify(A, n, i):
    l = 2*i + 1
    r = 2*i + 2
    largest = i
    if l < n and A[l] > A[largest]:
        largest = l
    if r < n and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, n, largest)

def buildheap(A):
    n = len(A)
    for i in range((n-2)//2, -1, -1):
        heapify(A, n, i)

def heapsort(A):
    n = len(A)
    buildheap(A)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)


tab = [4, 1, 3, 4, 9, 2, 7, 0]
heapsort(tab)
print(tab)