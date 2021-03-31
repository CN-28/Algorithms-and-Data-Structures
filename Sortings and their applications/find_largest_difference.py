#find largest difference of numbers that are next to each other in linear time


def find(Arr):
    n = len(Arr)
    maxi = max(Arr)
    mini = min(Arr)
    buckets = [[] for _ in range(n)]
    bucket_range = (maxi - mini)/(n - 1)

    for i in range(len(Arr)):
        buckets[int((Arr[i] - mini)//bucket_range)].append(Arr[i])
    
    res = 0
    maxi = max(buckets[0])
    for i in range(1, len(buckets)):
        if len(buckets[i]) != 0:
            res = max(res, min(buckets[i]) - maxi)
            maxi = max(buckets[i])
    print(buckets)
    return res

Arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 35]
print(find(Arr))
Arr.sort()
print(Arr)