def isNonDirected(G):
    n = len(G)
    for i in range(n):
        for j in range(len(G[i])):
            temp = False
            for k in range(len(G[G[i][j]])):
                if G[G[i][j]][k] == i:
                    temp = True
                    break
            if not temp:
                return False
    return True


G = [[3, 4, 5], [4, 5], [3, 5], [0, 2], [0, 1], [0, 1, 2]]
print(isNonDirected(G))