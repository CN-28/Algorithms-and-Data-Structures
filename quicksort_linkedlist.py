class Node:
    def __init__(self):
        self.next = None
        self.value = None



def tab2list( A ):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next


def printList(head):
    itr = head
    while itr:
        print(itr.value, end='--->')
        itr = itr.next
    print()


from random import randint
tab = [8, 4, 3, 2, 1, 2]
head = tab2list(tab)



printList(head)
print()


def qsort(L):
    def quicksort(left, right):
        if not left or left == right:
            return left

        pivot, left, right = partition(left, right)

        if left != pivot: 
            itr = left
            while itr.next != pivot:
                itr = itr.next
            itr.next = None
            left = quicksort(left, itr)

            itr = getLast(left)
            itr.next = pivot

        while pivot.next and pivot.next.value == pivot.value:
            pivot = pivot.next

        pivot.next = quicksort(pivot.next, right)
        return left


    def partition(left, right):
        pivot = right

        temp = Node()
        temp.next = left
        itr = temp
        tail = right
        while itr.next != pivot:

            if itr.next.value > pivot.value:
                tail.next, itr.next = itr.next, itr.next.next
                tail.next.next = None
                tail = tail.next
            elif itr.next.value == pivot.value:
                pivot.next, itr.next, pivot.next.next = itr.next, itr.next.next, pivot.next
                if tail.next and tail.value == pivot.value:
                    tail = tail.next
            else:
                itr = itr.next
            
        temp = temp.next
       
        left = temp
        right = tail
        return pivot, left, right


    def getLast(head):
        tail = head
        while tail and tail.next:
            tail = tail.next
        return tail
    
    L = quicksort(L, getLast(L))
    return L



printList(qsort(head))