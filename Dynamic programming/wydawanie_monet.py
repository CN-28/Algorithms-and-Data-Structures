def mincoins(coins,val):
    n = len(coins)

    t = [100 for _ in range(val+1)]

    t[0] = 0

    for i in range(1,val+1):
        for j in range(n):

            if coins[j] <= i:
                rest = t[i-coins[j]]

                if rest < 100 and rest + 1 < t[i]:
                    t[i] = rest + 1
    print(t)

t = [1,5,8]
mincoins(t,16)