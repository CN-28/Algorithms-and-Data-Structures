from random import randint
n = 10
Arr = [randint(0, 55) for _ in range(n)]

def counting_sort(Arr, k):
    n = len(Arr)
    count = [0]*(k + 1)
    for i in range(n):
        count[Arr[i]] += 1


    for i in range(1, k + 1):
        count[i] += count[i - 1]


    res = [0] * n
    for i in range(n - 1, -1, -1):
        count[Arr[i]] -= 1
        res[count[Arr[i]]] = Arr[i]
    
    for i in range(n):
        Arr[i] = res[i]


counting_sort(Arr, 55)
print(Arr)