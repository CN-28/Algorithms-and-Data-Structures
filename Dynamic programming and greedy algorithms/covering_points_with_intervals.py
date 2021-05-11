"""
Given X - array of points, find the minimum number of intervals of size 1
needed to cover all points from X
"""
def solve(X):
    n = len(X)
    X.sort()
    cnt = 1
    curr = X[0]
    for i in range(1, n):
        if X[i] - curr >= 1:
            cnt += 1
            curr = X[i]

    return cnt


X = [2.7, 1.6, 1.7, 1.8, 1.9, 2.0, 2.8]
print(solve(X))