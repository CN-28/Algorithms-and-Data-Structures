#assuming we don't insert into empty tree and delete the last node of the tree
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.right = None
        self.left = None



def insert(root, key):
    x = root
    while x:
        y = x
        if key > x.key:
            x = x.right
            if not x:
                y.right = BSTNode(key)
                y.right.parent = y
                return True
        elif key < x.key:
            x = x.left
            if not x:
                y.left = BSTNode(key)
                y.left.parent = y
                return True
        else:
            return False



def findMin(x):
    while x.left:
        x = x.left
    return x


def nextRightTree(x):
    if x.right:
        return findMin(x.right)



def remove(root, key):
    if not root:
        return False

    x = root
    while x:
        y = x
        if key > x.key:
            x = x.right
        elif key < x.key:
            x = x.left
        else:
            break
    
    
    if y.key == key:
        #no children
        if not y.right and not y.left:
            if y.parent.right and y.parent.right == y:
                y.parent.right = None
            else:
                y.parent.left = None
            return True
        #one child
        elif not y.left and y.right:
            y.right.parent = y.parent
            if y.parent.left == y:
                y.parent.left = y.right
            else:
                y.parent.right = y.right
            return True
        
        elif not y.right and y.left:
            y.left.parent = y.parent
            if y.parent.left == y:
                y.parent.left = y.left 
            else:
                y.parent.right = y.left
            return True
        #two children
        else:
            next = nextRightTree(y)
            y.key, next.key = next.key, y.key
            remove(next, key)
            return True


    return False



root = BSTNode(20)
A = [27, 18, 25, 29, 28, 30, 26, 24]
for key in A:
    insert(root, key)
remove(root, 29)