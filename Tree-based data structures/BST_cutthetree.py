class BNode:
    def __init__( self, value ):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def cutthetree(T): return cut(T.left) + cut(T.right)


def cut(T):
    if T.right and T.left: return min(cut(T.left) + cut(T.right), T.value)
    if T.right: return min(cut(T.right), T.value)
    if T.left: return min(cut(T.left), T.value)
    return float("inf")