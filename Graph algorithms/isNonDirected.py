#time complexity: O(V + E)
def isNonDirected(G):
    n = len(G)
    cnt = 0
    for u in range(n):
        for v in G[u]:
            if u < v:
                cnt += 1
            else:
                cnt -= 1
    
    if cnt != 0:
        return True
    return False
    


#directed
G = [[3, 4, 5], [4, 5], [3, 5], [0, 2], [0, 1], [0, 1, 2]]
#nondirected
G = [[1, 2], [], [3], []]
print(isNonDirected(G))