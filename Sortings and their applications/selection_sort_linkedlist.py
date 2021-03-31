#implementation with sentinel node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node("!")
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(3)

def printList(head):
    itr = head
    while itr:
        print(itr.value, end='--->')
        itr = itr.next
    print()

printList(head)

def selectionSort(T):
    itr = T
    while itr.next:
        itr1 = itr.next
        mini = itr
        while itr1.next:
            if itr1.next.value < itr.next.value:
                mini = itr1

            itr1 = itr1.next
        
        if itr.next == mini:
            itr.next, mini.next.next, mini.next = mini.next, itr.next, mini.next.next
        elif itr != mini:
            mini.next.next, itr.next.next = itr.next.next, mini.next.next
            itr.next, mini.next = mini.next, itr.next
        itr = itr.next

selectionSort(head)
printList(head)
