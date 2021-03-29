#find the interval that contains the most intervals
intervals = [(1, 4), (2, 3), (5, 9), (6, 10), (2, 11)]

def mergeSort(A, s):
    temp = [A[i] for i in range(len(A))]
    def merge(A, left, right):
        if left < right:
            mid = (left + right)//2
            merge(A, left, mid)
            merge(A, mid + 1, right)
            sort(A, left, mid, right)
    
    def sort(A, left, mid, right):
        i = j = 0
        for k in range(left, right + 1):
            if i <= mid and (mid + 1 + j >= right + 1 or A[left + i][s] <= A[mid + 1 + j][s]):
                temp[k] = A[left + i]
                i += 1
            else:
                temp[k] = A[mid + j + 1]
                j += 1
        
        for k in range(left, right + 1):
            A[k] = temp[k]

    merge(A, 0, len(A) - 1)    


def solve(intervals):
    mergeSort(intervals, 1)
    temp = intervals.copy()
    mergeSort(intervals, 0)
    print(temp, intervals)
    maxi = 0, -1
    for i in range(len(intervals)):
        cnt = 0
        for j in range(len(temp)):
            if temp[j][0] >= intervals[i][0] and temp[j][1] <= intervals[i][1]:
                cnt += 1
            elif temp[j][0] > intervals[i][1]:
                break
        if cnt > maxi[0]:
            maxi = cnt, i
    if maxi[1] != -1:
        return intervals[maxi[1]]

print(solve(intervals))