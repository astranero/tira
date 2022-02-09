from os import listxattr


def count(s):
    
    # Lasketaan listan lukujen summa
    # Jaetaan summa kahdella saadaan taulukon eri osien alkioiden summat.
    # Käydään läpi alkiot, jos alkioiden summa saavuttaa eri osien alkioiden summan, niin alustetaan muuttuja alkio_summa
    #  Kasvatetaan osien_maara yhdellä

    summa = 0
    for alkio in s:
        summa += alkio
    
    osa_summa = (summa / 2)
    alkio_summa = 0
    
    osien_maara = 0
    for alkio in s:
        if alkio_summa == osa_summa:
            alkio_summa = alkio
            osien_maara += 1
        alkio_summa += alkio

    return osien_maara

if __name__ == "__main__":
    print(count([1,0,3,-1,4,-3,5,-1])) # 2
    print(count([1,2,3,4,1,2,3,4])) #1
    print(count([1,2,3,0,1,2,3])) #1
    print(count([1,2,3,4,1,2,3])) #0


