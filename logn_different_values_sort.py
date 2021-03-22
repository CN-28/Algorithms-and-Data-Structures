#there is array with ceil(logn) different values, sort array in O(n*log(logn))

#first approach
def binary_search(A, n, x):
    left = 0
    right = n
    while left <= right:
        mid = (left + right)//2
        if A[mid] < x:
            left = mid + 1
        elif A[mid] > x:
            right = mid - 1
        elif A[mid] == x:
            return mid

Arr = [1, 2, 3, 1, 2, 3, 3, 2]
temp = []
count = []
for i in range(len(Arr)):
    index = binary_search(temp, len(temp) - 1, Arr[i])
    if index == None:
        if len(temp) == 0:
            temp.append(Arr[i])
            count.append(1)
        elif temp[len(temp) - 1] < Arr[i]:
            temp.append(Arr[i])
            count.append(1)
        else:
            for j in range(len(temp)):
                if temp[j] > Arr[i]:
                    temp.insert(j, Arr[i])
                    count.insert(j, 1)
                    break
    else:
        count[index] += 1

print(count)
index = 0
for i in range(len(temp)):
    for j in range(count[i]):
        Arr[index] = temp[i]
        index += 1

print(Arr)
print()


#second approach

def partition(T, left, right):
    k = right
    i = left
    j = left
    while j < k:
        if T[j] < T[right]:
            T[i], T[j] = T[j], T[i]
            i += 1
            j += 1
        elif T[j] == T[right]:
            if j == k:
                break
            k -= 1
            T[k], T[j] = T[j], T[k]
        else:
            j += 1
    start = i
    for index in range(k, right+1):
        T[i], T[index] = T[index], T[i]
        i += 1
    return start, i


def quickSort(T, left, right):
    if left < right:
        q, r = partition(T, left, right)
        if q > left:
            quickSort(T, left, q-1)
        if r != right:
            quickSort(T, r, right)


T = [0, 0, 0, 0, 2, 0, 1, 2, 2, 2, 2, 2,
     2, 2, 4, 4, 4, 45, 8, 12, 456, 34, 2]
quickSort(T, 0, len(T)-1)
print(T)