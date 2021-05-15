"""
The captain wants to get to the port. He has the map - M of size nxn, where M[j][i] is the depth of the bay at position (i , j).
Starting from (0, 0) check whether it is possible for the captain to get to the port, which is at position (n - 1, n - 1).
The captain can move to the next position only if exactly one of the coordinates differs by 1 from the current position
and the depth of the bay at the next position is greater than T.
"""
def solve(M, T):
    n = len(M)
    visited = [[False for _ in range(n)] for _ in range(n)]


    def DFSVisit(i, j):
        if i == n - 1 and j == n - 1:
            return True

        visited[i][j] = True
        if i + 1 < n and not visited[i + 1][j] and M[j][i + 1] > T:
            if DFSVisit(i + 1, j):
                return True
        if j + 1 < n and not visited[i][j + 1] and M[j + 1][i] > T:
            if DFSVisit(i, j + 1):
                return True
        if i - 1 >= 0 and not visited[i - 1][j] and M[j][i - 1] > T:
            if DFSVisit(i - 1, j):
                return True
        if j - 1 >= 0 and not visited[i][j - 1] and M[j - 1][i] > T:
            if DFSVisit(i, j - 1):
                return True


    if DFSVisit(0, 0):
        return True
    return False



M = [
    [5, 2, 2, 2, 2, 4],
    [2, 3, 1, 1, 5, 3],
    [1, 4, 1, 5, 4, 4],
    [1, 5, 5, 4, 1, 2],
    [1, 5, 4, 3, 4, 2],
    [1, 3, 5, 3, 1, 2]
]


print(solve(M, 1))