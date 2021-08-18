def select(A):
    n = len(A)
    A = sorted(A, key = lambda x : x[1])
    res = [A[0]]


    for i in range(1, n):
        if A[i][0] >= res[len(res) - 1][1]:
            res.append(A[i])
    
    return res



A = [(27, 39), (13, 23), (1, 9), (3, 7), (8, 15), (17, 21), (6, 15), (20, 28), (31, 37), (14, 23)]
print(select(A))