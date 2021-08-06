def quicksort(A, l, r):
    stack = []
    stack.append((l, r))
    while stack:
        l, r = stack.pop()
        while l < r:
            q = partition(A, l, r)
            if q - l > r - q:
                stack.append((l, q - 1))
                l = q + 1
            else:
                stack.append((q + 1, r))
                r = q - 1



def partition(A, l, r):
    i = l - 1
    for j in range(l, r):
        if A[j] < A[r]:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1



A = [3, 2, 1, 5, 4]
quicksort(A, 0, len(A) - 1)
print(A)