from collections import deque

#using Adjacency list
#Time Complexity: O(V + E), V - number of vertices, E - number of edges
def isBipartite(G):
    n = len(G)
    queue = deque()
    colour = [-1 for i in range(n)]
    queue.append((G[0], 0))
    colour[0] = 1


    while queue:
        u = queue.popleft()
        for i in range(len(u)):
            if colour[u[0][i]] == colour[u[1]]:
                return False
            
            if colour[u[0][i]] == -1:
                colour[u[0][i]] = 1 - colour[u[1]]
                queue.append((G[u[0][i]], u[0][i])) 
            
        
    return True



G = [[3, 4, 5], [4, 5], [3, 5], [0, 2], [0, 1], [0, 1, 2]]
print(isBipartite(G))


#using Adjacency Matrix
#Time Complexity: O(V*V)
def isBipartite_alt(G):
    n = len(G)
    queue = deque()
    colour = [-1 for i in range(n)]
    queue.append(0)
    colour[0] = 1


    while queue:
        u = queue.popleft()
        for i in range(n):
            if G[u][i] == 1:
                if colour[u] == colour[i]:
                    return False
                
                if colour[i] == -1:
                    colour[i] = 1 - colour[u]
                    queue.append(i)
    
    
    return True
                


G = [
    [-1, 0, 0, 1, 1, 1],
    [0, -1, 0, 0, 1, 1],
    [0, 0, -1, 1, 0, 1],
    [1, 0, 1, -1, 0, 0],
    [1, 1, 0, 0, -1, 0],
    [1, 1, 1, 0, 0, -1]
]
print(isBipartite_alt(G))