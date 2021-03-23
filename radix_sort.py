#radix sort for numbers

from random import randint

def countingSort(Arr, digit):
    n = len(Arr)
    count = [0] * 10
    res = [0] * n
    for i in range(n):
        index = Arr[i]//digit
        count[index % 10] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    for i in range(n - 1, -1, -1):
        index = Arr[i]//digit
        count[index % 10] -= 1
        res[count[index % 10]] = Arr[i]
        

    for i in range(n):
        Arr[i] = res[i]


def radixSort(Arr):
    maxi = max(Arr)

    digit = 1
    while maxi//digit != 0:
        countingSort(Arr, digit)
        digit *= 10


n = 10
Arr = [randint(0, n**2 - 1) for _ in range(n)]


radixSort(Arr)
print(Arr)