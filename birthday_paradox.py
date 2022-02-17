def laskuri():
    n = 1000000
    tod = 0
    alkiot = 0
    for i in range(1,n):
        if tod > (1/2): break
        alkiot += 1
        tod += (i/n)
    print(alkiot)
laskuri()