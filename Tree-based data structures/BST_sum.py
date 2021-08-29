#compute sum of all nodes in bst in O(n) time and O(1) space complexity
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.parent = None



def sumAll(root):
    if not root:
        return 0

    while root.left:
        root = root.left
    

    total = 0
    while True:
        total += root.key
        if root.right:
            root = root.right
            while root.left:
                root = root.left
        else:
            while root.parent and root.parent.right == root:
                root = root.parent
            
            if not root.parent:
                break
            
            if root.parent.left == root:
                root = root.parent

    return total
            
        
    
def insert(key, root=None):
    if not root:
        return BSTNode(key)
    
    x = root
    while x:
        y = x
        if key > x.key:
            x = x.right
            if not x:
                y.right = BSTNode(key)
                y.right.parent = y
        else:
            x = x.left
            if not x:
                y.left = BSTNode(key)
                y.left.parent = y



A = [20, 15, 25, 14, 17, 23, 27, 22, 24]
root = None
for i in range(len(A)):
    if i == 0:
        root = insert(A[i])
    else:
        insert(A[i], root)


print(sumAll(root))