def prev(T, i):
    left = 0
    right = i - 1
    mid = None
    while left <= right:
        mid = (left + right) // 2
        if T[mid][2] >= T[i][1]:
            right = mid - 1
        else:
            left = mid + 1

    return left - 1



def select_buildings(T, p):
    n = len(T)
    T = [(T[i][0], T[i][1], T[i][2], T[i][3], i) for i in range(n)]
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
            h, a, b, w, _ = T[i]
            if j - w >= 0 and prevArr[i] != -1:
                F[i][j] = max(F[prevArr[i]][j - w] + h * (b - a), F[i][j])
    
    
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



#test cases
T, p = [(2, 1, 5, 3), (3, 7, 9, 2), (2, 8, 11, 1)], 6
T, p = [(8, 2, 6, 2), (9, 4, 8, 5), (9, 8, 9, 2), (3, 10, 15, 1)], 7
T, p = [(7, 23, 24, 1), (2, 10, 14, 3), (7, 17, 22, 1), (9, 20, 22, 2), (4, 19, 22, 8), (2, 2, 6, 1)], 10
T, p = [(1, 8, 12, 5), (4, 7, 8, 2), (3, 2, 3, 6), (9, 7, 8, 5), (8, 21, 22, 8), (5, 4, 7, 10), (1, 21, 24, 10), (7, 14, 16, 1)], 32
print(select_buildings(T, p))