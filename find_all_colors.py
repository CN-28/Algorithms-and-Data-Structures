#find in array the smallest range with all colors
#there are k colors, which are mapped as integers from 0 to k - 1
from random import randint

def colors(Arr):
    n = len(Arr)
    i = j = 0
    temp = [0 for _ in range(k)]
    cnt = 0
    col_cords = (0, n - 1)
    while i < n and j < n - 1:
        if temp[Arr[j]] == 0:
            cnt += 1
            if cnt == k:
                temp[Arr[j]] += 1

        if cnt != k:
            temp[Arr[j]] += 1
            j += 1
        else:
            if j - i < col_cords[1] - col_cords[0]:
                col_cords = i, j
            temp[Arr[i]] -= 1
            if temp[Arr[i]] == 0:
                cnt -= 1
            i += 1
    
    return col_cords






n = 20
k = 5
Arr = [randint(0, k - 1) for _ in range(n)]
print(Arr)
print(colors(Arr))