from itertools import islice
 
 
def count(t,k):
    lista = []
    kirjasto = {}
    distinct_value = 0

    for i in range(k):
        if t[i] not in kirjasto:
            kirjasto[t[i]] = 1
        else:
            kirjasto[t[i]] += 1
    distinct_value = len(kirjasto)
    lista.append(distinct_value)

    for j in range(len(t)-k):
        kirjasto[t[j]] -= 1
        if kirjasto[t[j]] == 0:
            distinct_value -= 1
        if t[j+k] not in kirjasto:
            kirjasto[t[j+k]] = 1
        else:
            kirjasto[t[j+k]] += 1
        if kirjasto[t[j+k]] == 1:
            distinct_value += 1
        lista.append(distinct_value)
    return lista

if __name__ == "__main__":
    print(count([1,1,2,2],2)) # [1,2,1]
    print(count([1,1,1,1],4)) # [1]
    print(count([1,2,3,2,2,2],3)) # [3,2,2,1]
    