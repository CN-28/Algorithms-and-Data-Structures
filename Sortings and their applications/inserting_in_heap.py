def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def parent(i):
    return (i - 1)//2


def heapify(A, n, i):
    l = left(i)
    r = right(i)
    m = i
    if l < n and A[l] > A[m]:
        m = l
    if r < n and A[r] > A[m]:
        m = r
    
    if m != i:
        A[i], A[m] = A[m], A[i]
        heapify(A, n, m)


def insert(A, x):
    A.append(x)
    i = len(A) - 1
    while i > 0 and A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)

tab = [5, 4, 2]

insert(tab, 10)
print(tab)