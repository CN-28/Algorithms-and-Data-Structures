A = [5, 1, 6, 2, 7, 55, 4, 0]

maxi = A[0]
mini = A[0]

for i in range(len(A)//2):
    if A[i] < A[len(A) - 1 - i] and A[i] < mini:
        mini = A[i]
    elif A[len(A) - 1 - i] < mini:
        mini = A[len(A) - 1 - i]

    if A[i] > A[len(A) - 1 - i] and A[i] > maxi:
        maxi = A[i]
    elif A[len(A) - 1 - i] > maxi:
        maxi = A[len(A) - 1 - i]

print(maxi, mini)