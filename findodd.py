from re import A


def find(t):
    
    kirja = {}
    for alkio in t:
        kirja[alkio] = 0
        
    for alkio in t:
        kirja[alkio] += 1

    luku = 0
    for alkio in t:
        if kirja[alkio] == 1:
            luku = alkio
    return luku

if __name__ == "__main__":
    print(find([2,2,4,3,4])) # 3
    print(find([1,2,3,4,1,2,3])) # 4
    print(find([1])) # 1
    print(find([1,4,2,3,2,3,4])) # 1
    print(find([4,1,3,2,3,2,1])) # 4