from random import randint
n = 10
Arr = [randint(0, 55) for _ in range(n)]

def counting_sort(Arr, k):
    count = [0]*k
    for i in range(len(Arr)):
        count[Arr[i]] += 1


    for i in range(k):
        count[i] += count[i - 1]


    res = [0] * n
    for i in range(n - 1, -1, -1):
        count[Arr[i]] -= 1
        res[count[Arr[i]]] = Arr[i]
    
    return res

print(counting_sort(Arr, 55))
