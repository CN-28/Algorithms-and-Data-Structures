def mincost(Arr):
    n = len(Arr) - 1
    F = [[float("inf") if i != j else 0 for j in range(n)] for i in range(n)]
    
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            end = i + length - 1
            for j in range(i, end):
                cost = F[i][j] + F[j + 1][end] + Arr[i]*Arr[j + 1]*Arr[end + 1]
                if cost < F[i][end]:
                    F[i][end] = cost

    return F[0][n - 1]

            
                
Arr = [3, 2, 4, 2, 5]
print(mincost(Arr))