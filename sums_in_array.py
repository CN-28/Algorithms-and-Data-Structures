#check if every number from array is a total of two other numbers from array

def mergeSort(Arr):
    temp = [Arr[i] for i in range(len(Arr))]
    def merge(Arr, left, right):
        if left < right:
            mid = (left + right)//2
            merge(Arr, left, mid)
            merge(Arr, mid + 1, right)
            sort(Arr, left, mid, right)
    
    def sort(Arr, left, mid, right):
        
        i = j = 0
        for k in range(left, right + 1):
            if (mid + 1 + j >= right + 1 or Arr[left + i] <= Arr[mid + 1 + j]) and left + i <= mid:
                temp[k] = Arr[left + i]
                i += 1
            else:
                temp[k] = Arr[mid + 1 + j]
                j += 1
        
        for k in range(left, right + 1):
            Arr[k] = temp[k]
    
    merge(Arr, 0, len(Arr) - 1)


Arr = [-1, 1, 0, -1, 1, 2]
mergeSort(Arr)
print(Arr)


def isSum(Arr, x, index):
    i = 0 
    j = len(Arr) - 1

    while Arr[i] + Arr[j] != x and i < j:
        if Arr[i] + Arr[j] < x:
            i += 1
        else:
            j -= 1

        if i == index:
            i += 1
        elif j == index:
            j -= 1

    if Arr[i] + Arr[j] == x:
        return True
    return False

temp = True
for i in range(len(Arr)):
    if not isSum(Arr, Arr[i], i):
        temp = False
        break

print(temp)

#performance O(nlogn) + O(n**2) = O(n**2)