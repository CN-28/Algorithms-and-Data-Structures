#there is a two dimensional array T of size NxN filled with natural nubmers (all numbers are different)
#transform an array, so that under main diagonal of array there are only smaller numbers than on diagonal and 
#above diagonal there are only bigger numbers than on diagonal

def linearselect( A, k ):
    def select(Arr, left, right, k):
        if left == right:
            return left
        
        pivot_index = select_pivot(Arr, left, right)
        pivot_index = partition(Arr, left, right, pivot_index, k)

        if k == pivot_index:
            return k
        elif k < pivot_index:
            return select(Arr, left, pivot_index - 1, k)
        else:
            return select(Arr, pivot_index + 1, right, k)
    

    def partition(Arr, left, right, pivot_index, k):
        pivot = Arr[pivot_index]
        Arr[pivot_index], Arr[right] = Arr[right], Arr[pivot_index]
        i = left - 1
        for j in range(left, right):
            if Arr[j] <= pivot:
                i += 1
                Arr[i], Arr[j] = Arr[j], Arr[i]
        Arr[i + 1], Arr[right] = Arr[right], Arr[i + 1]
        
        return i + 1


    def select_pivot(Arr, left, right):
        if right - left + 1 <= 5:
            return medianOf5(Arr, left, right)
        
        for i in range(left, right + 1, 5):
            median_of_group = medianOf5(Arr, i, min(i + 4, right))
            Arr[median_of_group], Arr[left + (i - left)//5] = Arr[left + (i - left)//5], Arr[median_of_group]
        
        mid = (right - left)//10 + left + 1
        return select(Arr, left, left + (right - left)//5, mid)
            

    def medianOf5(Arr, left, right):
        for i in range(left + 1, right + 1):
            j = i
            while j > left and Arr[j - 1] > Arr[j]:
                Arr[j - 1], Arr[j] = Arr[j], Arr[j - 1]
                j -= 1
        
        return (left + right)//2


    return A[select(A, 0, len(A) - 1, k)]


def solve(T):
    n = len(T)
    Arr = [T[i][j] for i in range(len(T)) for j in range(len(T))]
    if n % 2 == 1:
        left = linearselect(Arr, n**2//2 - n//2)
        right = linearselect(Arr, n**2//2 + n//2)
    else:
        left = linearselect(Arr, n**2//2 - n//2)
        right = linearselect(Arr, n**2//2 + n//2 - 1)
    k = 1
    l = 0


    o = 1
    m = 0


    j = 0
    for i in range(n**2):
        if j < n and right >= Arr[i] >= left:
            T[j][j] = Arr[i]
            j += 1
        elif l < n - 1 and Arr[i] > right:
            T[l][k] = Arr[i]
            k += 1
            if k % n == 0:
                l += 1
                k = l + 1
        elif o < n:
            T[o][m] = Arr[i]
            m += 1
            if m % o == 0:
                o += 1
                m = 0


T = [ [ 2, 3, 5],
[ 7,11,13],
[17,19,23] ]


solve(T)

for x in T:
    print(x)
