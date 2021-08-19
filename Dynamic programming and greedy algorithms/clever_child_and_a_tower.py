"""
A group of m children try to build the tallest possible tower. Every kid has the bricks of different size.
The first child has w1, ... , w1,n1, the second w2, ... w2,n2 etc. The kids went to eat dinner, but one clever child stayed.
Now he has the only chance to pick up some bricks from other children so that he has the highest tower.
Implement the quickest algorithm to solve this problem, which takes the little number of bricks (note that the number wi,j can be very large).
Treat towers as a sets, not stack (we can take any bricks that we want from the particular tower).
"""
from copy import deepcopy
def buildTower(A, ind_child):
    n = len(A)
    sums = [sum(A[i]) for i in range(n)]
    for tower in A:
        tower.sort()

    
    copy_A = deepcopy(A)
    copy_sums = deepcopy(sums)
    mini_cnt = float("inf")
    for i in range(n):
        cnt = float("inf")
        if i != ind_child:
            temp = False
            cnt = 0
            while sums[ind_child] <= copy_sums[i] or not temp:
                maxi = 0
                ind = -1
                maxi_all = 0
                ind_all = -1
                temp = True
                for j in range(n):
                    if j != ind_child:
                        if len(A[j]) > 0 and A[j][len(A[j]) - 1] > maxi and sums[j] > copy_sums[i]:
                            temp = False
                            maxi = A[j][len(A[j]) - 1]
                            ind = j

                        if len(A[j]) > 0 and A[j][len(A[j]) - 1] > maxi_all:
                            maxi_all = A[j][len(A[j]) - 1]
                            ind_all = j


                if ind != -1:
                    x = A[ind].pop()
                    sums[ind] -= x
                    sums[ind_child] += x
                    cnt += 1
                elif sums[ind_child] <= copy_sums[i]:
                    x = A[ind_all].pop()
                    sums[ind_all] -= x
                    sums[ind_child] += x
                    cnt += 1
                

        mini_cnt = min(cnt, mini_cnt)
        A = deepcopy(copy_A)
        sums = deepcopy(copy_sums)
    
        
    return mini_cnt
            


towers = [
    [9, 4],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [2,2,2,2,2,2,2],
    [7,4,1],
    [9, 2]
]
#towers = [[], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [5,5,5,1], [6,6,6,1]]
#towers = [[1, 1], [8], [5, 4]]
print(buildTower(towers, 0))