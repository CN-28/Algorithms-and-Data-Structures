def inversion_counter(T):

    temp = [T[i] for i in range(len(T))]
    def merge(T, f, m, l):
        i = j = 0
        inv_cnt = 0
        for k in range(f, l + 1):
            if (f + i) <= m and (m + 1 + j >= l + 1 or T[f + i] <= T[m + 1 + j]):
                temp[k] = T[f + i]
                i += 1
            else:
                inv_cnt += m - (f + i) + 1
                temp[k] = T[m + 1 + j]
                j += 1
        
        for k in range(f, l + 1):
            T[k] = temp[k]
        
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

    return mergesort(T, 0, len(A) - 1)


A = [1, 10, 7, 4, 5]
print(inversion_counter(A))