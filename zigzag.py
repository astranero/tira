def create(n):

    parilliset = []
    parittomat = []
    for i in range(2,n+1):
        if i % 2 == 0:
            parilliset.append(i)
        else:
            parittomat.append(i)

    palautus_lista = sorted(parittomat, reverse=True)
    palautus_lista.append(1)
    for seed in parilliset:
        palautus_lista.append(seed)
    return palautus_lista

if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(2)) # [1,2]
    print(create(3)) # [3,1,2]
    print(create(4)) # [3,1,2,4]
    print(create(5)) # [5,3,1,2,4]