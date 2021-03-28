#sort an array of n strings, all strings are different lengths

def sort(Arr):
    n = len(Arr)
    mini = maxi = len(Arr[0])
    for i in range(n//2):
        left = len(Arr[i])
        right = len(Arr[n - 1 - i])
        if left >= right:
            if left > maxi:
                maxi = left
            if right < mini:
                mini = right
        elif left < right:
            if right > maxi:
                maxi = right
            if left < mini:
                mini = left
    

    buckets = ["" for _ in range(maxi - mini + 1)]
    
    for i in range(n):
        buckets[len(Arr[i]) - mini] = Arr[i]


    for i in range(maxi - mini, - 1, -1):
        if buckets[i] != "":
            counting_sort(buckets, i)
            
    for i in range(n):
        Arr[i] = buckets[i]


def counting_sort(Arr, index):
    count = [0] * 26
    n = len(Arr)
    res = [""]*n
    for i in range(index, n):
        if Arr[i] != "":
            count[ord(Arr[i][index]) - 97] += 1
    
    for i in range(1, 26):
        count[i] += count[i - 1]


    for i in range(n - 1, index - 1, -1):
        if Arr[i] != "":
            count[ord(Arr[i][index]) - 97] -= 1
            res[count[ord(Arr[i][index]) - 97] + index] = Arr[i]
    
    for i in range(index, n):
        Arr[i] = res[i]
    
         




Arr = ["asd", "lkhgsasdf", "a", "qustgai", "bb", "cccc", "duqngouy", "asdfqw", "agfad", "sdfgawdawdawdaw"]
sort(Arr)
print(Arr)