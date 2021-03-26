#single digit - occurs once in the number, multiple digit - occurs more than once in the number
#Number A is prettier than B if in A there is more single digits than in B, then if we still can't decide
#prettier is that one with less multiple numbers, otherwise they are equally pretty

def countingSort(Arr, elem, option):
    n = len(Arr)
    count = [0] * 10
    res = [0] * n

    for i in range(n):
        count[Arr[i][elem]] += 1
    
    if option == "D":
        for i in range(n - 2, -1, -1):
            count[i] += count[i + 1]
        
    else:
        for i in range(1, n):
            count[i] += count[i - 1]

    
    for i in range(n - 1, -1, -1):
            count[Arr[i][elem]] -= 1
            res[count[Arr[i][elem]]] = Arr[i]

    for i in range(n):
        Arr[i] = res[i]



def pretty_sort(T):
    n = len(T)
    count = [[0 for _ in range(10)] for _ in range(n)]
    for i in range(n):
        temp = T[i]
        while temp != 0:
            count[i][temp % 10] += 1
            temp //= 10
    
    
    for i in range(n):
        cnt = 0
        cnt_mult = 0
        for j in range(10):
            if count[i][j] == 1:
                cnt += 1
            elif count[i][j] > 1:
                cnt_mult += 1
        count[i] = (Arr[i], cnt, cnt_mult)
        
    countingSort(count, 2, "A")
    countingSort(count, 1, "D")

    #description of count array - (number, number of single digits, number of multiple digits)
    for x in count:
        print(x)
    print()

    for i in range(n):
        T[i] = count[i][0]


Arr = [123, 455, 1266, 114577, 2344, 67333]
pretty_sort(Arr)
print(Arr)

#let d - maximal length of the number in array
#performance: O(10*n + d*n + 10*n + 2n + n) = O(d*n)