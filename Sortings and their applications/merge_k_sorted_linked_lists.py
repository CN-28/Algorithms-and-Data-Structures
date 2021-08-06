class Node:
    def __init__(self, val):
        self.val = val
        self.next = None



def merge(head1, head2):
    res = None
    if head1 and (not head2 or head1.val < head2.val):
        res = head1
        res.next = merge(head1.next, head2)
    elif head2:
        res = head2
        res.next = merge(head1, head2.next)
    
    return res



def mergeKlists(A):
    i = 0
    j = len(A) - 1
    while i != 0 or j != 0:
        temp = j
        while i < temp:
            A[i] = merge(A[i], A[temp])
            i += 1
            temp -= 1
        i = 0
        j //= 2
    


def printList(head):
    itr = head
    while itr:
        print(itr.val, end="--->")
        itr = itr.next



L1 = Node(1)
L1.next = Node(5)
L1.next.next = Node(9)

L2 = Node(2)
L2.next = Node(6)
L2.next.next = Node(10)

L3 = Node(3)
L3.next = Node(7)
L3.next.next = Node(11)

L4 = Node(4)
L4.next = Node(8)
L4.next.next = Node(12)


A = [L1, L2, L3, L4]
mergeKlists(A)
printList(A[0])