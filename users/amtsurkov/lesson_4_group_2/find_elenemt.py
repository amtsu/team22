def find_elenemt(element, lists):
    k = 0
    for i in lists:
        if element == i:
            return k
        k += 1
    return -1

#print(find_elenemt('Misha', ['Vast', 'Petya', 'Misha', 'Vova']))