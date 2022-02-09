def count(t):

    lista_minimit = []
    pienin = t[-1]
    for i in range(len(t)-1,-1,-1):
        if t[i] < pienin:
            pienin = t[i]
        lista_minimit.append(pienin)
    
    lista_minimit.reverse()
    
    osa_jonot = 0
    suurin = t[0]
    for i in range(0,len(t)):
        if suurin < lista_minimit[i]:
            osa_jonot += 1
        if t[i] > suurin:
            suurin = t[i]
    return osa_jonot


if __name__ == "__main__":
    print(count([1,2,3,4,5])) # 4
    print(count([5,4,3,2,1])) # 0
    print(count([2,1,2,5,7,6,9])) # 3
    print(count([1,2,3,1])) # 0
    print(count([9, 6, 10, 10, 3, 6, 7, 6, 5, 7])) #0
    print(count([1, 1, 4, 4, 2, 5, 4, 8, 10, 6])) #2
    print(count([6, 2, 7, 7])) #1
    print(count([7, 5, 1, 6, 10, 2, 8])) #0