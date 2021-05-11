"""
Given array of (P_i -profits for completing the task on time, D_i - deadlines for i-th task).
Completing one task lasts 1 unit of time. Find the subset of tasks, which can be completed on time and leads to the maximum profit. 
"""


def max_profit(Arr, time):
    Arr.sort()
    Arr = Arr[::-1]
    T = [-1 for _ in range(time + 1)]
    for p, d in Arr:
        temp = d
        if T[d] == -1:
            T[d] = p
        else:
            while T[temp] != -1 and temp > 0:
                temp -= 1
            if T[temp] == -1:
                T[temp] = p

        
    res = 0
    for i in range(time + 1):
        if T[i] != -1:
            res += T[i]

    return res


time = 8
Arr = [(8, 1), (4, 0), (7, 2), (5, 4), (4, 5), (4, 3)]
print(max_profit(Arr, time))