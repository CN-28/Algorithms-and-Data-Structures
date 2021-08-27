from maxFlowEdmondsKarp import edmonds_karp
def solve(G, variables):
    n = 3 * variables + len(G) + 2
    GG = [[0 for _ in range(n)] for _ in range(n)]
    

    A = []
    for i in range(len(G)):
        for var in G[i]:
            if var[-1:] not in A:
                A.append(var[-1:])
    

    for i in range(variables):
        GG[0][i + 1] = 1

    
    i = variables + 1
    j = variables + 1
    indexes = {}
    while j < 3 * variables + 1:
        GG[i - variables][j] = 1
        GG[i - variables][j + 1] = 1
        indexes[A[i - (variables + 1)]] = j, j + 1
        i += 1
        j += 2


    ind = 3 * variables + 1
    for i in range(len(G)):
        for var in G[i]:
            if len(var) == 1:
                GG[indexes[var[-1:]][0]][ind] = 1
            else:
                GG[indexes[var[-1:]][1]][ind] = 1
        GG[ind][n - 1] = 1
        ind += 1


    return edmonds_karp(GG, 0, n - 1) == variables
    


G = [("x", "y", "z"), ("not y", "w"), ("not z", "v"), ("not x", "not w"), ("not v", )]
variables = 5
print(solve(G, variables))