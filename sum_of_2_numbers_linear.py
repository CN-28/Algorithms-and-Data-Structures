#finding sum of 2 elements of sorted array in linear time

def findingsum(A, sum):
    i = 0
    j = len(A) - 1
    sum_curr =  A[i] + A[j]
    while i < j:
        if sum_curr > sum:
            j -= 1
            sum_curr = A[i] + A[j]
        elif sum_curr < sum:
            i += 1
            sum_curr = A[i] + A[j] 
        elif sum_curr == sum:
            return i, j
        else:
            return False

n = int(input())
sum = int(input())
A = [_ for _ in range(n)]
print(A)
print(findingsum(A, sum))