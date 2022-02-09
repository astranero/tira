def count(s):
    
    pituus = len(s)
    edellinen = s[0]
    vanhempi = None
    osajonot = 0
    
    jono_pituus = 0
    merkkimaara = 0
    #babbbabbba
    for i in range(0,pituus):
        if s[i] != edellinen and vanhempi == None:
            osajonot+=jono_pituus
            merkkimaara = 0
            vanhempi = s[i-1]
            edellinen = s[i]
 
        elif s[i] == edellinen and s[i] != vanhempi and vanhempi != None:
            osajonot+=(jono_pituus-merkkimaara)
 
        elif s[i] != edellinen and s[i] == vanhempi and vanhempi != None:
            osajonot +=(jono_pituus)
            vanhempi = edellinen
            merkkimaara = 0
            edellinen = s[i]
 
        elif s[i] != edellinen and s[i] != vanhempi and vanhempi != None:
            osajonot += (merkkimaara)
            vanhempi = edellinen
            jono_pituus = merkkimaara
            merkkimaara = 0
            edellinen = s[i]

        jono_pituus +=1
        merkkimaara += 1
    return osajonot
 
if __name__ == "__main__":
    print(count("aaaa")) # 0
    print(count("abab")) # 6
    print(count("aabacba")) # 8
    print(count("abacaadbaacaa")) # 21
    print(count("babbbabbba")) #39
    print(count("babbba"))
    print(count("bbab"))