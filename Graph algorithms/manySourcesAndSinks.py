from maxFlowEdmondsKarp import edmonds_karp
def solve(G, vertices):
    n = len(G)
    GG = [[G[i][j] if i < n and j < n else 0 for j in range(n + 2)] for i in range(n + 2)]
    source = n
    sink = n + 1


    for i in range(n):
        if vertices[i] == "so":
            GG[source][i] = float("inf")
        elif vertices[i] == "si":
            GG[i][sink] = float("inf")

    
    return edmonds_karp(GG, n, n + 1)



G = [
    [0, 5, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 10],
    [0, 5, 0, 0, 1, 0, 0, 0],
    [0, 4, 0, 0, 6, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
vertices = ["so", "", "so", "so", "", "si", "", "si"]
print(solve(G, vertices))