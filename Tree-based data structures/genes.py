class Node:
    def __init__(self):
        self.A = None
        self.C = None
        self.T = None
        self.G = None



def check(genes):
    root = Node()
    n = len(genes)
    for i in range(n):
        m = len(genes[i])
        tempRoot = root
        for j in range(m):
            if genes[i][j] == "A":
                if j == m - 1 and tempRoot.A:
                    return False
                if not tempRoot.A:
                    tempRoot.A = Node()
                    tempRoot = tempRoot.A

            elif genes[i][j] == "C":
                if j == m - 1 and tempRoot.C:
                    return False
                if not tempRoot.C:
                    tempRoot.C = Node()
                    tempRoot = tempRoot.C

            elif genes[i][j] == "T":
                if j == m - 1 and tempRoot.T:
                    return False
                if not tempRoot.T:
                    tempRoot.T = Node()
                    tempRoot = tempRoot.T

            elif genes[i][j] == "G":
                if j == m - 1 and tempRoot.G:
                    return False
                if not tempRoot.G:
                    tempRoot.G = Node()
                    tempRoot = tempRoot.G
    

    return True
            


genes = ["GAT", "ACT", "ACTG", "GATCG"]
print(check(genes))