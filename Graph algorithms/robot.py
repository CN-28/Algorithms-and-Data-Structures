#exam 2021, first exam date, task 2
def robot( L, A, B ):
    n = len(L)
    m = len(L[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    dist = [[(float("inf"), "") for _ in range(m)] for _ in range(n)]
    dist[A[1]][A[0]] = 0, 0
    direction = None
    dirArr = ["r", "b", "l", "t"]
    Arr = [0, 1, -1, 2]

    for _ in range(n):
        for _ in range(m):
            
            mini = float("inf")
            for kk in range(n):
                for l in range(m):
                    if L[kk][l] != "X" and dist[kk][l][0] < mini and not visited[kk][l]:
                        mini, direction = dist[kk][l]
                        u = kk, l

            i, j = u
            visited[i][j] = True
            for rot in Arr:
                cost = abs(rot) * 45
                where = dirArr[(direction + rot) % 4]
                for k in range(1, max(n, m)):
                    if where == "r":
                        if j + k >= m or L[i][j + k] == "X":
                            break
                        if j + k < m and not visited[i][j + k]:
                            if k == 1:
                                if dist[i][j][0] + cost + 60 < dist[i][j + k][0]:
                                    dist[i][j + k] = dist[i][j][0] + cost + 60, (direction + rot) % 4
                            elif k == 2:
                                if dist[i][j][0] + cost + 100 < dist[i][j + k][0]:
                                    dist[i][j + k] = dist[i][j][0] + cost + 100, (direction + rot) % 4
                            else:
                                if dist[i][j][0] + cost + 100 + (k - 2) * 30 < dist[i][j + k][0]:
                                    dist[i][j + k] = dist[i][j][0] + cost + 100 + (k - 2) * 30, (direction + rot) % 4
                    
                    elif where == "b":
                        if i + k >= n or L[i + k][j] == "X":
                            break
                        if i + k < n and not visited[i + k][j]:
                            if k == 1:
                                if dist[i][j][0] + cost + 60 < dist[i + k][j][0]:
                                    dist[i + k][j] = dist[i][j][0] + cost + 60, (direction + rot) % 4
                            elif k == 2:
                                if dist[i][j][0] + cost + 100 < dist[i + k][j][0]:
                                    dist[i + k][j] = dist[i][j][0] + cost + 100, (direction + rot) % 4
                            else:
                                if dist[i][j][0] + cost + 100 + (k - 2) * 30 < dist[i + k][j][0]:
                                    dist[i + k][j] = dist[i][j][0] + cost + 100 + (k - 2) * 30, (direction + rot) % 4
                    
                    elif where == "l":
                        if j - k < 0 or L[i][j - k] == "X":
                            break
                        if j - k >= 0 and not visited[i][j - k]:
                            if k == 1:
                                if dist[i][j][0] + cost + 60 < dist[i][j - k][0]:
                                    dist[i][j - k] = dist[i][j][0] + cost + 60, (direction + rot) % 4
                            elif k == 2:
                                if dist[i][j][0] + cost + 100 < dist[i][j - k][0]:
                                    dist[i][j - k] = dist[i][j][0] + cost + 100, (direction + rot) % 4
                            else:
                                if dist[i][j][0] + cost + 100 + (k - 2) * 30 < dist[i][j - k][0]:
                                    dist[i][j - k] = dist[i][j][0] + cost + 100 + (k - 2) * 30, (direction + rot) % 4
                    
                    elif where == "t":
                        if i - k < 0 or L[i - k][j] == "X":
                            break
                        if i - k >= 0 and not visited[i - k][j]:
                            if k == 1:
                                if dist[i][j][0] + cost + 60 < dist[i - k][j][0]:
                                    dist[i - k][j] = dist[i][j][0] + cost + 60, (direction + rot) % 4
                            elif k == 2:
                                if dist[i][j][0] + cost + 100 < dist[i - k][j][0]:
                                    dist[i - k][j] = dist[i][j][0] + cost + 100, (direction + rot) % 4
                            else:
                                if dist[i][j][0] + cost + 100 + (k - 2) * 30 < dist[i - k][j][0]:
                                    dist[i - k][j] = dist[i][j][0] + cost + 100 + (k - 2) * 30, (direction + rot) % 4
                
    if dist[B[1]][B[0]][0] != float("inf"):
        return dist[B[1]][B[0]][0]