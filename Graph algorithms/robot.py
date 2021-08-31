#exam 2021, first exam date, task 2
from queue import PriorityQueue
def robot(L, A, B):
    dp = [[[[-1 for _ in range(3)] for _ in range(4)] for _ in range(len(L[0]))] for _ in range(len(L))]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cost = [60, 40, 30]


    Q = PriorityQueue()
    Q.put((0, A[1], A[0], 0, 0))
    while not Q.empty():
        res, y, x, dir, step = Q.get()
        if (x, y) == B:
            return res
        if dp[y][x][dir][step] != -1:
            continue
        dp[y][x][dir][step] = res

        Q.put((res + 45, y, x, (dir + 1) % 4, 0))
        Q.put((res + 45, y, x, (dir + 3) % 4, 0))

        y += dirs[dir][0]
        x += dirs[dir][1]
        if L[x][y] == 'X':
            continue
        Q.put((res + cost[step], y, x, dir, min(step + 1, 2)))