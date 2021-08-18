from queue import PriorityQueue
class Node:
    def __init__(self, freq=None, char=None, index=-1):
        self.char = char
        self.freq = freq
        self.right = None
        self.left = None
        self.index = index



def huffman( S, F ):
    n = len(S)
    Q = PriorityQueue()
    for i in range(n):
        Q.put((F[i], Node(F[i], S[i], i)))
    

    for i in range(n - 1):
        z = Node()
        _, z.right = Q.get()
        _, z.left = Q.get()
        z.freq = z.left.freq + z.right.freq
        z.char = z.left.char + z.right.char
        Q.put((z.freq, z))


    _, root = Q.get()
    res = [None for _ in range(n)]
    cnt = printSymbolsBits(root, res)
    for i in range(n):
        print(S[i] + ":", res[i])
    print("bits needed", cnt)



def printSymbolsBits(root, res, num="", cnt=0):
    if not root.left and not root.right:
        res[root.index] = num
        cnt += len(num) * root.freq
        return cnt

    if root.left:
        cnt = printSymbolsBits(root.left, res, num + "0", cnt)
    if root.right:
        cnt = printSymbolsBits(root.right, res, num + "1", cnt)
    
    return cnt


  
S = ["a", "b", "c", "d", "e", "f"]
F = [10, 11, 7, 13, 1, 20]
huffman( S, F )