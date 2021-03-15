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


from random import randint
tab = [randint(1, 10) for _ in range(10)]
head = tab2list(tab)



printList(head)
print()


def qsort(L):

    def quicksort(left, right):
        if not left or left == right:
            return left

        new_left = None
        new_right = None
        pivot, new_left, new_right = partition(left, right, new_left, new_right)

        if new_left != pivot: 
            itr = new_left
            while itr.next != pivot:
                itr = itr.next
            itr.next = None
            new_left = quicksort(new_left, itr)

            itr = getLast(new_left)
            itr.next = pivot

        while pivot.next and pivot.next.value == pivot.value:
            pivot = pivot.next

        pivot.next = quicksort(pivot.next, new_right)
        return new_left


    def partition(left, right, new_left, new_right):
        pivot = right

        temp = Node()
        temp.next = left
        prev = temp
        itr = temp.next
        tail = right

        while itr != pivot:
            if itr.value > pivot.value:
                tail.next, prev.next, itr = itr, prev.next.next, itr.next
                tail.next.next = None
                tail = tail.next
            elif itr.value == pivot.value:
                pivot.next, prev.next, pivot.next.next, itr = itr, prev.next.next, pivot.next, itr.next
                if tail.value == pivot.value:
                    tail = tail.next
            else:
                prev = itr
                itr = itr.next
        
        temp = temp.next
       
        new_left = temp
        new_right = tail
        return pivot, new_left, new_right


    def getLast(head):
        tail = head
        while tail and tail.next:
            tail = tail.next
        return tail
    
    res = quicksort(L, getLast(L))
    return res

printList(qsort(head))