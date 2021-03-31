class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def printList(head):
    itr = head
    while itr:
        print(itr.value, end='--->')
        itr = itr.next
    print()


def merge2lists(head1, head2):
    res = None

    if not head1:
        return head2
    elif not head2:
        return head1

    if head1.value <= head2.value:
        res = head1
        res.next = merge2lists(head1.next, head2)
    else:
        res = head2
        res.next = merge2lists(head1, head2.next)
    
    return res

def mergeklists(A):
    last = len(A) - 1
    while last != 0:
        i = 0
        j = last
    
        while i < j:
            A[i] = merge2lists(A[i], A[j])
            i += 1
            j -= 1

            if i >= j:
                last = j

    return A[0]

tab = []
tab.append(Node(2))
tab[0].next = Node(4)
tab.append(Node(1))
tab.append(Node(4))
tab.append(Node(0))
tab.append(Node(9))
x = mergeklists(tab)
printList(x)