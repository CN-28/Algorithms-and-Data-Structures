#given n**2-length array A sort it, that
#Sum from 0 to n - 1 <= sum from n to 2n - 1 <= ... <= sum from n**2 - n to n**2 - 1

from random import randint
n = 5

def sumSort(Arr, n):
    B = [None for _ in range(n**2)]
    first_maxi = Arr[linearselect(Arr, n - 1)]
    second_maxi = Arr[linearselect(Arr, 2*n - 1)]
    third_mini = Arr[linearselect(Arr, n**2 - n)]
    j = 0
    k = n
    l = n**2 - n
    m = 2*n
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    for i in range(n**2):
        if Arr[i] == first_maxi:
            cnt_1 += 1
        elif Arr[i] == second_maxi:
            cnt_2 += 1
        elif Arr[i] == third_mini:
            cnt_3 += 1
        
        if Arr[i] < first_maxi and j < n:
            B[j] = Arr[i]
            j += 1
        elif first_maxi < Arr[i] < second_maxi and k < 2*n:
            B[k] = Arr[i]
            k += 1
        elif Arr[i] > third_mini and l < n**2:
            B[l] = Arr[i]
            l += 1
        elif Arr[i] > second_maxi and Arr[i] < third_mini:
            B[m] = Arr[i]
            m += 1
    
    for i in range(n**2):
        if B[i] == None:
            if i < n:
                B[i] = first_maxi
                cnt_1 -= 1
            elif n <= i < 2*n:
                if cnt_1 > 0:
                    B[i] = first_maxi
                    cnt_1 -= 1
                else:
                    B[i] = second_maxi
                    cnt_2 -= 1
            elif 2*n <= i < n**2 - n:
                if cnt_2 > 0:
                    B[i] = second_maxi
                    cnt_2 -= 1
                else:
                    B[i] = third_mini
                    cnt_3 -= 1
            else:
                B[i] = third_mini
    
    return B




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
        i = left
        for j in range(left, right):
            if Arr[j] < pivot:
                Arr[i], Arr[j] = Arr[j], Arr[i]
                i += 1

        eq_i = i
        for j in range(i, right):
            if Arr[j] == pivot:
                Arr[eq_i], Arr[j] = Arr[j], Arr[eq_i]
                eq_i += 1

        Arr[eq_i], Arr[right] = Arr[right], Arr[eq_i]
        
        if k < i:
            return i
        if k <= eq_i:
            return k
        return eq_i


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


    return select(A, 0, len(A) - 1, k)



Arr = [randint(1, 25) for _ in range(n**2)]
print(sumSort(Arr, n))
#assume k = n**2
#performance: 3*k + k + k = O(k)