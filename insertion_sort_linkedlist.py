class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node("!")
head.next = Node(6)
head.next.next = Node(5)
head.next.next.next = Node(3)
head.next.next.next.next = Node(1)
head.next.next.next.next.next = Node(8)


def printList(head):
    itr = head
    while itr:
        print(itr.value, end='--->')
        itr = itr.next
    print()

printList(head)


def insertionSort(T):
    if not T or not T.next:
        return

    itr = T.next
    while itr.next:
        itr1 = T

        temp = False
        while itr1.next != itr.next:
            
            if itr.next.value < itr1.next.value and itr1.next == itr: 
                itr.next.next, itr.next, itr1.next = itr, itr.next.next, itr1.next.next
                temp = True
                break
            elif itr.next.value < itr1.next.value:
                itr1.next, itr.next.next, itr.next = itr.next, itr1.next, itr.next.next
                temp = True
                break
            
            itr1 = itr1.next
        
        if not temp:
            itr = itr.next
        
        
insertionSort(head)
printList(head)