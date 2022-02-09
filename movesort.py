def check(t):    
    n = int(len(t)/2)
    z = 1
    j = len(t)-1
    tarkistus = []
    vertaus = []
    for i in range(0,n): 
        vertaus.append(z)
        tarkistus.append(abs(t[i]-t[j]))
        z+=2
        j-=1

    jar_list = sorted(tarkistus)
    for i in range(0,len(tarkistus)):
        if jar_list[i] != vertaus[i]: return False
    return True

if __name__ == "__main__":
    print(check([3,1,4,2])) # True
    print(check([4,5,6,1,2,3])) # True
    print(check([3,1,2,4])) # False
    print(check([1,2])) # True
    print(check([4,5,6,1,2,3])) # True
    print(check([4,5,6,3,2,1])) # False 
    print(check([5, 8, 13, 1, 3, 6, 11, 4, 9, 12, 14, 2, 7, 10]))
    print(check([19, 8, 3, 1, 15, 9, 10, 2, 14, 4, 7, 5, 20, 16, 17, 13, 11, 6, 12, 18]))
   