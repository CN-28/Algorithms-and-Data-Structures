from queue import PriorityQueue


def getSum(T, i, j, n, m, oilSum):
    if i + 1 < m and T[i + 1][j] != 0:
        oilSum[0] += T[i + 1][j]
        T[i + 1][j] = 0
        getSum(T, i + 1, j, n, m, oilSum)
    if j + 1 < n and T[i][j + 1] != 0:
        oilSum[0] += T[i][j + 1]
        T[i][j + 1] = 0
        getSum(T, i, j + 1, n, m, oilSum)
    if i - 1 >= 0 and T[i - 1][j] != 0:
        oilSum[0] += T[i - 1][j]
        T[i - 1][j] = 0
        getSum(T, i - 1, j, n, m, oilSum)
    if j - 1 >= 0 and T[i][j - 1] != 0:
        oilSum[0] += T[i][j - 1]
        T[i][j - 1] = 0
        getSum(T, i, j - 1, n, m, oilSum)



def plan(T):
    m = len(T[0])
    n = len(T)
    G = [[T[i][j] for j in range(m)] for i in range(n)]
    for j in range(m):
        oilSum = [G[0][j]]
        G[0][j] = 0
        if oilSum[0] != 0:
            getSum(G, 0, j, n, m, oilSum)
        G[0][j] = oilSum[0]

    
    i = 0
    tanked = G[0][0]
    G[0][0] = 0
    Q = PriorityQueue()
    res = []
    res.append(0)
    while i < m:
        if tanked >= m - i - 1:
            break
        if G[0][i] != 0:
            Q.put((-G[0][i], i))
        if tanked == 0:
            temp = Q.get()
            res.append(temp[1])
            tanked = -temp[0]
        if tanked > 0:
            tanked -= 1
            i += 1
        
    return sorted(res)