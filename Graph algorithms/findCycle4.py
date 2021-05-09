#find the cycle of length 4, adjacency matrix, time complexity: O(n**3)
def findCycle4(G):
    n = len(G)
    for i in range(n):
        for j in range(i + 1, n):
            cnt = 0
            for k in range(n):
                if G[i][k] == G[j][k] == 1:
                    cnt += 1
            if cnt > 1:

                cnt_2 = 0
                for k in range(n):
                    if G[i][k] == G[j][k] == 1:
                        print(k, end=" ")
                        cnt_2 += 1
                        if cnt_2 == 2:
                            break

                print(i, j)
                return True


    return False



G = [
    [-1, 0, 0, 1, 1, 0],
    [0, -1, 0, 1, 1, 1],
    [0, 0, -1, 1, 1, 1],
    [1, 1, 1, -1, 0, 0],
    [1, 1, 1, 0, -1, 0],
    [0, 1, 1, 0, 0, -1]
]
"""
G = [
    [-1, 1, 1, 1, 1, 1],
    [1, -1, 1, 1, 1, 1],
    [1, 1, -1, 1, 1, 1],
    [1, 1, 1, -1, 1, 1],
    [1, 1, 1, 1, -1, 1],
    [1, 1, 1, 1, 1, -1]
]
"""
"""
G = [
    [-1, 0, 0, 1, 0, 0],
    [0, -1, 1, 1, 0, 0],
    [0, 1, -1, 0, 0, 1],
    [1, 1, 0, -1, 1, 0],
    [0, 0, 0, 1, -1, 1],
    [0, 0, 1, 0, 1, -1]
]
"""
print(findCycle4(G))