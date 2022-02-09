def difference(t):

    l = sorted(t)
    smallest = abs(t[0]-t[len(l)-1])
    j = 1
    for i in range(0,len(l)):
        if j == len(l):
            break
        if abs(l[i] - l[j]) < smallest:
            smallest = abs(l[i]-l[j])
        j +=1

    return smallest

if __name__ == "__main__":
    print(difference([1,3,5,6,9]))
