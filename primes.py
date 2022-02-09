def count(n):
    total = 0
    for i in range(2,n+1):
        fail = False
        for j in range(2,i):
            if i%j == 0:
                fail = True
        if not fail:
            total +=1
    return total

if __name__ == "__main__":
    print(count(2)) # 1
    print(count(10)) # 4
    print(count(11)) # 5
    print(count(100)) # 25
    print(count(1000)) # 168