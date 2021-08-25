def races(G):
    n = len(G)
    formula = []
    for u in range(n):
        if len(G[u]) == 2:
            formula.append((f"({u}, {G[u][0]})", f"({u}, {G[u][1]})"))
            formula.append((f"not ({u}, {G[u][0]})", f"not ({u}, {G[u][1]})"))
        else:
            formula.append((f"({u}, {G[u][0]})", f"({u}, {G[u][0]})"))


    enteringEdges = [[] for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            enteringEdges[v].append((u, v))


    for u in range(len(enteringEdges)):
        if len(enteringEdges[u]) == 2:
            formula.append((f"{enteringEdges[u][0]}", f"{enteringEdges[u][1]}"))
            formula.append((f"not {enteringEdges[u][0]}", f"not {enteringEdges[u][1]}"))
        else:
            formula.append((f"{enteringEdges[u][0]}", f"{enteringEdges[u][0]}"))
    
    
    return SAT_2CNF(formula)



def SAT_2CNF(formula):
    n = len(formula)
    G = {}
    for a, b in formula:
        if a[:3] == "not":
            G[a[-6:]] = []
            G[a] = []
        else:
            G["not " + a] = []
            G[a] = []

        if b[:3] == "not":
            G[b[-6:]] = []
            G[b] = []
        else:
            G["not " + b] = []
            G[b] = []
    

    for a, b in formula:
        if a[:3] == "not":
            G[a[-6:]].append(b)
        else:
            G["not " + a].append(b)

        if b[:3] == "not":
            G[b[-6:]].append(a)
        else:
            G["not " + b].append(a)
    

    return SCC(G)



def SCC(G):
    processingTime = []
    visited = {}
    for v in G:
        visited[v] = False
    

    def getTimes(i):
        visited[i] = True
        for v in G[i]:
            if not visited[v]:
                getTimes(v)
    
        processingTime.append(i)
    

    for v in G:    
        if not visited[v]:
            getTimes(v)


    GG = {}
    for v in G:
        GG[v] = []


    for u in G:
        for v in G[u]:
            GG[v].append(u)

    
    def DFSVisit(i, temp):
        visited[i] = False
        for v in GG[i]:
            if visited[v]:
                DFSVisit(v, temp)

        temp.append(i)
    

    SCC = []
    n = len(processingTime)
    for i in range(n - 1, -1, -1):
        temp = []
        if visited[processingTime[i]]:
            DFSVisit(processingTime[i], temp)
            SCC.append(temp)
       

    for component in SCC:
        not_cnt = {}
        cnt = {}
        for literal in component:
            if literal[:3] == "not":
                not_cnt[literal[-6:]] = True
            else:
                cnt[literal] = True

    
        for literal in component:
            if literal in not_cnt and literal in cnt:
                return False


    return True



G = [[2, 6], [0], [1, 3], [5], [3], [4], [7], [8], [6]]
print(races(G))
G = [[1], [2], [0, 4], [2], [3]]
print(races(G))