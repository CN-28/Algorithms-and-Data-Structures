#T[N] filled with rational values from k intervals located in array P, for each interval there is probability of choosing number from this interval
#number from the interval is chosen from a uniform distribution, sort array T


def SortTab(T,P):
    def InsertionSort(tab):
        for i in range(1, len(tab)):
            elem = tab[i]
            j = i - 1
            while j >= 0 and tab[j] > elem:
                tab[j + 1] = tab[j]
                j = j - 1
            tab[j + 1] = elem

    N = len(T)
    array_of_buckets = []
    for i in range(len(P)):
        bucket = [[] for _ in range(int(P[i][2]*N))]
        array_of_buckets.append(bucket)
    
    
    for i in range(N):
        for j in range(len(P)):
            bucket_range = (P[j][1] - P[j][0])/int(P[j][2]*N)
            if int((T[i] - P[j][0])//bucket_range) < len(array_of_buckets[j]):
                array_of_buckets[j][int((T[i] - P[j][0])//bucket_range)].append(T[i])
                break

    l = 0
    for j in range(len(array_of_buckets)):
        for k in range(len(array_of_buckets[j])):
            InsertionSort(array_of_buckets[j][k])
            for m in range(len(array_of_buckets[j][k])):
                T[l] = array_of_buckets[j][k][m]
                l += 1

P = [(1,5, 0.75) , (4,8, 0.25)]
T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]
SortTab(T, P)
print(T)