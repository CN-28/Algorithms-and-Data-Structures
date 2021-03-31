from random import randint
def select(Arr, left, right, k):
    while True:
        
        if left == right:
            return Arr[left]
        
        pivot_index = left + randint(1, 10000) % (right - left + 1)
        pivot_index = partition(Arr, left, right, pivot_index)
        
        if k == pivot_index:
            return Arr[k]
        elif k < pivot_index:
            right = pivot_index - 1
        else:
            left = pivot_index + 1
        
    

def partition(Arr, left, right, pivot_index):
    pivot = Arr[pivot_index]
    i = left - 1
    j = right + 1
    while True:
        
        i += 1
        while Arr[i] < pivot:
            i += 1

        j -= 1
        while Arr[j] > pivot:
            j -= 1
        
        if i >= j:
            return j
        Arr[i], Arr[j] = Arr[j], Arr[i]

Arr = [4, 2, 3, 1, 6, 4, 7]
print(select(Arr, 0, len(Arr) - 1, 5))