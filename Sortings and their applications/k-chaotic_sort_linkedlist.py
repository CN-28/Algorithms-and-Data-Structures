"""
List is k-chaotic when all of its elements, after sorting, are placed
at most k indexes from current index, sort the list taking the advantage of knowing k.
Time complexity: O(n*log(k))
"""
class Node:
    def __init__(self, val=None):
        self.val = val     
        self.next = None 



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
    if l < n and A[l].val < A[m].val:
        m = l
    if r < n and A[r].val < A[m].val:
        m = r
    
    if m != i:
        A[m], A[i] = A[i], A[m]
        heapify(A, n, m)



def insert(A, x):
    A.append(x)
    i = len(A) - 1
    while i > 0 and A[parent(i)].val > A[i].val:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)



def extractMin(A):
    n = len(A)
    A[0], A[n - 1] = A[n - 1], A[0]
    heapify(A, n - 1, 0)
    return A.pop()



def SortH(p,k):
    heap = []
    itr = p
    cnt = 0
    res = Node()
    itr_res = res
    while itr:
        while cnt != k + 1 and itr:
            temp = itr
            itr = itr.next
            temp.next = None
            insert(heap, temp)
            cnt += 1

        cnt -= 1
        itr_res.next = extractMin(heap)
        itr_res = itr_res.next
    

    while len(heap) != 0:
        itr_res.next = extractMin(heap)
        itr_res = itr_res.next


    return res.next