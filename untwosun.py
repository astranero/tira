def find(t,x):
    b = 0
    e = len(t)-1
    sorted_t = sorted(t)

    y=0
    for i in range(1,len(sorted_t)):
        if sorted_t[0]+sorted_t[-1] <= x:
            y= len(sorted_t)
            break
        elif sorted_t[0]+sorted_t[i] > x:
            y = i
            break
    sum = mergeSort(sorted_t,b,e,x,y)
    return sum

def mergeSort(sorted_t,b,e,x,y):
    m = (b+e)//2
    if b == e:
        sum = 0
        for i in range(b+1,y):
            if sorted_t[b]+sorted_t[i]<=x: 
                sum+=1
        return sum
    else: return mergeSort(sorted_t,b,m,x,y) + mergeSort(sorted_t,m+1,e,x,y)

 
if __name__ == "__main__":
    print(find([1,2,3],4)) # 2
    print(find([5,2,4,7],10)) # 4
    print(find([1,1,1,1],2)) # 6
    print(find([1,1,1,1],1)) # 0
    print(find([8,8,1,2,5,1,9,3],9)) # 14
    #1 1 2 3 5 8 8 9