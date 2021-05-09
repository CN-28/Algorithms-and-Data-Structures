#find a deletion order for the n vertices such that no deletion disconnects the graph using DFS
#using adjacency matrix, time complexity: O(V*V)
def DFS_AM(G):
    def DFSVisit(G, i):
        visited[i] = True
        for j in range(n):
            if G[i][j] == 1 and not visited[j]:
                DFSVisit(G, j)
        
        deleteOrder.append(i)
        
        
    n = len(G)
    visited = [False for _ in range(n)]
    deleteOrder = []
    for i in range(n):
        if not visited[i]:
            DFSVisit(G, i)
    

    return deleteOrder

    

G = [
    [-1, 0, 0, 1, 1, 1],
    [0, -1, 0, 0, 1, 1],
    [0, 0, -1, 1, 0, 1],
    [1, 0, 1, -1, 0, 0],
    [1, 1, 0, 0, -1, 0],
    [1, 1, 1, 0, 0, -1]
]
print(DFS_AM(G))


#using adjacency list, time complexity: O(V + E)
def DFS_AL(G):
    def DFSVisit(G, i):
        visited[i] = True
        for j in range(len(G[i])):
            if not visited[G[i][j]]:
                DFSVisit(G, G[i][j])
            
        deleteOrder.append(i)


    n = len(G)
    visited = [False for _ in range(n)]
    deleteOrder = []
    for i in range(n):
        if not visited[i]:
            DFSVisit(G, i)


    return deleteOrder



G = [[3, 4, 5], [4, 5], [3, 5], [0, 2], [0, 1], [0, 1, 2]]
print(DFS_AL(G))


#find a deletion order for the n vertices such that no deletion disconnects the graph using BFS
#using adjacency list, time complexity: O(V + E) 
from collections import deque

def BFS_AL(G):
    n = len(G)
    queue = deque()
    visited = [False for _ in range(n)]
    visited[0] = True
    queue.append(G[0])
    deletionOrder = []
    deletionOrder.append(0)

    while queue:
        u = queue.popleft()
        for i in range(len(u)):
            if not visited[u[i]]:
                visited[u[i]] = True
                queue.append(G[u[i]])
                deletionOrder.append(u[i])

    return deletionOrder[::-1]


G = [[3, 4, 5], [4, 5], [3, 5], [0, 2], [0, 1], [0, 1, 2]]
print(BFS_AL(G))