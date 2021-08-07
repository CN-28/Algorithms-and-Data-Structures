"""
Data structure based on heap.
Time complexity of operations:
- insert (log(n)),
- removeMin (log(n)),
- removeMax (log(n)).
"""
def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def parent(i):
    return (i - 1)//2



def heapify(A, B, n, i, opt):
    l = left(i)
    r = right(i)
    m = i
    if opt == "min":
        if l < n and A[l] < A[m]:
            m = l
        if r < n and A[r] < A[m]:
            m = r
        if m != i:
            B[A[i][1]] = B[A[i][1]][0], m
            B[A[m][1]] = B[A[m][1]][0], i
            A[m], A[i] = A[i], A[m]
            heapify(A, B, n, m, opt)
    else:
        if l < n and B[l] > B[m]:
            m = l
        if r < n and B[r] > B[m]:
            m = r
        if m != i:
            A[B[i][1]] = A[B[i][1]][0], m
            A[B[m][1]] = A[B[m][1]][0], i
            B[m], B[i] = B[i], B[m]
            heapify(A, B, n, m, opt)
    


def insert(A, B, x):
    n = len(B)
    A.append((x, n))
    B.append((x, n))
   

    i = n
    while i > 0 and A[parent(i)][0] > A[i][0]:
        B[A[i][1]] = B[A[i][1]][0], parent(i)
        B[A[parent(i)][1]] = B[A[parent(i)][1]][0], i
        A[parent(i)], A[i] = A[i], A[parent(i)]
        i = parent(i)

 
    i = n
    while i > 0 and B[parent(i)][0] < B[i][0]:
        A[B[i][1]] = A[B[i][1]][0], parent(i)
        A[B[parent(i)][1]] = A[B[parent(i)][1]][0], i
        B[parent(i)], B[i] = B[i], B[parent(i)]
        i = parent(i)
    


def removeMin(A, B):
    n = len(A)
    A[n - 1], A[0] = A[0], A[n - 1]
    B[A[0][1]] = B[A[0][1]][0], 0
    val, ind = A.pop()
  
    if ind != n - 1:
        B[ind], B[n - 1] = B[n - 1], B[ind]
        A[B[ind][1]] = A[B[ind][1]][0], ind
    B.pop()


    heapify(A, B, n - 1, 0, "min")
    heapify(A, B, n - 1, ind, "max")



def removeMax(A, B):
    n = len(A)
    B[n - 1], B[0] = B[0], B[n - 1]
    A[B[0][1]] = A[B[0][1]][0], 0
    val, ind = B.pop()


    if ind != n - 1:
        A[ind], A[n - 1] = A[n - 1], A[ind]
        B[A[ind][1]] = B[A[ind][1]][0], ind
    A.pop()
  

    heapify(A, B, n - 1, 0, "max")
    heapify(A, B, n - 1, ind, "min")



#minHeap
A = []
#maxHeap
B = []
insert(A, B, 1)
insert(A, B, 2)
insert(A, B, 3)
print(A)
print(B)
print()
removeMin(A, B)
print(A)
print(B)
print()
removeMax(A, B)
print(A)
print(B)
print()
removeMax(A, B)
print(A)
print(B)
print()