#merge sort on linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, elem):
        if not self.head:
            self.head = Node(elem)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(elem)
    
    def printList(self):
        itr = self.head
        while itr:
            print(itr.value, end="---> ")
            itr = itr.next
        print()

    def mergeSort(self, first):
        if not first or not first.next:
            return first
        
        #getting the middle element of the list
        mid = first
        last = first
        
        while last.next and last.next.next:
            mid = mid.next
            last = last.next.next
        #end of getting the middle element of the list

        righthead = mid.next
        mid.next = None

        L = self.mergeSort(first)

        R = self.mergeSort(righthead)

        sortedll_head = self.sortmerge(L, R)
        return sortedll_head
    
    #rekur
    def sort_and_merge(self, left, right):
        if not left:
            return right
        if not right:
            return left
        
        res = None
        if left.value <= right.value:
            res = left
            res.next = self.sort_and_merge(left.next, right)
        else:
            res = right
            res.next = self.sort_and_merge(left, right.next)
        
        return res
    
    #iter
    def sortmerge(self, left, right):
        res = None
        if left and left.value <= right.value:
            res = left
            left = left.next
        elif right:
            res = right
            right = right.next

        itr = res
        while left or right:
            if left and right and left.value <= right.value:
                itr.next = left
                left = left.next
            elif right:
                itr.next = right
                right = right.next
            elif left:
                itr.next = left
                left = left.next

            itr = itr.next
        return res




llist = LinkedList()
llist.append(4)
llist.append(1)
llist.append(3)
llist.append(5)

llist.head = llist.mergeSort(llist.head)
print("Merge sort on linked list", end=' ')
llist.printList()