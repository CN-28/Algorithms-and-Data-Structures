class Node():
  def __init__(self):
    self.value = None
    self.next = None

def merge(L1,L2):
  L = Node()
  tail = L
  f1 = L1.next
  f2 = L2.next
  while f1 and f2:
    if f1.value < f2.value:
      tail.next = f1
      f1 = f1.next
    else:
      tail.next = f2
      f2 = f2.next
    tail = tail.next
  if f1:
    tail.next = f1
  if f2:
    tail.next = f2
  return L

def printing(L):
  while L:
    print(L.value,end=" ")
    L = L.next
  print()

def insert(L,el):
  start = L
  while L.next:
    L = L.next
  L.next = el
  return start

n1 = Node()
n2 = Node()
for i in range(0,6,2):
  a = Node()
  a.value = i
  insert(n1,a)
for i in range(1,7,2):
  a = Node()
  a.value = i
  insert(n2,a)
printing(n1)
printing(n2)
printing(merge(n1,n2))

n3 = Node()
for i in range(8,-1, -2):
  a = Node()
  a.value = i
  insert(n3, a)
printing(n3)

def mergeSort(first):
  if not first or not first.next:
    return first
  
  mid = first
  last = first

  while last.next and last.next.next:
    mid = mid.next
    last = last.next.next
  
  rightll_head = mid.next
  mid.next = None

  L = mergeSort(first)
  R = mergeSort(rightll_head)

  sortedll_head = merge1(L, R)
  return sortedll_head

def merge1(left, right):
  if not left:
    return right
  if not right:
    return left
  
  res = None
  if left.value <= right.value:
    res = left
    res.next = merge1(left.next, right)
  else:
    res = right
    res.next = merge1(left, right.next)
  
  return res

res = mergeSort(n3.next)
printing(res)


def merge(T, l, m, r):
    inver=0
    new = [0 for _ in range(r-l+1)]
    idx = 0
    i = l
    j = m+1
    while i <= m and j <= r:
        if T[j] >= T[i]:
            new[idx] = T[i]
            i += 1
        else:
            inver += m-i+1
            new[idx] = T[j]
            j += 1
        idx += 1

    while i <= m:
        new[idx] = T[i]
        i += 1
        idx += 1
    while j <= r:
        inver += m-i+1
        new[idx] = T[j]
        j += 1
        idx += 1

    idx = 0
    for i in range(l, r+1):
        T[i] = new[idx]
        idx += 1
    return inver


def mergeSort(T, l, r):
    inver=0
    if l < r:
        m = (r+l)//2
        inver += mergeSort(T, l, m)
        inver += mergeSort(T, m+1, r)
        inver += merge(T, l, m, r)
    return inver

T=[2,3,5,1,2,10]
ret = mergeSort(T,0,len(T)-1)
print(T)
print(ret)


def find_leader(arr):
  n = len(arr)
  leader = -1
  cnt = 0
  for i in range(n):
    if cnt == 0:
      leader = arr[i]
      cnt = 1
    
    elif leader == arr[i]:
      cnt += 1
    
    else:
      cnt -=1
  
  if cnt == 0:
    return None

  cnt = 0
  for j in range(n):
    if arr[j] == leader:
      cnt += 1
  
  if cnt >= n // 2 + 1:
    return True
  return False

arr = [1, 2, 2, 2, 4]
arr1 = [1, 4, 7, 8, 8, 8]
print(find_leader(arr))
print(find_leader(arr1))