'''how many rectangular containers can be fully filled with water with
given A units of water and coordinates of top left and bottom right corners of the container?
'''


#mergeSort for containers, sorting by top left corner's y value
def mergeSort(Arr):
    temp = [Arr[i] for i in range(len(Arr))]
    def merge(Arr, f, l):
        if f < l:
            mid = (f + l)//2
            merge(Arr, f, mid)
            merge(Arr, mid + 1, l)
            sort(Arr, f, mid, l)
    
    def sort(Arr, f, mid, l):
        i = j = 0
        for k in range(f, l + 1):
            if i <= mid and (mid + 1 + j >= l + 1 or Arr[f + i][0][1] <= Arr[mid + 1 + j][0][1]):
                temp[k] = Arr[f + i]
                i += 1
            else:
                temp[k] = Arr[mid + 1 + j]
                j += 1
        
        for k in range(f, l + 1):
            Arr[k] = temp[k]

    merge(Arr, 0, len(Arr) - 1)




containers = [((2, 13), (3, 11)), ((3, 7), (5, 5)), ((11, 14), (14, 10)), ((6, 12), (8, 9)), ((7, 6), (10, 2)), ((13, 8), (16, 1))]
mergeSort(containers)


def solve(A, containers):
    left = 0
    right = len(containers) - 1
    filled = 0
    while left <= right:
        mid = (left + right)//2
        temp = A
        temp -= (containers[mid][0][1] - containers[mid][1][1]) * (containers[mid][1][0] - containers[mid][0][0])
        for i in range(len(containers)):
            if i != mid and containers[i][0][1] <= containers[mid][0][1]:
                temp -= (containers[i][0][1] - containers[i][1][1]) * (containers[i][1][0] - containers[i][0][0])
            elif i != mid and containers[i][1][1] < containers[mid][0][1]:
                temp -= (containers[mid][0][1] - containers[i][1][1]) * (containers[i][1][0] - containers[i][0][0])

        if temp > 0 and mid + 1 > filled:
            filled = mid + 1
            left = mid + 1
        elif temp == 0:
            filled = mid + 1
            break
        else:
            right = mid - 1
    
    return filled

print(solve(53, containers))