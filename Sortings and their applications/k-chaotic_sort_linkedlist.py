"""
list is k-chaotic when all of its elements, after sorting, are placed
at most k indexes from current index, sort the list taking the advantage of knowing k

n - the length of the list
For k = 1 - insertion sort, performance: O(n)
For k <= logn - insertion sort, performance: O(nlogn)
For k > logn - merge sort, perfmorance: O(nlogn)
"""

class Node:
  def __init__(self):
    self.val = None     
    self.next = None 


from math import log2
def SortH(p,k):
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

        if head1.val <= head2.val:
            res = head1
            res.next = mergelists(head1.next, head2)
        else:
            res = head2
            res.next = mergelists(head1, head2.next)
        
        return res
  

    def insertionSort(T, k):
        if not T or not T.next:
            return

        prev = Node()
        prev.next = T
        itr = T
        itr1 = prev
        cnt = 0
        while itr.next:
            temp = False
            if itr.next.val < itr.val:
                temp_itr = itr1
                while temp_itr.next != itr.next:
                    if itr.next.val < temp_itr.next.val and temp_itr.next == itr: 
                        itr.next.next, itr.next, temp_itr.next = itr, itr.next.next, temp_itr.next.next
                        temp = True
                        break
                    elif itr.next.val < temp_itr.next.val:
                        temp_itr.next, itr.next.next, itr.next = itr.next, temp_itr.next, itr.next.next
                        temp = True
                        break
                    
                    temp_itr = temp_itr.next
            
            if not temp:
                itr = itr.next
            cnt += 1
            if cnt >= k:
                itr1 = itr1.next
        
        return prev.next


    def getLength(head):
        length = 0
        itr = head
        while itr:
            itr = itr.next
            length += 1
        return length
  
    if k <= log2(getLength(p)):
        return insertionSort(p, k)
    else:
        return mergeSort(p)


def makeList(l):
    n = len(l)
    p = None
    for i in range(n-1,-1,-1):
        q = Node()
        q.val = l[i]
        q.next = p
        p = q
    return p


def printList(head):
    itr = head
    while itr:
        print(itr.val, end='--->')
        itr = itr.next
    print()

Arr = [2, 1, 3, 6]
head = makeList(Arr)

printList(head)
x = SortH(head, 1)
printList(x)