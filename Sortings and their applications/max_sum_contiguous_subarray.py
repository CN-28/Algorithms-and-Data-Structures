#O(n**2) approach
def maxSumSlow(A):
    n = len(A)
    sums = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        sums[i] = sums[i - 1] + A[i - 1]


    maxi = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            maxi = max(maxi, sums[j] - sums[i])
    return maxi



#O(n * log(n)) approach
def maxSumOK(A, left, right):
    if left == right:
        return A[left]
    

    mid = (left + right)//2
    return max(maxSumOK(A, left, mid), maxSumOK(A, mid + 1, right), connectedSum(A, left, right, mid))


def connectedSum(A, left, right, mid):
    curr_sum = 0
    left_sum = -1
    for i in range(mid, left - 1, -1):
        curr_sum += A[i]
        if curr_sum > left_sum:
            left_sum = curr_sum
    
    curr_sum = 0
    right_sum = -1
    for i in range(mid + 1, right + 1):
        curr_sum += A[i]
        if curr_sum > right_sum:
            right_sum = curr_sum


    return max(left_sum, right_sum, left_sum + right_sum)



#O(n) - dynamic programming approach
def maxSumSpeed(A):
    n = len(A)
    last_max = 0
    curr_sum = 0
    for i in range(n):
        curr_sum = max(0, curr_sum + A[i])
        last_max = max(last_max, curr_sum)
    
    return last_max



A = [7, -10, 2, 5, 3, 1, 8, -100, 2]
print(maxSumSlow(A))
print(maxSumOK(A, 0, len(A) - 1))
print(maxSumSpeed(A))