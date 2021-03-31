#find the most common k-length substring of the n-length string

def find(word, k):
    n = len(word)
    temp = []
    for i in range(n - k + 1):
        temp.append(word[i: i + k])
    radixSort(temp, k)
    print(temp)

    cnt = 1
    maxi = temp[0], 1
    for i in range(1, len(temp)):
        if temp[i] == temp[i - 1]:
            cnt += 1
        else:
            if cnt > maxi[1]:
                maxi = temp[i - 1], cnt
            cnt = 1
    if cnt > maxi[1]:
        maxi = temp[i - 1], cnt

    return maxi[0]
    

def radixSort(Arr, k):
    for j in range(k - 1, -1, -1):
        counting_sort(Arr, j)


def counting_sort(Arr, j):
    n = len(Arr)
    count = [0]*2
    res = [0] * n
    for i in range(n):
        if Arr[i][j] == 'a':
            count[0] += 1
        else:
            count[1] += 1
        
    count[1] += count[0]

    for i in range(n - 1, -1, -1):
        if Arr[i][j] == 'a':
            count[0] -= 1
            res[count[0]] = Arr[i]
        else:
            count[1] -= 1
            res[count[1]] = Arr[i]

    for i in range(n):
        Arr[i] = res[i]
        



print(find("ababaaaabb", 3))

#performance: O((n - k)*k)