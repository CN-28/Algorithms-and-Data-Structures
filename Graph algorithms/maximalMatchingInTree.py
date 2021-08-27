from maxFlowEdmondsKarp import edmonds_karp
class Node:
    def __init__(self):
        self.children = []
        self.time = -1



def maxMatching(root):
    def cntNode(root):
        if root.children == []:
            return 1

        cnt = 0
        for i in range(len(root.children)):
            cnt += cntNode(root.children[i])
        
        return cnt + 1


    cnt = cntNode(root)
    G = [[0 for _ in range(cnt + 2)] for _ in range(cnt + 2)]
    sources = [False for _ in range(cnt)]
    time = 0
    h = 0
    def DFSVisit(u, h, prev=-1):
        nonlocal time, G, sources
        if h % 2 == 0:
            sources[time] = True

        u.time = time
        time += 1
        for v in u.children:
            if v.time == -1:
                DFSVisit(v, h + 1, time - 1)
            G[u.time][v.time] = 1
            G[v.time][u.time] = 1


    DFSVisit(root, 0)
    for i in range(cnt):
        if sources[i]:
            G[cnt][i] = 1
        else:
            G[i][cnt + 1] = 1
    
    
    return edmonds_karp(G, cnt, cnt + 1)



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
print(maxMatching(root))