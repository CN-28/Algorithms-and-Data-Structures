#there is n-length sorted array filled with different n odd numbers
#someone chose ceil(logn) elements and replaced them with random even numbers, sort this array

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
            if (mid + 1 + j > right or Arr[left + i] <= Arr[mid + 1 + j]) and left + i <= mid:
                temp[k] = Arr[left + i]
                i += 1
            else:
                temp[k] = Arr[mid + 1 + j]
                j += 1
        
        for k in range(left, right + 1):
            Arr[k] = temp[k]

    merge(Arr, 0, len(Arr) - 1)





def solve(Arr):
    n = len(Arr)
    temp = []
    for i in range(n):
        if Arr[i] % 2 == 0:
            temp.append(Arr[i])
    mergeSort(temp)
    
    res = []
    j = 0
    i = 0
    while i < len(Arr):
        if Arr[i] % 2 == 1 and (j >= len(temp) or Arr[i] < temp[j]):
            res.append(Arr[i])
            i += 1
        elif Arr[i] % 2 == 1:
            res.append(temp[j])
            j += 1
        else:
            i += 1
            if Arr[i] % 2 == 1 and (j >= len(temp) or Arr[i] < temp[j]):
                res.append(Arr[i])
                i += 1
            elif Arr[i] % 2 == 1:
                res.append(temp[j])
                j += 1
    
    return res
        







Arr = [1, 3, 5, 7, 24, 18, 13, 15, 4, 19, 21, 23, 25, 27, 2, 31]
print(Arr)
print(solve(Arr))

#performance: n + logn*log(logn) + n = O(n)