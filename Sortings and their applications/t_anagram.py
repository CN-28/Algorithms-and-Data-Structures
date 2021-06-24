from collections import deque

def tanagram(x, y, t):
    n = len(x)
    positions = [deque() for _ in range(26)]
    for i in range(n):
        positions[ord(y[i]) - 97].append(i)
    for i in range(n):
        if len(positions[ord(x[i]) - 97]) == 0:
            return False
        closest = positions[ord(x[i]) - 97].popleft()
        if abs(closest - i) > t:
            return False


    return True