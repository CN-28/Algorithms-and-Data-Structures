#exam 2021, 0 exam date
from collections import deque
def tanagarm(x, y, t):
    n = len(x)
    count = [deque() for _ in range(26)]
    for i in range(n):
        count[ord(x[i]) - ord('a')].append(i)
    
    for i in range(n):
        if not count[ord(y[i]) - ord('a')] or abs(count[ord(y[i]) - ord('a')].popleft() - i) > t:
            return False
    return True


A = "kotomysz"
B = "tokmysoz"
print(tanagarm(A, B, 3))