def count(n):
    shakkilauta = []
    for i in range(n):
        shakkilauta.append([])
    
    for i in range(n):
        for j in range(n):
            shakkilauta[i].append(j)
    print(shakkilauta)

if __name__ == "__main__":
    print(count(3)) # 0
    print(count(4)) # 40
    print(count(5)) # 184