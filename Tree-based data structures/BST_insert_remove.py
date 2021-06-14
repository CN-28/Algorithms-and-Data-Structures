class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None



def insert(root, key):
    newNode = BSTNode(key)
    y = None
    x = root
    while x:
        y = x
        if newNode.key < x.key:
            x = x.left
        else:
            x = x.right
    newNode.parent = y


    if not y:
        root = newNode
    else:
        if newNode.key < y.key:
            y.left = newNode
        elif newNode.key > y.key:
            y.right = newNode
    return root



def findMin(x):
    curr = x
    while curr.left:
        curr = curr.left
    return curr



def replace(root, newVal):
    temp = 0
    if root.parent:
        if root == root.parent.left:
            root.parent.left = newVal
            temp = 1
        else:
            root.parent.right = newVal
    if newVal:
        newVal.parent = root.parent
    if temp == 1:
        return root.parent.left
    else:
        return root.parent.right



def delete(root, key):
    if key < root.key:
        root.left = delete(root.left, key)
        return root
    if key > root.key:
        root.right = delete(root.right, key)
        return root
    

    if root.left and root.right:
        succ = findMin(root.right)
        root.key = succ.key
        succ = delete(succ, succ.key)
    elif root.left:
        root = replace(root, root.left)
    elif root.right:
        root = replace(root, root.right)
    else:
        root = replace(root, None)
    return root
 


root = None
root = insert(root, 4)
root = insert(root, 5)
root = insert(root, 3)
root = delete(root, 4)
print(root.left.key)