#In array there are n heights of soldiers, they line up in decreasing order by height
#return an array with heights of soldiers from position p to q

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


def section(T, p, q):
    temp = []
    for i in range(p - 1, q):
        temp.append(Arr[linearselect(Arr, i)])
    return temp


Arr = [188, 165, 174, 190, 169, 178, 185, 179, 182]
print(section(Arr, 1, 5))

#performance: O((q - p + 1)*n)