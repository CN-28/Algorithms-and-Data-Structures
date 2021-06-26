def prev(T, i):
    a = 0
    b = len(T) - 1
    while a <= b:
        mid = (a + b)//2
        if T[mid][2] < T[i][1] and T[mid + 1][2] >= T[i][1] and mid + 1 < len(T):
            return mid
        if T[mid][2] < T[i][1]:
            a = mid + 1
        elif T[mid][2] >= T[i][1]:
            b = mid - 1
    
    if T[mid][2] >= T[i][1]:
        return -1
    
    return mid


def select_buildings(T, p):
    n = len(T)
    for i in range(n):
        T[i] = T[i][0], T[i][1], T[i][2], T[i][3], i
    T.sort(key = lambda x: x[2])
    F = [[0 for _ in range(p)] for _ in range(n)]
    for j in range(p):
        if j - T[0][3] >= 0:
            F[0][j] = T[0][0]*(T[0][2] - T[0][1])
    prevArr = [-1 for _ in range(n)]
    for i in range(1, n):
        prevArr[i] = prev(T, i)



    for i in range(1, n):
        for j in range(p):
            F[i][j] = F[i - 1][j]
            if j - T[i][3] >= 0 and prevArr[i] != -1:
                F[i][j] = max(F[prevArr[i]][j - T[i][3]] + T[i][0]*(T[i][2] - T[i][1]), F[i][j])
    
    
    maxi_ind = 0
    for i in range(1, p):
        if F[n - 1][i] > F[n - 1][maxi_ind]:
            maxi_ind = i

    
    i = n - 1
    j = maxi_ind
    res = []
    while i != -1:
        if i - 1 >= 0 and F[i - 1][j] == F[i][j]:
            i -= 1
        else:
            res.append(T[i][4])
            j -= T[i][3]
            i = prevArr[i]
    
    
    return sorted(res)