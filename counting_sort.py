from random import randint
n = 10
Arr = [randint(0, n**2 - 1) for _ in range(n)]

count = [0]*(n**2)
for i in range(len(Arr)):
    count[Arr[i]] += 1


for i in range(n**2):
    count[i] += count[i - 1]


res = [0] * n
for i in range(n - 1, -1, -1):
    count[Arr[i]] -= 1
    res[count[Arr[i]]] = Arr[i]
    

print(res)