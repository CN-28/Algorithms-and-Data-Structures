#n is length of the words and k is the size of the used alphabet
#performance: O(n + k)
def isAnagram1(A, B):
    if len(A) != len(B):
        return False
    
    mini, maxi = float('inf'), 0
    for i in range(len(A)):
        maxi = max(ord(A[i]), ord(B[i]), maxi)
        mini = min(ord(A[i]), ord(B[i]), mini)

    count = [0] * (maxi - mini + 1)

    for i in range(len(A)):
        count[ord(A[i]) - mini] += 1
        count[ord(B[i]) - mini] -= 1
    
    for i in range(len(count)):
        if count[i] != 0:
            return False
    
    return True


A = 'accga'
B = 'aacgc'
print(isAnagram1(A, B))


#performance: O(n)
def isAnagram2(A, B):
    if len(A) != len(B):
        return False
    
    mini, maxi = float('inf'), 0
    for i in range(len(A)):
        maxi = max(ord(A[i]), ord(B[i]), maxi)
        mini = min(ord(A[i]), ord(B[i]), mini)

    count = [0] * (maxi - mini + 1)

    for i in range(len(A)):
        count[ord(A[i]) - mini] += 1
        count[ord(B[i]) - mini] -= 1
    
    for i in range(len(A)):
        if count[ord(A[i]) - mini] != 0:
            return False
    
    return True

A = 'accga'
B = 'aacgc'
print(isAnagram2(A, B))