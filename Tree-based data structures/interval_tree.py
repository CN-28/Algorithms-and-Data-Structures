class Node:
    def __init__(self):
        self.cut    = None
        self.left   = None
        self.right  = None
        self.intervals = []
        self.lchild = None
        self.rchild = None
        self.leaf   = False



def tree_build(A, i, j, left, right):
    X = Node()
    X.left  = left
    X.right = right
    if (j < i):
        X.cut  = -1
        X.leaf = True
    else:
        m = (i + j) // 2
        X.cut   = A[m]
        X.lchild = tree_build(A, i, m - 1, left, A[m])
        X.rchild = tree_build(A, m + 1, j, A[m], right)
    return X


def tree(A):
    return tree_build(A, 0, len(A) - 1, min(A) - 1, max(A) + 1)



def tree_print(X, ind=""):

    if X.leaf:
        print(ind, "leaf-span: [%d, %d] --> " % (X.left, X.right), X.intervals);
    if not X.leaf:
        print(ind, "cut = %d," % X.cut, "span = [%d, %d], " % (X.left, X.right), "intervals =", X.intervals);
        tree_print(X.lchild, ind + "  ")
        tree_print(X.rchild, ind + "  ")



def tree_op( X, I, f):
    (a, b) = I
    if a <= X.left and b >= X.right:
        f(X,I)
        return
    if a < X.cut:
        tree_op(X.lchild, I, f)
    if b > X.cut:
        tree_op(X.rchild, I, f)


def tree_insert(X, I):
    tree_op( X, I, op_insert )

def op_insert(X,I):
    X.intervals.append(I)



def tree_remove(X, I):
    tree_op( X, I, op_remove )

def op_remove( X, I ):
    try:
        X.intervals.remove(I)
    except ValueError:
        None



def tree_intersect(X, a):
    R = X.intervals.copy()
    if X.leaf:
        return R
    if a <= X.cut:
        R += tree_intersect(X.lchild, a)
    if a >= X.cut:
        R += tree_intersect(X.rchild, a)
    return R