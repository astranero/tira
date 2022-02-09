def sort(t,a,b):
    if a >= b:
        return
    k = divide(t,a,b)
    print(t)
    sort(t,a,k-1)
    sort(t,k+1,b)

def divide(t,a,b):
    k = a
    for i in range(a+1,b+1):
        if t[i] < t[a]:
            k+=1
            swap(t,i,k)
            
    swap(t,a,k)
    return k

def swap(t,a,b):
    k = t[a]
    t[a] = t[b]
    t[b] = k
    

if __name__ == "__main__":
    t = [7,8,6]
    a = 0
    b = len(t)-1
    sort(t, a, b)
    