#split linked list into two linked lists, one with even numbers and the
#other one with odd numbers


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def printList(head):
    itr = head
    while itr:
        print(itr.value, end='--->')
        itr = itr.next
    print()


head = Node(4)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(5)
printList(head)

def split(head):
    even_numbers = Node()
    itr_even = even_numbers

    temp = Node()
    temp.next = head

    itr = temp
    while itr.next:
        if itr.next.value % 2 == 0:
            itr_even.next = itr.next
            itr.next = itr.next.next
            itr_even.next.next = None
            itr_even = itr_even.next
        else:
            itr = itr.next
        
        
    return even_numbers.next, temp.next




even, odd = split(head)
printList(even)
printList(odd)