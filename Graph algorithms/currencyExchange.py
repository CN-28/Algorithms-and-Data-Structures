#Check if you can benefit from currency exchange, all exchanges can be done.
from math import log
def exchange(G):
    n = len(G)
    dist = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] != 0 and G[i][j] != 1:
                dist[i][j] = 1/log(G[i][j])
    

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dist[j][k] > dist[j][i] + dist[i][k]:
                    dist[j][k] = dist[j][i] + dist[i][k]

    
    for i in range(n):
        if dist[i][i] < 0:
            return True
    return False


G = [
    #PLN
    [0, 0.25, 0.33],
    #EUR
    [4, 0, 1],
    #USD
    [5, 1, 0]
]
print(exchange(G))