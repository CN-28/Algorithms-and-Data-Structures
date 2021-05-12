"""
Load the trailer to get maximum possible space filled taking as little items as we can.
All items' weights are powers of 2.
"""
def solve(W, K):
    n = len(W)
    W.sort(reverse=True)
    print(W)
    i = 0
    cnt = 0
    while True:
        if K - W[i] >= 0:
            K -= W[i]
            print(W[i], end=" ")
            cnt += 1
        i += 1
        if i >= n:
            print()
            break

    return cnt


K = 25
W = [4, 2, 8, 1, 2, 1, 16]
print(solve(W, K))