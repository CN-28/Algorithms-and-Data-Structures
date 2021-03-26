#sort linked list with values from [0, 10) with uniform distribution of numbers

class Node:
    def __init__(self):
        self.value = None
        self.next = None

from random import uniform

linkedlist = Node()
itr = linkedlist
for i in range(15):
    itr.next = Node()
    itr.next.value = round(uniform(10 - i/2 - 2, 10 - i/2 - 0.01), 2)
    itr = itr.next


def printList(head):
    itr = head
    while itr:
        print(itr.value, end="---> ")
        itr = itr.next
    print()


def getLength(head):
    length = 0
    itr = head.next
    while itr:
        length += 1
        itr = itr.next
    
    return length


def insertionSort(T):
    if not T or not T.next:
        return

    head = Node()
    head.next = T
    itr = head.next
    while itr.next:
        itr1 = head

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



def bucket_sort(head):
    n = getLength(head)
    buckets = [None for _ in range(n)]
    bucket_range = 10/n
 

    itr = head.next
    while itr:
        index = int(itr.value//bucket_range)
        temp = itr
        itr = itr.next
        temp.next = None
        if buckets[index] == None:
            buckets[index] = temp
        else:
            temp.next = buckets[index]
            buckets[index] = temp
    itr = head
    for i in range(len(buckets)):
        if buckets[i] and buckets[i].next != None:
            insertionSort(buckets[i])
        if buckets[i]:
            itr.next = buckets[i]
            while itr.next:
                itr = itr.next

    
bucket_sort(linkedlist)
printList(linkedlist)