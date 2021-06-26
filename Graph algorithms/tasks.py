#EXAM 2020, task 3, second exam date
def tasks(T):
    n = len(T)
    visited = [False for _ in range(n)]
    top_sorted = []
    def DFSVisit(i):
        visited[i] = True
        for j in range(n):
            if T[i][j] == 2 and not visited[j]:
                DFSVisit(j)
        top_sorted.append(i)


    for i in range(n):
        if not visited[i]:
            DFSVisit(i)
    
    return top_sorted


T = [[0,2,1,1], [1,0,1,1], [2,2,0,1], [2,2,2,0]]
print(tasks(T))