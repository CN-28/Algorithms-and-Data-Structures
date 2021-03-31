#given word u and v, check if it is possible to build word w, you don't need to use all letters


u = "abc"
v = "cdev"
w = "abcccdev"

def build(u, v, w):
    count = [0]*26
    n = max(len(u), len(v), len(w))
    for i in range(n):
        if i < len(w):
            count[ord(w[i]) - 97] += 1
        if i < len(u):
            count[ord(u[i]) - 97] -= 1
        if i < len(v):
            count[ord(v[i]) - 97] -= 1
    
    for i in range(26):
        if count[i] > 0:
            return False
    return True

print(build(u, v, w))