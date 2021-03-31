def partition(Arr, p, r):
    pivot = Arr[r]
    i = p - 1
    for j in range(p, r):
        if Arr[j] <= pivot:
            i += 1
            Arr[i], Arr[j] = Arr[j], Arr[i]

    Arr[i + 1], Arr[r], = Arr[r], Arr[i + 1]
    return i + 1


def quicksort(Arr, p, r):
    size_of_stack = r - p + 1
    stack = [0] * size_of_stack

    top_of_stack = -1
    top_of_stack += 1
    stack[top_of_stack] = p
    top_of_stack += 1
    stack[top_of_stack] = r

    while top_of_stack >= 0:
        r = stack[top_of_stack]
        top_of_stack -= 1
        p = stack[top_of_stack]
        top_of_stack -= 1

        q = partition(Arr, p, r)

        if q - 1 > p:
            top_of_stack += 1
            stack[top_of_stack] = p
            top_of_stack += 1
            stack[top_of_stack] = q - 1
        
        if q + 1 < r:
            top_of_stack += 1
            stack[top_of_stack] = q + 1
            top_of_stack += 1
            stack[top_of_stack] = r


Arr = [4, 1, 5, 7, 3, 4, 3]
quicksort(Arr, 0, len(Arr) - 1)
print(Arr)