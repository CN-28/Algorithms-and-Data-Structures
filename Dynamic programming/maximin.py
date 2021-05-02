def maximin(Arr, k):
    n = len(Arr)
    sums = [0 for i in range(n)]
    sums[0] = Arr[0]
    for i in range(1, n):
        sums[i] = Arr[i] + sums[i - 1]
    

    F = [[0 for j in range(k)] for i in range(n)]
    S = [[0 for j in range(k)] for i in range(n)]
    for i in range(n):
        F[i][0] = sums[i]
    

    maxi = 0
    index = -1
    for j in range(1, k):
        for i in range(j, n):
            for l in range(j - 1, i):
                if min(F[l][j - 1], sums[i] - sums[l]) > maxi:
                    maxi = min(F[l][j - 1], sums[i] - sums[l])
                    index = l
            S[i][j] = index
            F[i][j] = maxi
            maxi = 0

    
    temp = [-1 for i in range(k)]
    index = n - 1
    for i in range(k - 1, -1, -1):
        temp[i] = S[index][i]
        index = S[index][i]
    
    print(Arr[:temp[1] + 1], end=" ")
    for i in range(2, k):
        print(Arr[temp[i - 1] + 1: temp[i] + 1], end=" ")
    print(Arr[F[n - 1][k - 1] + 1:])


    return F[n - 1][k - 1]



Arr = [5, 3, 2, 6, 7, 4, 9, 6]
print(Arr, end="\n")
k = 5
print(maximin(Arr, k))