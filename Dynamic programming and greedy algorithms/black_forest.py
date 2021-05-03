def f(V, i):
    if i in memoF:
        return memoF[i]
    if i == 0:
        memoF[i] = V[0]
        return memoF[i]
    memoF[i] = g(V, i-1) + V[i]
    return memoF[i]


def g(V, i):

    if i in memoG:
        return memoG[i]
    if i == 0:
        memoG[i] = 0
        return memoG[i]
    memoG[i] = max(f(V, i-1),g(V, i-1))
    return memoG[i]

V = [2,3,5,7,1,11,13,0,0,17]
memoG = {}
memoF = {}
print(g(V, len(V)))