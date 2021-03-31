#merge sort on linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
def mergeSort(head):
    if not head or not head.next:
        return head
    
    mid = head
    fast = head
    while fast.next and fast.next.next:
        mid = mid.next
        fast = fast.next.next

    right_head = mid.next
    mid.next = None

    left = mergeSort(head)
    right = mergeSort(right_head)
    sortedlist = mergelists(left, right)

    return sortedlist


def mergelists(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    res = None

    if head1.value <= head2.value:
        res = head1
        res.next = mergelists(head1.next, head2)
    else:
        res = head2
        res.next = mergelists(head1, head2.next)
    
    return res

def printList(head):
    itr = head
    while itr:
        print(itr.value, end='--->')
        itr = itr.next
    print()

head = Node(2)
head.next = Node(1)
head.next.next = Node(3)
head.next.next.next = Node(0)
printList(head)

x = mergeSort(head)

printList(x)