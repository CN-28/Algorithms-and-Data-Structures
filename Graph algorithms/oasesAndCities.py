def oasesAndCities(G, A):
    n = len(G)    
    visited = [False for _ in range(n)]
    def DFSVisit(u):
        visited[u] = True
        temp.append(u)
        for v in G[u]:
            if not visited[v] and A[v] == "O":
                DFSVisit(v)


    superOases = []
    cnt_cities = 0
    for u in range(n):
        if A[u] == "C":
            cnt_cities += 1

        temp = []
        if not visited[u] and A[u] == "O":
            DFSVisit(u)
        if temp:
            superOases.append(temp)


    oasesMap = [0 for _ in range(n)]
    for i in range(len(superOases)):
        for v in superOases[i]:
            oasesMap[v] = i + 1
    
    
    toBeDeleted = [False for _ in range(n)]
    for u in range(n):
        if A[u] == "C" and oasesMap[G[u][0]] == oasesMap[G[u][1]] != 0:
            toBeDeleted[u] = True
    

    degree = [0 for _ in range(n)]
    for u in range(n):
        if A[u] == "O":
            for v in G[u]:
                if A[v] == "C" and not toBeDeleted[v] and oasesMap[u] != 0:
                    degree[oasesMap[u]] += 1
    
    
    for i in range(n):
        if degree[i] % 2 != 0:
            return False

    return True



G = [
    [1, 6],
    [0, 2, 3, 4],
    [1, 3],
    [1, 2, 4],
    [1, 3, 5],
    [4, 6],
    [0, 5]
]
A = ["C", "O", "C", "O", "O", "C", "O"]
print(oasesAndCities(G, A))
G = [
    [1, 6],
    [0, 2, 3, 4, 7],
    [1, 3],
    [1, 2, 4],
    [1, 3, 5],
    [4, 6],
    [0, 5, 7],
    [1, 6] 
]
A = ["C", "O", "C", "O", "O", "C", "O", "C"]
print(oasesAndCities(G, A))