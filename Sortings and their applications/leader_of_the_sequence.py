#check if there is x in sequence, that occur on more than half of positions in array, O(n) required

def leader(Arr):
    stack = 0
    for i in range(len(Arr)):
        if stack == 0:
            stack += 1
            temp = Arr[i]
        else:
            if Arr[i] != temp:
                stack -= 1
            else:
                stack += 1
    
    if stack > 0:
        counter = 0
        for i in range(len(Arr)):
            if Arr[i] == temp:
                counter += 1
        
        if counter > len(Arr)//2:
            return True
    
    return False

Arr = [2, 1, 2, 3, 2, 2, 2, 2, 1]
print(leader(Arr))