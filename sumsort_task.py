#given n**2-length array A sort it, that
#Sum from 0 to n - 1 <= sum from n to 2n - 1 <= ... <= sum from n**2 - n to n**2 - 1

from random import randint
n = 5

def quicksort(Arr):
    def sort(Arr, left, right):
        if left < right:
            pivot_index = partition(Arr, left, right)
            sort(Arr, left, pivot_index - 1)
            sort(Arr, pivot_index + 1, right)
    

    def partition(Arr, left, right):
        pivot = Arr[right][0]

        i = left - 1
        for j in range(left, right):
            if Arr[j][0] <= pivot:
                i += 1
                Arr[i], Arr[j] = Arr[j], Arr[i]
        Arr[i + 1], Arr[right] = Arr[right], Arr[i + 1]
        
        return i + 1
    sort(Arr, 0, len(Arr) - 1)


def sumSort(Arr, n):
    temp = []
    B = [0 for _ in range(n**2)]
    sum = 0
    for i in range(n**2):
        sum += Arr[i]
        if i != 0 and (i + 1) % n == 0:
            temp.append((sum, i  + 1 - n))
            sum = 0
    print(temp)
    quicksort(temp)
    k = 0
    start = temp[k][1]
    for i in range(n**2):
        if i != 0 and i % 5 == 0:
            k += 1
        B[i] = Arr[temp[k][1] + i % 5]
    
    return B
        



Arr = [randint(1, 25) for _ in range(n**2)]
print(Arr)
print(sumSort(Arr, n))
#assume quicksort working in linearitmic time
#performance: n**2 + n*logn + n**2 = O(n**2)