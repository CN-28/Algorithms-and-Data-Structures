#Good start is a vertex, from which you can get to all other vertices. Check if a "good start" exists in a graph.
#time complexity: O(V + E)
def DFS(G):
    n = len(G)
    visited = [False for _ in range(n)]
    time = 0
    v_good = -1
    def DFSVisit(G, i):
        nonlocal time, v_good
        visited[i] = True
        for v in G[i]:
            if not visited[v]:
                DFSVisit(G, v)

        time += 1
        if time == n:
            v_good = i

    for i in range(n):
        if not visited[i]:
            DFSVisit(G, i)
    
    return v_good
    

def DFSOnce(G, visited, i):
    visited[i] = True
    for v in G[i]:
        if not visited[v]:
            DFSOnce(G, visited, v)


G = [[1], [2, 3], [], [4], []]

v_good = DFS(G)
visited = [False for _ in range(len(G))]
DFSOnce(G, visited, v_good)
temp = 1
for check in visited:
    if not check:
        print(False)
        temp = 0
        break
if temp:
    print(True)