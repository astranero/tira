def count(s):
    
    pituus = len(s)
    edellinen = s[0]
    edellinen_maara = 0
    vanhempi = None
    osajonot = 0
    
    jono_pituus = 0
    merkkimaara = 0
    for i in range(0, pituus):
        if vanhempi == None:
            vanhempi = s[i]

        elif s[i] == edellinen and vanhempi != edellinen:
            osajonot+=jono_pituus

        if s[i] != edellinen and s[i] != vanhempi:
            osajonot += (merkkimaara)
            merkkimaara = 0
            edellinen = s[i]
            vanhempi = edellinen
            jono_pituus = 0

        if s[i] != edellinen and s[i] == vanhempi:
            osajonot += (jono_pituus*2)
            
        if s[i] != edellinen:
            merkkimaara = 0
        
        jono_pituus +=1
        merkkimaara += 1

    return osajonot

if __name__ == "__main__":
    print(count("aaaa")) # 0
    print(count("abab")) # 6
    print(count("aabacba")) # 8
    print(count("abacaadbaaca")) # 21
    print(count("babbbabbba")) #39
    print(count("babbba"))
    print(count("bbab"))