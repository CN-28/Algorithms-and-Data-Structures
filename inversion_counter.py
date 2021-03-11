def merge(T, f, mid, l):
    L = T[f:mid + 1]
    R = T[mid + 1: l + 1] 
    L.append(float('inf'))
    R.append(float('inf'))
    
    inv_cnt = 0

    i = j = 0
    for k in range(f, l + 1):
        if L[i] <= R[j]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = R[j]
            j += 1
            inv_cnt += 1
    
    return inv_cnt



def mergesort(T, f, l):
    if f == l:
        return 0

    mid = (f + l)//2
    inv_cnt = 0

    inv_cnt += mergesort(T, f, mid)
    inv_cnt += mergesort(T, mid + 1, l)
    inv_cnt += merge(T, f, mid, l)

    return inv_cnt

A = [1, 9, 6, 4, 5]
print(mergesort(A, 0, len(A) - 1))