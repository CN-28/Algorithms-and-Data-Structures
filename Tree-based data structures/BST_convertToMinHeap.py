def findMin(x):
    while x.left:
        x = x.left
    return x


def findNext(x):
    if x.right:
        return findMin(x.right)
    

    y = x.parent
    while y and x == y.right:
        x = y
        y = y.parent
    return y



def ConvertTree(p):
    l = []
    x = findMin(p)
    while x:
        l.append(x)
        x = findNext(x)
    
   
    n = len(l)
    for i in range(n):
        if 2 * i + 1 < n:
            l[i].left = l[2 * i + 1]
        else:
            l[i].left = None
        if 2 * i + 2 < n:
            l[i].right = l[2 * i + 2]
        else:
            l[i].right = None
        if (i - 1) // 2 >= 0:
            l[i].parent = l[(i - 1) // 2]
        else:
            l[i].parent = None
    return l[0]