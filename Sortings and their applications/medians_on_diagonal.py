#there is a two dimensional array T of size NxN filled with natural nubmers (all numbers are different)
#transform an array, so that under main diagonal of array there are only smaller numbers than on diagonal and 
#above diagonal there are only bigger numbers than on diagonal

def Median(T):
    n = len(T)
    first = select(T, 0, n**2 - 1, n**2//2 - n//2, n)
    if n == 2:
        last = select(T, 0, 3, 2, 2)
        T[n - 1][n - 1], T[(n**2//2 + n//2 - 1) // n][(n**2//2 + n//2 - 1) % n] = last, T[n - 1][n - 1]
    else:
        last = select(T, 0, n**2 - 1, n**2//2 + n//2, n)
        T[n - 1][n - 1], T[(n**2//2 + n//2) // n][(n**2//2 + n//2) % n] = last, T[n - 1][n - 1]
    T[0][0], T[(n**2//2 - n//2) // n][(n**2//2 - n//2) % n] = first, T[0][0]
    
    

    diag_ind = 1
    for i in range(n):
        for j in range(n):
            if diag_ind == n - 1:
                break
            if last > T[i][j] > first:
                T[i][j], T[diag_ind][diag_ind] = T[diag_ind][diag_ind], T[i][j]
                diag_ind += 1
    

    k = 1
    l = 1
    for i in range(n):
        for j in range(i + 1, n):
            if T[i][j] <= first:
                T[i][j], T[k // n][k // n + (k + k //n) % n] = T[k // n][k // n + (k + k //n) % n], T[i][j]
                k += 1
            if T[j][i] >= last:
                T[j][i], T[l // n + (l + l//n) % n][l // n] = T[l // n + (l + l//n) % n][l // n], T[j][i]
                l += 1
    

    for i in range(n):
        for j in range(i + 1, n):
            if T[i][j] <= first:
                T[i][j], T[j][i] = T[j][i], T[i][j]   
    


def select(Arr, left, right, k, n):
    while True:
        
        if left == right:
            return Arr[left // n][left % n]
        
        pivot_index = left + (right - left + 1) // 2
        pivot_index = partition(Arr, left, right, pivot_index, n)
        
        if k == pivot_index:
            return Arr[k // n][k % n]
        elif k < pivot_index:
            right = pivot_index - 1
        else:
            left = pivot_index + 1
        
    

def partition(Arr, left, right, pivot_index, n):
    pivot = Arr[pivot_index // n][ pivot_index % n]
    i = left - 1
    j = right + 1
    while True:
        
        i += 1
        while Arr[i // n][i % n] < pivot:
            i += 1

        j -= 1
        while Arr[j // n][j % n] > pivot:
            j -= 1
        
        if i >= j:
            return j
        Arr[i // n][i % n], Arr[j // n][j % n] = Arr[j // n][j % n], Arr[i // n][i % n]