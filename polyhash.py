def hajautusfunktio(x):
    n = 997163
    return (x % n)

def polynomihajautus(s):
    a = 17
    p = len(s)-1

    sum = 0
    for alkio in s:
        sana = ord(alkio)
        kerroin = (a)**p
        sum += sana*kerroin
        p-=1

    print(hajautusfunktio(sum))

polynomihajautus("analfabeetti")
polynomihajautus("bazzibasuuki")
polynomihajautus("cromagnonlainen")
polynomihajautus("dipsomaani")
polynomihajautus("ektoplasma")