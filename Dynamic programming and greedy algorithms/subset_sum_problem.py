def isSubsetSum(A, sum):
    n = len(A)
    subset = [[False for i in range(sum + 1)] for i in range(n + 1)]
     

    for i in range(n + 1):
        subset[i][0] = True
         

    for i in range(1, sum + 1):
         subset[0][i]= False


    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j < A[i-1]:
                subset[i][j] = subset[i-1][j]
            elif j >= A[i-1]:
                subset[i][j] = subset[i-1][j] or subset[i - 1][j-A[i-1]]
     
   
    return subset[n][sum]
         


A = [3, 34, 4, 12, 5, 2]
sum = 34
print(isSubsetSum(A, sum))
