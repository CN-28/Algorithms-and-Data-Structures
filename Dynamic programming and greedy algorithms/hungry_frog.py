"""
Find the minimum number of frog jumps to get from index 0 to n - 1, with given
array A with energy potions on each index, to get to j-th index from i-th frog need to consume
j - i energy points, frog starts with 0 energy points, and energy points mustn't drop below 0
"""
def solve(A):
    n = len(A)
    F = [(float("inf"), 0) for _ in range(n)]

    F[0] = 0, A[0]
    for i in range(1, n):
        for j in range(i):
            mana = F[j][1]
            if mana >= i - j and F[j][0] + 1 < F[i][0]:
                F[i] = F[j][0] + 1, mana - (i - j) + A[i]
                
            

    return F[n - 1][0]



A = [6, 3, 5, 4, 7, 2, 3, 1, 3, 1, 1, 1, 1, 1]
print(solve(A))