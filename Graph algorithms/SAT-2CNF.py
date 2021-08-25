def SAT_2CNF(formula):
    n = len(formula)
    G = {}
    for a, b in formula:
        if a[:3] == "not":
            G[a[-1:]] = []
            G[a] = []
        else:
            G["not " + a] = []
            G[a] = []

        if b[:3] == "not":
            G[b[-1:]] = []
            G[b] = []
        else:
            G["not " + b] = []
            G[b] = []
    

    for a, b in formula:
        if a[:3] == "not":
            G[a[-1:]].append(b)
        else:
            G["not " + a].append(b)

        if b[:3] == "not":
            G[b[-1:]].append(a)
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
                not_cnt[literal[len(literal) - 1:]] = True
            else:
                cnt[literal] = True


        for literal in component:
            if literal in not_cnt and literal in cnt:
                return False


    return True

    

#satisfiable
formula = [('x', 'y'), ('not x', 'z'), ('not z', 'not y')]
print(SAT_2CNF(formula))
#unsatisfiable
formula = [('x', 'y'), ('y', 'not x'), ('x', 'not y'), ('not x', 'not y')]
print(SAT_2CNF(formula))