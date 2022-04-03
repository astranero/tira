from re import I
import string
from itertools import permutations
def find(s):
    aakkoset_pituus = string.ascii_lowercase
    
    j = 5
    for i in range(4,0,-1): 
        lista = set(permutations(s,i))

        for c in permutations(aakkoset_pituus,i):
            if c not in lista: 
                j-=1
                break
    if j == 5: return 2
    return j
        
        

if __name__ == "__main__":
    print(find("abac"))
    print(find("zzz")) # 1
    print(find("aybabtu")) # 1
    print(find("abcdefghijklmnopqrstuvwxyz")) # 2
