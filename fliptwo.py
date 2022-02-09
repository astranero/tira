import collections 
def solve(n,k):
    
    lista = collections.deque()
    for i in range(1,n+1):
        lista.append(i)
    
    for i in range(0,k):
        eka = lista.popleft()
        toka = lista.popleft()
        lista.append(toka)
        lista.append(eka)
    
    arvo = lista[0]
    return arvo
    

if __name__ == "__main__":
    print(solve(4,3)) # 4
    print(solve(12,5)) # 11
    print(solve(99,555)) # 11
    print(solve(12345,54321)) # 9875