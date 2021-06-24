"""
Find the minimum sum, such that from every leaf to root there is exactly one vertex added to sum.
Leaves are not connected directly to the root.
"""


class BNode:
    def __init__( self, value ):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def cut(T):
    if not T:
        return 0
    if not T.right and not T.left:
        return float("inf")
    return min(T.value, cut(T.left) + cut(T.right))


def cutthetree(T):
    return cut(T.left) + cut(T.right)