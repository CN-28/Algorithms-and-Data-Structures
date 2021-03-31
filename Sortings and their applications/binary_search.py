def binary_search(A, n, x):
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right)//2
        if A[mid] < x:
            left = mid + 1
        elif A[mid] > x or (A[mid] == x and mid - 1 > 0 and A[mid - 1] == x):
            right = mid - 1
        elif A[mid] == x:
            return mid
        

A = [1,2,2,3,4,5]
print(binary_search(A, len(A), 3))