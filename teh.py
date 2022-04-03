def tehtava(A, B):
    A = sorted(A)
    B = sorted(B)
    
    taulukko = {}
    for i in range(0,len(A)):
        if A[i] not in taulukko:
            taulukko[A[i]] =1

    for i in range(0, len(A)):
        if B[i] in taulukko:
            taulukko[B[i]] +=1
        
    suurin = -1
    for key in taulukko:
        if key > suurin and taulukko[key] == 2:
            suurin = key

    return suurin
