#data structure based on heaps, time complexity of operations: insert (log(n)), removeMedian (log(n))
def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def parent(i):
    return (i - 1)//2



def heapify(A, n, i, opt):
    l = left(i)
    r = right(i)
    m = i
    if opt == "min":
        if l < n and A[l] < A[m]:
            m = l
        if r < n and A[r] < A[m]:
            m = r
    else:
        if l < n and A[l] > A[m]:
            m = l
        if r < n and A[r] > A[m]:
            m = r

    if m != i:
        A[m], A[i] = A[i], A[m]
        heapify(A, n, m, opt)



def removeMax(MaxHeap):
    n = len(MaxHeap)
    MaxHeap[0], MaxHeap[n - 1] = MaxHeap[n - 1], MaxHeap[0]
    maxi = MaxHeap.pop()
    heapify(MaxHeap, n - 1, 0, "max")
    return maxi



def removeMin(MinHeap):
    n = len(MinHeap)
    MinHeap[0], MinHeap[n - 1] = MinHeap[n - 1], MinHeap[0]
    mini = MinHeap.pop()
    heapify(MinHeap, n - 1, 0, "min")
    return mini



def insert(MinHeap, MaxHeap, x):
    MaxHeap.append(x)
    i = len(MaxHeap) - 1
    while i > 0 and MaxHeap[parent(i)] < MaxHeap[i]:
        MaxHeap[i], MaxHeap[parent(i)] = MaxHeap[parent(i)], MaxHeap[i]
        i = parent(i)

    if len(MaxHeap) > len(MinHeap):
        maxi = removeMax(MaxHeap)
        MinHeap.append(maxi)
        i = len(MinHeap) - 1
        while i > 0 and MinHeap[parent(i)] > MinHeap[i]:
            MinHeap[i], MinHeap[parent(i)] = MinHeap[parent(i)], MinHeap[i]
            i = parent(i)
    if len(MinHeap) > len(MaxHeap):
        mini = removeMin(MinHeap)
        MaxHeap.append(mini)
        i = len(MaxHeap) - 1
        while i > 0 and MaxHeap[parent(i)] < MaxHeap[i]:
            MaxHeap[i], MaxHeap[parent(i)] = MaxHeap[parent(i)], MaxHeap[i]
            i = parent(i)



def removeMedian(MinHeap, MaxHeap):
    n = len(MaxHeap)
    m = len(MinHeap)
    if n > m:
        MaxHeap[0], MaxHeap[n - 1] = MaxHeap[n - 1], MaxHeap[0]
        heapify(MaxHeap, n - 1, 0, "max")
        return MaxHeap.pop()
    else:
        MinHeap[0], MinHeap[m - 1] = MinHeap[m - 1], MinHeap[0]
        MaxHeap[0], MaxHeap[n - 1] = MaxHeap[n - 1], MaxHeap[0]
        heapify(MinHeap, m - 1, 0, "min")
        heapify(MaxHeap, n - 1, 0, "max")
        return (MaxHeap.pop() + MinHeap.pop())/2



MaxHeap = []
MinHeap = []
insert(MinHeap, MaxHeap, 2)
insert(MinHeap, MaxHeap, 5)
insert(MinHeap, MaxHeap, 1)
insert(MinHeap, MaxHeap, 4)
insert(MinHeap, MaxHeap, 3)
insert(MinHeap, MaxHeap, 6)
print(removeMedian(MinHeap, MaxHeap))
print(MaxHeap)
print(MinHeap)