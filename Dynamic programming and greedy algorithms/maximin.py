"""
Divide an array into k subarrays, such that the minimum sum from all subarrays is maximized
"""
def maximin(A, k):
    n = len(A)
    sums = [0 for i in range(n + 1)]
    F = [[0 for _ in range(k)] for _ in range(n + 1)]
    S = [[-1 for _ in range(k)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        sums[i] += sums[i - 1] + A[i - 1]
 
    for i in range(n + 1):
        F[i][0] = sums[i]

    index = -1
    for i in range(2, n + 1):
        for t in range(1, min(i, k)):
            maxi = 0
            for j in range(i, 0, -1):
                mini = min(F[i - j][t - 1], sums[i] - sums[i - j])
                if mini > maxi:
                    maxi = mini
                    index = i - j
            F[i][t] = maxi
            S[i][t] = index
    
    
    res = []
    index = S[n][k - 1]
    cnt = k - 1
    end = n
    while True:
        res.append(A[index: end])
        cnt -= 1
        if cnt == -1:
            break
        end = index
        index = S[index][cnt]
        if index == -1:
            index = 0 


    return res[::-1], F[n][k - 1]



A = [5, 1, 3, 9, 15, 2, 4, 7, 0]
print(maximin(A, 4))