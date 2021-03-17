class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def merge(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    res = None

    if head1.value <= head2.value:
        res = head1
        res.next = merge(head1.next, head2)
    else:
        res = head2
        res.next = merge(head1, head2.next)
    
    return res

def printList(head):
    itr = head
    while itr:
        print(itr.value, end='--->')
        itr = itr.next
    print()

head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(5)

head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)

head = merge(head1, head2)
printList(head)