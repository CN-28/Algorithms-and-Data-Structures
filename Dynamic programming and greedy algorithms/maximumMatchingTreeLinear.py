#find the maximaxl matching in the tree in O(n) time
class Node:
    def __init__(self):
        self.children = []
        self.g = -1
        self.f = -1



def f(x):
    if x.f >= 0:
        return x.f


    maxi = 0
    for y in x.children:
        maxi = max(g(y) - f(y) + 1, maxi)

    suum = 0
    for y in x.children:
        suum += f(y)
    
    suum += maxi
    x.f = suum
    return x.f



def g(x):
    if x.g >= 0:
        return x.g
    
    x.g = 0
    for y in x.children:
        x.g += f(y)
    
    return x.g



def makeTree():
    root = Node()
    root.children.append(Node())
    root.children.append(Node())
    root.children.append(Node())
    root.children[0].children.append(Node())
    root.children[0].children.append(Node())
    root.children[1].children.append(Node())
    root.children[1].children.append(Node())
    root.children[2].children.append(Node())
    root.children[2].children.append(Node())
    return root



root = makeTree()
print(f(root))