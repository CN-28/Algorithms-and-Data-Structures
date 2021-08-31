class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        


def inorderTraversal(root):
    if not root:
        return
    inorderTraversal(root.left)
    print(root.key)
    inorderTraversal(root.right)