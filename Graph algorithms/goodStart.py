#Good start is a vertex, from which you can get to all other vertices. Check if a "good start" exists in a graph.
#time complexity: O(V + E)
def DFS(G):
    n = len(G)
    visited = [False for _ in range(n)]
    v_good = -1
    for i in range(n):
        if not visited[i]:
            v_good = i
            DFSVisit(G, visited, i)
    

    return v_good
    


def DFSVisit(G, visited, i):
    visited[i] = True
    for v in G[i]:
        if not visited[v]:
            DFSVisit(G, visited, v)



def goodStart(G):  
    v_good = DFS(G)
    visited = [False for _ in range(len(G))]
    DFSVisit(G, visited, v_good)
    for check in visited:
        if not check:
            return False
    
    return True, v_good



G = [[], [0], [1, 3, 4], [], []]
print(goodStart(G))