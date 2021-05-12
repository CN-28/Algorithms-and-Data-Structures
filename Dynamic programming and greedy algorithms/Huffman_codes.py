from queue import PriorityQueue

def huffman(S, F):
    n = len(F)
    queue = PriorityQueue()
    for i in range(n):
        queue.put((F[i], S[i]))
    

    cnt = 0
    total = 0
    for i in range(n - 1):
        left = queue.get(False)
        right = queue.get(False)

        
        cnt = left[0] + right[0]
        total += cnt
        queue.put((cnt, (left, right)))
    printAll(queue.get(False))
    print("bits needed:", total)



def printAll(head, temp=""):
    if type(head[1]) == str:
        print(head[1] + ": " + temp)
    else:
        printAll(head[1][0], temp + "0")
        printAll(head[1][1], temp + "1")
    

    
S = ["a", "b", "c" ,"d", "e", "f" ]
F = [10 , 11 , 7 , 13, 1 , 20]
huffman(S, F)