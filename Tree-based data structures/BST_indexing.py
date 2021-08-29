class BSTNode:
    def __init__(self, key, num=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.num = num
        self.max_pos = num

    

#finding the k-th largest element
def findKth(root, k):
    if k < 1 or not root:
        return False

    if root.left:
        if root.max_pos - root.left.num == k:
            return root
    else:
        if root.max_pos == k:
            return root
    
    if root.left:
        if k < root.max_pos - root.left.num:
            root.right.max_pos = root.max_pos - root.left.num - 1
            return findKth(root.right, k)
        else:
            root.left.max_pos = root.max_pos
            return findKth(root.left, k)
        

    return False



#given the node, find the position of the node in an array sorted in ascending order
def findK(root):
    x = root
    while x.parent:
        x = x.parent
    
    return utilfindK(x, root.key)


def utilfindK(root, val):
    if not root:
        return
    
    if root.key == val:
        if root.left:
            return root.max_pos - root.left.num
        return root.max_pos

    if root.key < val:
        root.right.max_pos = root.max_pos - root.left.num - 1
        return utilfindK(root.right, val)
    else:
        root.left.max_pos = root.max_pos
        return utilfindK(root.left, val)



def insert(key, num, root=None):
    if not root:
        return BSTNode(key, num)
    

    x = root
    while x:
        y = x
        if key > x.key:
            x = x.right
            if not x:
                y.right = BSTNode(key, num)
                y.right.parent = y
        else:
            x = x.left
            if not x:
                y.left = BSTNode(key, num)
                y.left.parent = y 



A = [(20, 9), (24, 5), (15, 3), (13, 1), (17, 1), (25, 1), (22, 3), (21, 1), (23, 1)]
for i in range(len(A)):
    if i == 0:
        root = insert(A[i][0], A[i][1])
    else:
        insert(A[i][0], A[i][1], root)



print(findKth(root, 1).key)
print(findK(root.right.left.left))