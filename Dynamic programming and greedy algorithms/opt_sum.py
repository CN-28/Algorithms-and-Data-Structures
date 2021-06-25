def opt_sum(tab):
    n = len(tab)
    tab.sort()
    sum = tab[0] + tab[n - 1]
    mini = abs(sum)
    i = 1
    j = n - 1
    while i < j:
        if abs(sum + tab[i]) < abs(sum + tab[j]):
            sum += tab[i]
            if abs(sum) > mini:
                mini = abs(sum)
            i += 1
        else:
            sum = sum + tab[j]
            if abs(sum) > mini:
                mini = abs(sum)
            j -= 1
    return mini



tab = [-9, -3, 2, 3, 4, 5]
print(opt_sum(tab))