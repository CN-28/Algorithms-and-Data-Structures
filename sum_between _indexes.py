#find the sum of numbers which after sorting would be from indexes p to q inclusive

def linearselect(Arr, k):
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
    
    return select(Arr, 0, len(Arr) - 1, k)
    

def sumBetween(T, p, q):
    mini = T[linearselect(T, p)]
    maxi = T[linearselect(T, q)]
    suma = mini + maxi
    for i in range(len(T)):
        if T[i] < maxi and T[i] > mini:
            suma += T[i]
    
    return suma


Arr = [23, 1, 5, 41, 10, 15, 29]
print(sumBetween(Arr, 0, 3))

#performance O(n)