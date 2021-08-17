def TSP(S):
    n = len(S)
    all = (1 << n) - 1
    dist = [[float("inf") if i != j else 0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = ((S[i][1] - S[j][1])**2 + (S[i][2] - S[j][2])**2)**(1/2)

    F = [[float("inf") for _ in range(n)] for _ in range(1 << n)]
    parent = [[-1 for _ in range(n)] for _ in range(1 << n)]


    def solve(pos=0, mask=1):
        if mask == all:
            return dist[pos][0]
        
        if F[mask][pos] != float("inf"):
            return F[mask][pos]


        for city in range(n):
            if mask & (1 << city) == 0:
                ans = dist[pos][city] + solve(city,  mask | (1 << city))
                if ans < F[mask][pos]:
                    F[mask][pos] = ans
                    parent[mask][pos] = city
        
        return F[mask][pos]
    
    
    res = solve()
    path = []
    index = 0
    mask = 1
    while True:
        path.append(S[index])
        index = parent[mask][index]
        if index == -1:
            break
        mask = mask | (1 << index)

    return res, path



C = [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1]]
print(TSP(C))