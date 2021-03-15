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
tab = [8,4, 3, 2, 1]
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
       
        new_left = temp
        new_right = tail
        return pivot, new_left, new_right


    def getLast(head):
        tail = head
        while tail and tail.next:
            tail = tail.next
        return tail
    
    L = quicksort(L, getLast(L))
    return L

printList(qsort(head))