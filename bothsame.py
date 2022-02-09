def count(s):
    # TODO
    merkkijono = ""
    osajonojen_lukumaara = 0

    lukumaara_kirjasto = {}
    for merkki in s:
        if merkki in merkkijono:
            maara = lukumaara_kirjasto[merkki]
            osajonojen_lukumaara += (maara + 1)
            lukumaara_kirjasto[merkki] += 1

        if merkki not in merkkijono:
            lukumaara_kirjasto[merkki] = 1
            osajonojen_lukumaara +=1  
        merkkijono += merkki
        
    return osajonojen_lukumaara

if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abcd")) # 4
    print(count("ababca")) # 10