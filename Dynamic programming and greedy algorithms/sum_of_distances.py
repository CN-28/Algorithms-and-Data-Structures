"""
A - sorted array with n numbers, find x, such that sum from i = 0 to i = n - 1, such that
|A[i] - x| takes the minimum value.
"""
def solve(A):
    n = len(A)
    if n % 2 == 0:
        median = (A[n//2 - 1] + A[n//2])/2
    else:
        median = A[n//2]
    return median


A = [1, 2, 5, 7, 10, 12]
print(solve(A))