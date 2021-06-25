#Exam 2020, task 3, first exam date
import math
def InsertionSort(tab):
    for i in range(1, len(tab)):
        elem = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > elem:
            tab[j + 1] = tab[j]
            j = j - 1
        tab[j + 1] = elem

                 
    
def fast_sort(tab, a):
    n = len(tab)
    print(n)
    buckets = [[] for _ in range(n)]
    bucketRange = 1/n
    for i in range(n):
        buckets[int(math.log(tab[i], a)//bucketRange)].append(tab[i])
    k = 0
    for i in range(n):
        InsertionSort(buckets[i])
        for j in range(len(buckets[i])):
            tab[k] = buckets[i][j]
            k += 1

    return tab