#Time complexity: O(n * log(n))
def findInterval(A):
    n = len(A)
    print(A)
    for i in range(n):
        A[i] = A[i], i

    start = sorted(A)
    end = sorted(A, reverse=True)
    end.sort(key = lambda x: x[0][1])
    

    i = 0
    j = 0
    timetable = []
    while i < n and j < n:
        if start[i][0][0] < end[j][0][1]:
            timetable.append((start[i], "s"))
            i += 1
        else:
            timetable.append((end[j], "e"))
            j += 1
    
    while j < n:
        timetable.append((end[j], "e"))
        j += 1
    
    
    counters = [0 for _ in range(len(timetable))]
    cnt = 0
    cnt1 = 0
    for i in range(len(timetable)):
        if timetable[i][1] == "s":
            cnt += 1
            counters[i] = cnt
        if timetable[i][1] == "e":
            cnt1 += 1
            counters[i] = cnt1
    

    res = [0 for _ in range(n)]
    for i in range(len(timetable)):
        if timetable[i][1] == "s":
            res[timetable[i][0][1]] -= counters[i]
        else:
            res[timetable[i][0][1]] += counters[i]
    
    return A[res.index(max(res))][0]
        


#test cases
#A = [(1, 3), (0, 9), (7, 8), (3, 8)]
#A = [(1, 4), (2, 3), (5, 9), (6, 10), (2, 11)]
#A = [(1, 9), (0, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (0, 8)]
#A = [(0, 5), (3, 4), (2, 9), (7, 8), (6, 11)]
#A = [(0, 4), (1, 4), (2, 4), (5, 9), (6, 8)]
A = [(2, 9), (0, 7), (3, 8), (4, 5), (6, 7)]
print(findInterval(A))