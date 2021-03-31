class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

def printlist(head):
    itr = head
    while itr:
        print(itr.value, end='--->')
        itr = itr.next
    print()

def reverse(head):
    itr = head
    prev = None
    next = head.next
    while itr:
        itr.next = prev
        prev = itr
        itr = next
        if next:
            next = next.next
    return prev

head = reverse(head)
printlist(head)