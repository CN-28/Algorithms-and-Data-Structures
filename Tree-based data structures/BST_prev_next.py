class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None



def insert(x, key):
    if not x:
        return BSTNode(key)
    
    
    if key < x.key:
        x.left = insert(x.left, key)
        x.left.parent = x
    else:
        x.right = insert(x.right, key)
        x.right.parent = x
    
    return x



def findMax(x):
    while x.right:
        x = x.right
    return x



def findMin(x):
    while x.left:
        x = x.left
    return x



def findPrev(x):
    if x.left:
        return findMax(x.left)
    

    y = x.parent
    while y and x == y.left:
        x = y
        y = y.parent
    return y



def findNext(x):
    if x.right:
        return findMin(x.right)
    

    y = x.parent
    while y and x == y.right:
        x = y
        y = y.parent
    return y



values = [15, 10, 20, 8, 12, 14, 25]
root = None
for val in values:
    root = insert(root, val)


print(findNext(root).key)
print(findPrev(root.left.right).key)