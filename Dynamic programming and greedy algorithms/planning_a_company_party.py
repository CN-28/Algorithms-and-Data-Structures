"""
The company has a hierarchical structure, that is, the supervisor relation forms
a tree rooted at the president. The personnel office has ranked each employee with
with a convivality rating, which is a real number. In order to make the party fun
for all attendees, the president does not want both an employee and his or her immediate
supervisor to attend. Implement an algorithm to make up a guest list that maximizes the sum
of the conviviality ratings of the guests.
f(v) - value of the best party rooted in v
g(v) - value of the best party rooted in v, but v doesn't attend this party

g(v) = (for all u in v.children) Σ f(u)
f(v) = max(g(v), v.fun + (for all u in v.children) Σ g(u))
Time complexity: O(n**2)
"""
class Node:
    def __init__(self, fun):
        self.fun = fun
        self.children = []
        self.f = -1
        self.g = -1



def f(v):
    if v.f >= 0:
        return v.f

    x = v.fun
    for u in v.children:
        x += g(u)
    
    v.f = max(g(v), x)
    return v.f



def g(v):
    if v.g >= 0:
        return v.g

    v.g = 0
    for u in v.children:
        v.g += f(u)

    return v.g



def makeTree():
    T = Node(25)
    T.children.append(Node(28))
    T.children.append(Node(10))
    T.children.append(Node(100))
    T.children[0].children.append(Node(1))
    T.children[0].children[0].children.append(Node(0))
    T.children[0].children[0].children.append(Node(0))
    T.children[0].children[0].children.append(Node(0))
    T.children[0].children[0].children.append(Node(100))
    T.children[1].children.append(Node(35))
    T.children[1].children.append(Node(15))
    T.children[1].children.append(Node(20))
    T.children[2].children.append(Node(29))
    T.children[2].children.append(Node(50))
    T.children[2].children[0].children.append(Node(17))
    T.children[2].children[0].children.append(Node(45))
    T.children[2].children[0].children[1].children.append(Node(2))
    T.children[2].children[0].children[1].children.append(Node(700))
    return T



v = makeTree()
print(f(v))