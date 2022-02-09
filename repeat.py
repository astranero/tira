def find(s):
    kirjaimet = list(s)
    merkkijono = ""
    
    for kirjain in kirjaimet:
        merkkijono += kirjain
        for i in range(len(kirjaimet)+1):
            if i*merkkijono == s:
                return len(merkkijono)
        
if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7