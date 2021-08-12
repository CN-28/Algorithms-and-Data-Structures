#Time complexity: O(n * log(n))
def lis(A):
    n = len(A)
    prev = [-1 for _ in range(n)]
    last = [-1 for _ in range(n)]


    last[0] = 0
    length = 1
    for i in range(1, n):
        left = 0
        right = length - 1
        mid = None
        while left <= right:
            mid = (left + right) // 2
            if A[last[mid]] < A[i]:
                left = mid + 1
            else:
                right = mid - 1
    
    
        prev[i] = last[left - 1]
        last[left] = i
        length = max(length, left + 1)
        

    res = [None for _ in range(length)]
    index = last[length - 1]
    for i in range(length - 1, -1, -1):
        res[i] = A[index]
        index = prev[index]
    
    return res


A = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
print(lis(A))