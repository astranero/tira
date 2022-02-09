from itertools import combinations, count


def find(t,x):
    sorted_t = sorted(t)
    
    i = 0
    j = len(sorted_t)-1
    counter = 0
    j_arvo = j
    sum = 0
    
    while i < j:
        if sorted_t[i] + sorted_t[j] <= x:
            counter += 1
            i += 1
        elif sorted_t[i] + sorted_t[j]>x:
            sum += counter
            j_arvo = j
            j-=1

    j = j_arvo-1
    for i in range(j,-1,-1): 
            sum += counter
            counter -= 1
    return sum
    
 
if __name__ == "__main__":
    print(find([1,2,3],4)) # 2
    print(find([5,2,4,7],10)) # 4
    print(find([1,1,1,1],2)) # 6
    print(find([1,1,1,1],1)) # 0
    print(find([8,8,1,2,5,1,9,3],9)) # 14
    print(find([1,1,1,2,3,4,4,4,4,4,7,7,7,7,7,7,8,9,10],8))
    #1 1 2 3 5 8 8 9