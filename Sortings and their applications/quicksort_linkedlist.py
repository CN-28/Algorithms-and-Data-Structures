class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
    


def printList(head):
    itr = head
    while itr:
        print(itr.val, end="---> ")
        itr = itr.next
    print()



def quicksort(head):
    if not head or not head.next:
        return head, head
    
    left, left_end, mid = partition(head)
    right = mid.next
    mid.next = None
    left, left_end = quicksort(left)
    right, right_end = quicksort(right)
    if left:
        left_end.next = mid
        mid.next = right
    else:
        left = mid
        left.next = right
        left_end = left.next
    
    
    return left, left_end



def partition(head):
    pivot = head
    temp = Node()
    temp.next = head.next
    pivot.next = None
    itr_pivot = pivot
    itr = temp
    while itr and itr.next:
        boolTemp = False
        if itr.next.val > pivot.val:
            itr_pivot.next = itr.next
            itr.next = itr.next.next
            itr_pivot = itr_pivot.next
            itr_pivot.next = None
            
            boolTemp = True
        if not boolTemp:
            itr = itr.next

    return temp.next, itr, pivot



head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(5)
head.next.next.next.next = Node(4)

printList(head)
head, x = quicksort(head)
printList(head)