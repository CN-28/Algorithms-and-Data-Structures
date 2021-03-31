#selection sort
def SelectionSort(tab):
    for i in range(len(tab)):
        mini = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[mini]:
                mini = j  
        tab[mini], tab[i] = tab[i], tab[mini]

tab = [4,1,3,5]
SelectionSort(tab)
print("Selection sort", tab)


#bubble sort
def BubbleSort(tab):
    for i in range(len(tab)):
        for j in range(1, len(tab)):
            if tab[j] < tab[j - 1]:
                tab[j], tab[j - 1] = tab[j - 1], tab[j]

tab = [4,1,3,5]
BubbleSort(tab)
print("Bubble sort", tab)


#insertion sort
def InsertionSort(tab):
    for i in range(1, len(tab)):
        elem = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > elem:
            tab[j + 1] = tab[j]
            j = j - 1
        tab[j + 1] = elem

tab = [4,1,3,5]
InsertionSort(tab)
print("Insertion sort", tab)