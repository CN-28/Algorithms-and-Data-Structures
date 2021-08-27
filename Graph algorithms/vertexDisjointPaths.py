from maxFlowEdmondsKarp import edmonds_karp
def solve(G, s, t):
    n = len(G)
    GG = [[0 for _ in range(2 * (n - 2) + 2)] for _ in range(2 * (n - 2) + 2)]
    
    start = min(s, t)
    end = max(s, t)
    for i in range(n):
        if i < start:
            GG[i + n][i] = 1
        elif start < i < end:
            GG[i + n - 1][i] = 1
        elif i != start and i != end:
            GG[i + n - 2][i] = 1
        for j in range(n):
            if G[j][i] == 1:
                if i < start:
                    GG[j][i + n] = 1
                elif start < i < end:
                    GG[j][i + n - 1] = 1
                elif i != start and i != end:
                    GG[j][i + n - 2] = 1
            if G[i][t] == 1:
                GG[i][t] = 1
            
    
    return edmonds_karp(GG, s, t) 
    


G = [
    [0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
print(solve(G, 0, 8))