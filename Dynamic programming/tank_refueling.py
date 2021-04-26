#L - fuel tank capacity, S - array of distances from start to i-th gas station, P - price per liter for each gas station

def minNumberOfRefuel(L_MAX, S, t):
    L_curr = L_MAX
    cnt = 0
    i = 0
    curr = 0
    n = len(S)
    while True:
        if t - curr <= L_curr:
            return cnt


        if n == 0 or i == n or S[i] - curr > L_curr:
            return False

        L_curr -= (S[i] - curr)
        curr = S[i]
        i += 1 
        

        if (i == n and t - curr > L_curr) or S[i] - curr > L_curr:
            L_curr = L_MAX
            cnt += 1

         

#we can refuel as much as we want to
def minCostToDest1(L_MAX, S, P, t):
    n = len(S)
    P = [(P[i], S[i]) for i in range(n)]
    P.sort()
    print(P)
    

    L_curr = L_MAX
    cost = 0
    curr = 0
    while True:
        if t - curr <= L_curr:
            return cost

        
        temp = False
        for j in range(n):
            if P[j][1] > curr and P[j][1] - curr <= L_curr:
                L_curr -= (P[j][1] - curr)
                curr = P[j][1]

                temp = True
                break
        
        if not temp:
            return False

        temp1 = False
        for k in range(n):
            if P[k][1] > curr and P[k][1] - curr <= L_MAX:
                if P[k][0] < P[j][0]:
                    cost += (P[k][1] - P[j][1] - L_curr) * P[j][0]
                    L_curr += (P[k][1] - P[j][1] - L_curr)
                else:
                    if t - curr <= L_MAX:
                        cost += (t - curr - L_curr)*P[j][0]
                        return cost

                    cost += (L_MAX - L_curr)*P[j][0]
                    L_curr = L_MAX
                temp1 = True
                break
        
        
        if not temp1:
            if t - curr <= L_MAX:
                cost += abs(L_curr - (t - curr))*P[j][0]
                return cost
        
        
        
#we must refuel to fill whole fuel tank
def minCostToDest2(L_MAX, S, P, t):
    L_curr = L_MAX

    S.append(t)
    n = len(S)
    F = [(float("inf"), float("inf")) for _ in range(n)]
    if S[0] > L_MAX:
        return False
    F[0] = 0, L_MAX - S[0]
    
    for i in range(1, n):
        for j in range(i + 1):
            if j - 1 == -1:
                if S[i] <= L_MAX:
                    F[i] = 0, L_MAX - S[i]
            else:
                cost = F[j - 1][0] + (L_MAX - F[j - 1][1])*P[j - 1]
                if cost < F[i][0] and S[i] - S[j - 1] <= L_MAX:
                    F[i] = cost, L_MAX - (S[i] - S[j - 1])
    return F[n - 1][0]


            


     

        


L_MAX = 50
S = [2, 5, 9, 14, 16, 23, 51, 54]
P = [4.5, 4.1, 3.5, 4.7, 5, 5.2, 3.6, 4.3]

L_MAX = 14
S = [1, 9, 15, 16, 17, 27, 28]
P = [1, 100, 10, 15, 1, 30, 30]
t = 30



print("a)")
print(minNumberOfRefuel(L_MAX, S, 55))
print("b1)")
print(minCostToDest1(L_MAX, S, P, t))
print("b2)")
print(minCostToDest2(L_MAX, S, P, t))