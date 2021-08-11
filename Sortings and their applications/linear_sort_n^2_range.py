#sort in linear time array of length n with numbers from range 0 to n**2 - 1

from random import randint

def countingSort(Arr):
    n = len(Arr)
    count = [0] * n
    res = [0] * n
    for i in range(n):
        count[Arr[i] % n] += 1
    
    for i in range(1, n):
        count[i] += count[i - 1]
    
    for i in range(n - 1, -1, -1):
        count[Arr[i] % n] -= 1
        res[count[Arr[i] % n]] = Arr[i]
        
    for i in range(n):
        Arr[i] = res[i]
    

    count = [0] * n
    for i in range(n):
        count[Arr[i] // n] += 1
    
    for i in range(1, n):
        count[i] += count[i - 1]
    
    for i in range(n - 1, -1, -1):
        count[Arr[i] // n] -= 1
        res[count[Arr[i] // n]] = Arr[i]
        
    for i in range(n):
        Arr[i] = res[i]


n = 10
Arr = [randint(0, n**2 - 1) for _ in range(n)]


countingSort(Arr)
print(Arr)