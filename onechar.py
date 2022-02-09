def count(s):
    merkki = [0]
    osajonojen_maara = 0
    lukumaara = 1
    
    for alkio in s:
        if alkio == merkki:
            osajonojen_maara += lukumaara
            lukumaara += 1
        if alkio != merkki:
            merkki = alkio
            lukumaara = 1
            osajonojen_maara += lukumaara
            lukumaara += 1

    return osajonojen_maara

if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5