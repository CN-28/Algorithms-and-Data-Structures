#there is array with ceil(logn) different values, sort array

#first approach, O(n * log(log(n)))
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


index = 0
for i in range(len(temp)):
    for j in range(count[i]):
        Arr[index] = temp[i]
        index += 1

print(Arr)
print()


#second approach using dictionary, O(n)
A = [3, 2, 1, 1, 2, 3, 3, 2]
hashmap = {}
n = len(A)
for i in range(n):
    if A[i] in hashmap:
        hashmap[A[i]] += 1
    else:
        hashmap[A[i]] = 1

temp = []
for k in hashmap:
    temp.append(k)
temp.sort()

i = 0
j = 0
while j < len(temp):
    while hashmap[temp[j]] != 0:
        hashmap[temp[j]] -= 1
        A[i] = temp[j]
        i += 1
    j += 1
print(A)