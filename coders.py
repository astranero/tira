from re import A


def find(a,b):
    lista_a = sorted(a)
    lista_b = sorted(b)

    sum = 0
    for i in range(0,len(lista_a)):
        sum += abs(lista_a[i]-lista_b[i])
    return sum
    
if __name__ == "__main__":
    print(find([1,2,3],[2,5,2])) # 3
    print(find([2],[7])) # 5
    print(find([1,1,1,1],[3,4,3,4])) # 10
    print(find([5,2,9,1,2,4],[8,8,2,3,9,4])) # 11