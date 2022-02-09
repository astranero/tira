def count(n):
    lukumaara = 0
    for i in range(1, n+1):
        for j in range(1, n+1):

            for x in range(1, n+1):
                for y in range(1, n+1):

                    if collision(i, j , x , y):
                        lukumaara +=1
    return lukumaara

def collision(i, j , x, y):
    if x == i or y == j or abs(x-i) == abs(y-j):
        return False
    if (x, y) == (i + 2, j + 1):
        return False
    if (x, y) == (i + 2, j - 1):
        return False
    if (x, y) == (i - 2, j + 1):
        return False
    if (x, y) == (i -2, j - 1):
        return False
    if (x, y) == (i + 1, j + 2):
        return False
    if (x, y) == (i + 1, j - 2):
        return False
    if (x, y) == (i - 1, j + 2):
        return False
    if (x, y) == (i - 1, j - 2):
        return False
    return True

if __name__ == "__main__":
    print(count(3)) # 0
    print(count(4)) # 40
    print(count(5)) # 184
    print(count(150))