#exam 2021, first exam date, task 1
def mergesort(T, opt):
    temp = [T[i] for i in range(len(T))]
    def merge(T, f, m, l, opt):
        i = j = 0
        for k in range(f, l + 1):
            if (f + i) <= m and (m + 1 + j >= l + 1 or T[f + i][opt] <= T[m + 1 + j][opt]):
                temp[k] = T[f + i]
                i += 1
            else:
                temp[k] = T[m + 1 + j]
                j += 1
    
        for k in range(f, l + 1):
            T[k] = temp[k]
    

    def sort(T, opt, f=0, l=len(T) - 1):
        if f < l:
            m = (f + l)//2
            sort(T, opt, f, m)
            sort(T, opt, m + 1, l)
            merge(T, f, m, l, opt)

    sort(T, opt)
    return T


def chaos_index( T ):
    n = len(T)
    for i in range(n):
        T[i] = (T[i], i)
    T = mergesort(T, 1)
    T = mergesort(T, 0)
    k = 0
    for i in range(n):
        if abs(i - T[i][1]) > k:
            k = abs(i - T[i][1])
    
    return k