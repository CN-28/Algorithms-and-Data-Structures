def heapify(A, i):
    parent = (i - 1)//2
    if parent >= 0 and A[i] > A[parent]:
        A[i], A[parent] = A[parent], A[i]
        heapify(A, parent)



def insert(A, elem):
    A.append(elem)
    heapify(A, len(A) - 1)

tab = [5, 4, 2]

insert(tab, 10)
print(tab)